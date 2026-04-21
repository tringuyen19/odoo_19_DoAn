import re

from odoo import _, api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _normalize_phone_for_duplicate(self, value):
        if not value:
            return ""
        return re.sub(r"\D", "", value)

    def _find_duplicate_partner_by_phone(self):
        self.ensure_one()
        partner_id = self._origin.id or self.id
        normalized_phone = self._normalize_phone_for_duplicate(self.phone)
        if not normalized_phone:
            return self.env["res.partner"]

        candidates = self.env["res.partner"].with_context(active_test=False).search(
            [("id", "!=", partner_id)],
            limit=200,
        )
        for partner in candidates:
            partner_phone = self._normalize_phone_for_duplicate(partner.phone)
            if normalized_phone == partner_phone:
                return partner
        return self.env["res.partner"]

    def _build_duplicate_partner_warning_message(self, duplicate_partner):
        self.ensure_one()
        sales_count = 0
        total_spent = 0.0
        if "sale.order" in self.env:
            sale_orders = self.env["sale.order"].search([
                ("partner_id", "child_of", duplicate_partner.commercial_partner_id.id),
                ("state", "in", ["sale", "done"]),
            ])
            sales_count = len(sale_orders)
            total_spent = sum(sale_orders.mapped("amount_total"))

        return _(
            "Khach hang co the da ton tai.\n\n"
            "Thong tin tim thay:\n"
            "- Ten: %(name)s\n"
            "- SDT: %(phone)s\n"
            "- Email: %(email)s\n"
            "- So lan mua: %(sales_count)s\n"
            "- Tong chi tieu: %(total_spent).0f\n\n"
            "Neu dung la khach cu, hay mo ban ghi cu thay vi tao moi.",
            name=duplicate_partner.display_name or "-",
            phone=duplicate_partner.phone or "-",
            email=duplicate_partner.email or "-",
            sales_count=sales_count,
            total_spent=total_spent,
        )

    @api.onchange("phone")
    def _onchange_duplicate_phone_warning(self):
        if not self.phone:
            return
        duplicate_partner = self._find_duplicate_partner_by_phone()
        if duplicate_partner:
            return {
                "warning": {
                    "title": _("Canh bao trung khach hang"),
                    "message": self._build_duplicate_partner_warning_message(duplicate_partner),
                }
            }
