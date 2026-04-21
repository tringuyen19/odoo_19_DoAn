from odoo import _, models
from odoo.fields import Domain


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_apply_eligible_promos(self):
        self.ensure_one()
        self._update_programs_and_rewards()

        trigger_domain = Domain.AND([self._get_trigger_domain(), [("mode", "=", "with_code")]])
        candidate_rules = self.env["loyalty.rule"].search(trigger_domain)

        applied_count = 0
        for rule in candidate_rules:
            status = self._try_apply_code(rule.code)
            if "error" in status:
                continue
            applied_count += 1

        self._update_programs_and_rewards()
        claimable_rewards = self._get_claimable_rewards()
        if claimable_rewards:
            # Same behavior as native flow: auto-apply if unambiguous, open wizard otherwise.
            return self.action_open_reward_wizard()

        if applied_count:
            return {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "title": _("Promotions Applied"),
                    "message": _("Applied %(count)s eligible promotion code(s).", count=applied_count),
                    "type": "success",
                    "sticky": False,
                },
            }

        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": _("No Eligible Promotion"),
                "message": _("No discount-code program is currently applicable for this quotation."),
                "type": "warning",
                "sticky": False,
            },
        }
