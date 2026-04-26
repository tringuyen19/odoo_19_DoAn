from uuid import uuid4

from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    mobile_barcode_enabled = fields.Boolean(
        string="Enable Mobile Barcode Scanner",
        default=True,
        help="Allow phone camera scanning and push barcode to this POS in real time.",
    )
    mobile_barcode_token = fields.Char(
        string="Mobile Scanner Token",
        default=lambda self: uuid4().hex,
        copy=False,
        readonly=True,
    )
    mobile_barcode_url = fields.Char(
        string="Mobile Scanner URL",
        compute="_compute_mobile_barcode_url",
    )

    def _compute_mobile_barcode_url(self):
        base_url = self.env["ir.config_parameter"].sudo().get_param("web.base.url", "")
        for config in self:
            if config.mobile_barcode_token:
                config.mobile_barcode_url = (
                    f"{base_url}/pos/mobile_scanner/{config.id}/{config.mobile_barcode_token}"
                )
            else:
                config.mobile_barcode_url = False

    def action_regenerate_mobile_barcode_token(self):
        for config in self:
            config.mobile_barcode_token = uuid4().hex
