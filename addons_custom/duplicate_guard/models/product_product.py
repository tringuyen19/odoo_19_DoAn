from odoo import _, api, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    def _find_duplicate_product_for_warning(self):
        self.ensure_one()
        product_id = self._origin.id or self.id
        domain = [("id", "!=", product_id)]

        if self.default_code:
            product_by_code = self.env["product.product"].search(
                domain + [("default_code", "=", self.default_code)],
                limit=1,
            )
            if product_by_code:
                return product_by_code, "sku"

        if self.name:
            product_by_name = self.env["product.product"].search(
                domain + [("name", "=ilike", self.name)],
                limit=1,
            )
            if product_by_name:
                return product_by_name, "name"

        return self.env["product.product"], ""

    def _build_duplicate_product_warning_message(self, duplicate_product, matched_by):
        self.ensure_one()
        reason = _("Ma SKU") if matched_by == "sku" else _("Ten san pham")
        return _(
            "%(reason)s da ton tai.\n\n"
            "San pham tim thay:\n"
            "- Ten: %(name)s\n"
            "- SKU: %(sku)s\n"
            "- Gia ban: %(price).0f\n"
            "- Ton kho: %(stock).2f\n\n"
            "Nen su dung ban ghi san pham da co hoac doi ma/ten de tranh trung.",
            reason=reason,
            name=duplicate_product.display_name or "-",
            sku=duplicate_product.default_code or "-",
            price=duplicate_product.lst_price or 0.0,
            stock=duplicate_product.qty_available if "qty_available" in duplicate_product._fields else 0.0,
        )

    @api.onchange("default_code", "name")
    def _onchange_duplicate_product_warning(self):
        duplicate_product, matched_by = self._find_duplicate_product_for_warning()
        if duplicate_product:
            return {
                "warning": {
                    "title": _("Canh bao trung san pham"),
                    "message": self._build_duplicate_product_warning_message(duplicate_product, matched_by),
                }
            }


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.onchange("default_code", "name")
    def _onchange_duplicate_product_warning(self):
        for template in self:
            variant = template.product_variant_id
            if not variant:
                continue
            duplicate_product, matched_by = variant._find_duplicate_product_for_warning()
            if duplicate_product:
                return {
                    "warning": {
                        "title": _("Canh bao trung san pham"),
                        "message": variant._build_duplicate_product_warning_message(duplicate_product, matched_by),
                    }
                }
