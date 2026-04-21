from odoo import _, api, models
from odoo.fields import Command
from odoo.exceptions import UserError


class PosOrder(models.Model):
    _inherit = "pos.order"

    @api.model
    def create_draft_quotation_from_pos(self, payload):
        partner_id = payload.get("partner_id")
        line_payloads = payload.get("lines", [])
        if not partner_id:
            raise UserError(_("Please select a customer before creating a quotation."))
        if not line_payloads:
            raise UserError(_("No order lines found to create a quotation."))

        partner = self.env["res.partner"].browse(partner_id).exists()
        if not partner:
            raise UserError(_("Customer not found."))

        order_lines = []
        for line in line_payloads:
            product_id = line.get("product_id")
            qty = line.get("qty", 0)
            if not product_id or qty <= 0:
                continue
            order_lines.append(
                Command.create(
                    {
                        "product_id": product_id,
                        "product_uom_qty": qty,
                    }
                )
            )

        if not order_lines:
            raise UserError(_("No valid lines to create a quotation."))

        sale_order = self.env["sale.order"].create(
            {
                "partner_id": partner.id,
                "pricelist_id": partner.property_product_pricelist.id,
                "origin": payload.get("origin", _("POS cart")),
                "note": _("Created automatically from POS due to insufficient stock."),
                "order_line": order_lines,
            }
        )
        return {"sale_order_id": sale_order.id, "sale_order_name": sale_order.name}
