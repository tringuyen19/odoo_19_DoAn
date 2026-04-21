from collections import defaultdict

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    vip_tier_id = fields.Many2one("customer.vip.tier", string="VIP Tier", tracking=True)
    lifetime_purchase_amount = fields.Monetary(string="Lifetime Purchase", default=0.0, tracking=True)
    vip_currency_id = fields.Many2one(
        "res.currency",
        default=lambda self: self.env.company.currency_id.id,
    )
    vip_last_compute_date = fields.Datetime(string="VIP Last Recompute")
    vip_pricelist_auto = fields.Boolean(string="VIP Pricelist Auto", default=False)

    def _get_sale_amounts_by_commercial_partner(self):
        totals = defaultdict(float)
        sale_orders = self.env["sale.order"].sudo().search(
            [("state", "in", ["sale", "done"])]
        )
        for order in sale_orders:
            commercial_partner = order.partner_id.commercial_partner_id
            if not commercial_partner:
                continue
            amount_company_currency = order.currency_id._convert(
                order.amount_total,
                order.company_id.currency_id,
                order.company_id,
                order.date_order or fields.Datetime.now(),
            )
            totals[commercial_partner.id] += amount_company_currency
        return totals

    def _get_pos_amounts_by_commercial_partner(self):
        totals = defaultdict(float)
        if "pos.order" not in self.env:
            return totals
        pos_orders = self.env["pos.order"].sudo().search(
            [("state", "in", ["paid", "done"]), ("partner_id", "!=", False)]
        )
        for order in pos_orders:
            commercial_partner = order.partner_id.commercial_partner_id
            if not commercial_partner:
                continue
            amount_company_currency = order.currency_id._convert(
                order.amount_total,
                order.company_id.currency_id,
                order.company_id,
                order.date_order or fields.Datetime.now(),
            )
            totals[commercial_partner.id] += amount_company_currency
        return totals

    def _get_matching_vip_tier(self, company, amount):
        tiers = self.env["customer.vip.tier"].sudo().search(
            [
                ("active", "=", True),
                ("company_id", "in", [False, company.id]),
                ("min_amount", "<=", amount),
            ],
            order="min_amount desc, id asc",
            limit=1,
        )
        return tiers[:1]

    def _apply_vip_result(self, tier, amount):
        self.ensure_one()
        vals = {
            "lifetime_purchase_amount": amount,
            "vip_currency_id": self.company_id.currency_id.id or self.env.company.currency_id.id,
            "vip_tier_id": tier.id if tier else False,
            "vip_last_compute_date": fields.Datetime.now(),
        }
        if tier:
            vals.update(
                {
                    "property_product_pricelist": tier.pricelist_id.id,
                    "vip_pricelist_auto": True,
                }
            )
        elif self.vip_pricelist_auto:
            vals.update(
                {
                    "property_product_pricelist": False,
                    "vip_pricelist_auto": False,
                }
            )
        self.write(vals)

    def _recompute_vip_tier_for_commercial_partners(self):
        commercial_partners = self.filtered(lambda p: not p.parent_id)
        sale_totals = self._get_sale_amounts_by_commercial_partner()
        pos_totals = self._get_pos_amounts_by_commercial_partner()
        for partner in commercial_partners:
            total_amount = sale_totals.get(partner.id, 0.0) + pos_totals.get(partner.id, 0.0)
            tier = partner._get_matching_vip_tier(partner.company_id or self.env.company, total_amount)
            partner._apply_vip_result(tier, total_amount)

    @api.model
    def _cron_recompute_vip_tier(self):
        partners = self.with_context(active_test=False).search([("parent_id", "=", False)])
        partners._recompute_vip_tier_for_commercial_partners()

    def action_recompute_vip_tier(self):
        self._recompute_vip_tier_for_commercial_partners()
        return True
