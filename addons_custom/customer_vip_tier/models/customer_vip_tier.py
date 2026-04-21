from odoo import fields, models


class CustomerVipTier(models.Model):
    _name = "customer.vip.tier"
    _description = "Customer VIP Tier"
    _order = "min_amount desc, id asc"

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    min_amount = fields.Monetary(required=True, default=0.0)
    currency_id = fields.Many2one(
        "res.currency",
        required=True,
        default=lambda self: self.env.company.currency_id.id,
    )
    company_id = fields.Many2one(
        "res.company",
        default=lambda self: self.env.company.id,
        index=True,
    )
    pricelist_id = fields.Many2one(
        "product.pricelist",
        required=True,
        domain="[('company_id', 'in', (False, company_id))]",
    )
    note = fields.Text()
