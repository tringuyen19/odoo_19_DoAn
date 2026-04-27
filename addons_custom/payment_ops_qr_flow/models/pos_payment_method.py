from urllib.parse import quote_plus

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    manual_bank_qr_enabled = fields.Boolean(
        string="Manual Bank QR (No Accounting)",
        default=False,
        help="Show manual transfer QR in POS payment screen without accounting integration.",
    )

    @api.model
    def _load_pos_data_fields(self, config):
        fields_list = super()._load_pos_data_fields(config)
        if "manual_bank_qr_enabled" not in fields_list:
            fields_list.append("manual_bank_qr_enabled")
        return fields_list

    @api.model
    def get_manual_qr_payload(self, payment_method_id, amount, reference):
        method = self.browse(payment_method_id).exists()
        if not method:
            raise UserError(_("Payment method is not found."))
        if not method.manual_bank_qr_enabled:
            raise UserError(_("This payment method is not configured for manual bank QR."))

        company = method.company_id or self.env.company
        bank_bin = (company.payment_qr_bank_bin or "").strip()
        account_no = (company.payment_qr_account_number or "").strip()
        account_name = (company.payment_qr_account_name or "").strip()
        if not bank_bin or not account_no or not account_name:
            raise UserError(
                _(
                    "Missing Payment QR setup. Please configure bank BIN, account number, and account name in Settings."
                )
            )

        amount_value = max(0, int(round(float(amount or 0.0))))
        ref_text = (reference or "").strip() or _("POS Payment")
        query = (
            f"amount={amount_value}"
            f"&addInfo={quote_plus(ref_text)}"
            f"&accountName={quote_plus(account_name)}"
        )
        image_url = f"https://img.vietqr.io/image/{bank_bin}-{account_no}-compact2.png?{query}"

        return {
            "image_url": image_url,
            "account_name": account_name,
            "account_number": account_no,
            "amount": amount_value,
            "reference": ref_text,
            "bank_bin": bank_bin,
        }
