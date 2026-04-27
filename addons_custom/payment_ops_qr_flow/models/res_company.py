from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    payment_qr_bank_bin = fields.Char(
        string="Payment QR Bank BIN",
        help="Bank BIN used to build VietQR image URL (example: 970422).",
    )
    payment_qr_account_number = fields.Char(
        string="Payment QR Account Number",
        help="Receiver account number used in transfer QR.",
    )
    payment_qr_account_name = fields.Char(
        string="Payment QR Account Name",
        help="Receiver account name displayed in transfer QR.",
    )
