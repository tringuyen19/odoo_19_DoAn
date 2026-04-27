from odoo import api, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.model
    def scan_receipt_barcode(self, barcode, current_picking_id=False):
        code = (barcode or "").strip()
        if not code:
            return {"status": "empty"}

        product = self.env["product.product"].search([("barcode", "=", code)], limit=1)
        if not product:
            return {"status": "product_not_found", "barcode": code}

        open_receipt_domain = [
            ("picking_type_code", "=", "incoming"),
            ("state", "in", ["assigned", "confirmed", "waiting"]),
            ("move_ids.product_id", "=", product.id),
        ]
        candidate_receipts = self.search(open_receipt_domain, order="priority desc, scheduled_date asc, id asc")
        if not candidate_receipts:
            return {
                "status": "not_in_open_receipts",
                "barcode": code,
                "product_display_name": product.display_name,
            }

        target_receipt = False
        if current_picking_id:
            current_receipt = self.browse(current_picking_id).exists()
            if current_receipt and current_receipt in candidate_receipts:
                target_receipt = current_receipt

        if not target_receipt and len(candidate_receipts) == 1:
            target_receipt = candidate_receipts[0]

        if not target_receipt:
            return {
                "status": "multiple_receipts",
                "barcode": code,
                "product_display_name": product.display_name,
                "receipt_suggestions": [
                    {"id": receipt.id, "name": receipt.name}
                    for receipt in candidate_receipts[:5]
                ],
            }

        target_move = target_receipt.move_ids.filtered(
            lambda move: move.state not in ("done", "cancel") and move.product_id == product
        )[:1]
        if not target_move:
            return {
                "status": "wrong_receipt",
                "barcode": code,
                "receipt_id": target_receipt.id,
                "receipt_name": target_receipt.name,
                "product_display_name": product.display_name,
            }

        return {
            "status": "ok",
            "barcode": code,
            "receipt_id": target_receipt.id,
            "receipt_name": target_receipt.name,
            "product_display_name": product.display_name,
        }
