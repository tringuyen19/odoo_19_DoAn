from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        result = super().action_confirm()
        commercial_partners = self.mapped("partner_id.commercial_partner_id")
        if commercial_partners:
            commercial_partners.action_recompute_vip_tier()
        return result
