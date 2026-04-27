from urllib.parse import quote_plus

from odoo import _, fields, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    payment_flow_method = fields.Selection(
        selection=[
            ("bank_transfer", "Bank Transfer"),
            ("cod", "COD"),
        ],
        string="Payment Method (Ops)",
        default="bank_transfer",
        required=True,
    )
    payment_flow_state = fields.Selection(
        selection=[
            ("unpaid", "Unpaid"),
            ("waiting_transfer", "Waiting Transfer"),
            ("paid_confirmed", "Paid Confirmed"),
            ("cod_pending", "COD Pending"),
            ("cod_collected", "COD Collected"),
        ],
        string="Payment Status (Ops)",
        default="unpaid",
        copy=False,
        tracking=True,
    )
    transfer_qr_url = fields.Char(
        string="Transfer QR URL",
        compute="_compute_transfer_qr_url",
    )

    def _compute_transfer_qr_url(self):
        for order in self:
            order.transfer_qr_url = order._build_transfer_qr_url()

    def _build_transfer_qr_url(self):
        self.ensure_one()
        company = self.company_id
        bank_bin = (company.payment_qr_bank_bin or "").strip()
        account_no = (company.payment_qr_account_number or "").strip()
        account_name = (company.payment_qr_account_name or "").strip()
        if not bank_bin or not account_no or not account_name:
            return False

        amount_value = max(0, int(round(self.amount_total)))
        ref_text = (self.name or "").strip() or _("Sale Order")
        query = (
            f"amount={amount_value}"
            f"&addInfo={quote_plus(ref_text)}"
            f"&accountName={quote_plus(account_name)}"
        )
        return f"https://img.vietqr.io/image/{bank_bin}-{account_no}-compact2.png?{query}"

    def action_open_transfer_qr(self):
        self.ensure_one()
        if not self.transfer_qr_url:
            raise UserError(
                _(
                    "QR setup is incomplete. Please configure bank BIN, account number, and account name in Settings."
                )
            )
        return {
            "type": "ir.actions.act_url",
            "url": self.transfer_qr_url,
            "target": "new",
        }

    def action_mark_transfer_waiting(self):
        self.filtered(lambda so: so.payment_flow_method == "bank_transfer").write(
            {"payment_flow_state": "waiting_transfer"}
        )

    def action_mark_transfer_paid(self):
        self.filtered(lambda so: so.payment_flow_method == "bank_transfer").write(
            {"payment_flow_state": "paid_confirmed"}
        )

    def action_mark_cod_pending(self):
        self.filtered(lambda so: so.payment_flow_method == "cod").write(
            {"payment_flow_state": "cod_pending"}
        )

    def action_mark_cod_collected(self):
        self.filtered(lambda so: so.payment_flow_method == "cod").write(
            {"payment_flow_state": "cod_collected"}
        )

    def action_reset_payment_ops_state(self):
        self.write({"payment_flow_state": "unpaid"})

    def action_confirm(self):
        result = super().action_confirm()
        for order in self:
            if order.payment_flow_method == "bank_transfer" and order.payment_flow_state == "unpaid":
                order.payment_flow_state = "waiting_transfer"
            elif order.payment_flow_method == "cod" and order.payment_flow_state == "unpaid":
                order.payment_flow_state = "cod_pending"
        return result

    def _create_invoices(self, grouped=False, final=False, date=None):
        invoices = super()._create_invoices(grouped=grouped, final=final, date=date)
        self._auto_post_and_pay_ops_invoices(invoices)
        return invoices

    def _auto_post_and_pay_ops_invoices(self, invoices):
        if not invoices:
            return
        if "account.payment.register" not in self.env:
            return

        eligible_states = {"paid_confirmed", "cod_collected"}
        candidate_invoices = invoices.filtered(lambda inv: inv.move_type == "out_invoice")
        for invoice in candidate_invoices:
            related_orders = invoice.invoice_line_ids.sale_line_ids.order_id
            if not related_orders:
                continue
            if any(order.payment_flow_state not in eligible_states for order in related_orders):
                continue

            if invoice.state == "draft":
                invoice.action_post()
            if invoice.payment_state == "paid":
                continue

            register = (
                self.env["account.payment.register"]
                .with_context(active_model="account.move", active_ids=invoice.ids)
                .create(
                    {
                        "payment_date": fields.Date.context_today(self),
                        "amount": invoice.amount_residual,
                    }
                )
            )
            register._create_payments()
