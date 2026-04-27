from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    payment_qr_bank_bin = fields.Char(
        related="company_id.payment_qr_bank_bin",
        readonly=False,
    )
    payment_qr_account_number = fields.Char(
        related="company_id.payment_qr_account_number",
        readonly=False,
    )
    payment_qr_account_name = fields.Char(
        related="company_id.payment_qr_account_name",
        readonly=False,
    )
