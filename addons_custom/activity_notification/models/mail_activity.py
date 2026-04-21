from datetime import timedelta

from odoo import _, api, fields, models


class MailActivity(models.Model):
    _inherit = "mail.activity"

    urgency_level = fields.Selection(
        [
            ("urgent", "Urgent"),
            ("important", "Important"),
            ("info", "Info"),
        ],
        string="Urgency",
        default="important",
    )
    deadline_datetime = fields.Datetime(string="Due Datetime")
    reminder_sent = fields.Boolean(default=False)
    overdue_notice_sent = fields.Boolean(default=False)
    escalation_sent = fields.Boolean(default=False)

    @api.onchange("deadline_datetime")
    def _onchange_deadline_datetime(self):
        for activity in self:
            if activity.deadline_datetime:
                activity.date_deadline = fields.Datetime.to_datetime(activity.deadline_datetime).date()

    @api.onchange("date_deadline")
    def _onchange_date_deadline(self):
        for activity in self:
            if activity.date_deadline and not activity.deadline_datetime:
                activity.deadline_datetime = fields.Datetime.to_datetime(activity.date_deadline)

    def _send_simple_notification(self, partner, title, message, warning=False):
        notif_type = "warning" if warning else "success"
        self.env["bus.bus"]._sendone(
            partner,
            "simple_notification",
            {
                "title": title,
                "message": message,
                "type": notif_type,
                "sticky": warning,
            },
        )

    def _send_email_notification(self, activity, to_email, subject, body_html):
        if not to_email:
            return
        self.env["mail.mail"].sudo().create(
            {
                "subject": subject,
                "body_html": body_html,
                "email_to": to_email,
                "auto_delete": True,
            }
        ).send()

    def _get_activity_url(self, activity):
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url")
        if activity.res_model and activity.res_id:
            return f"{base_url}/odoo/{activity.res_model}/{activity.res_id}"
        return base_url

    @api.model
    def _cron_activity_deadline_reminder(self):
        now = fields.Datetime.now()
        in_one_hour = now + timedelta(hours=1)
        domain = [
            ("active", "=", True),
            ("user_id", "!=", False),
            ("deadline_datetime", "!=", False),
            ("deadline_datetime", ">=", now),
            ("deadline_datetime", "<=", in_one_hour),
            ("reminder_sent", "=", False),
        ]
        activities = self.sudo().search(domain)
        for activity in activities:
            if not activity.user_id.partner_id:
                continue
            self._send_simple_notification(
                activity.user_id.partner_id,
                _("Task reminder"),
                _("Task '%(task)s' is due at %(deadline)s.", task=activity.summary or activity.res_name, deadline=activity.deadline_datetime),
                warning=activity.urgency_level == "urgent",
            )
            activity.reminder_sent = True

    @api.model
    def _cron_activity_overdue_notification(self):
        now = fields.Datetime.now()
        domain = [
            ("active", "=", True),
            ("user_id", "!=", False),
            ("deadline_datetime", "!=", False),
            ("deadline_datetime", "<", now),
            ("overdue_notice_sent", "=", False),
        ]
        activities = self.sudo().search(domain)
        for activity in activities:
            url = self._get_activity_url(activity)
            task_name = activity.summary or activity.res_name or _("Task")
            self._send_simple_notification(
                activity.user_id.partner_id,
                _("Overdue task"),
                _("Task '%(task)s' is overdue.", task=task_name),
                warning=True,
            )
            self._send_email_notification(
                activity,
                activity.user_id.email,
                _("[System] Overdue task: %(task)s", task=task_name),
                _(
                    "<p>Hello %(user)s,</p>"
                    "<p>Your task <b>%(task)s</b> is overdue.</p>"
                    "<p>Deadline: %(deadline)s</p>"
                    "<p><a href='%(url)s'>Open related document</a></p>",
                    user=activity.user_id.name,
                    task=task_name,
                    deadline=activity.deadline_datetime,
                    url=url,
                ),
            )
            activity.overdue_notice_sent = True

    @api.model
    def _cron_activity_escalation_24h(self):
        now = fields.Datetime.now()
        threshold = now - timedelta(hours=24)
        activities = self.sudo().search(
            [
                ("active", "=", True),
                ("deadline_datetime", "!=", False),
                ("deadline_datetime", "<=", threshold),
                ("escalation_sent", "=", False),
            ]
        )
        manager_group = self.env.ref("base.group_erp_manager", raise_if_not_found=False)
        managers = manager_group.users if manager_group else self.env["res.users"]
        if not managers:
            return
        for activity in activities:
            task_name = activity.summary or activity.res_name or _("Task")
            url = self._get_activity_url(activity)
            for manager in managers:
                self._send_email_notification(
                    activity,
                    manager.email,
                    _("[Escalation] Task overdue > 24h: %(task)s", task=task_name),
                    _(
                        "<p>Hello %(manager)s,</p>"
                        "<p>Task <b>%(task)s</b> assigned to %(assignee)s is overdue for more than 24 hours.</p>"
                        "<p>Deadline: %(deadline)s</p>"
                        "<p><a href='%(url)s'>Open related document</a></p>",
                        manager=manager.name,
                        task=task_name,
                        assignee=activity.user_id.name,
                        deadline=activity.deadline_datetime,
                        url=url,
                    ),
                )
            activity.escalation_sent = True
