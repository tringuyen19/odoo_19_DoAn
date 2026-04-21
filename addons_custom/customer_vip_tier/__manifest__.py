{
    "name": "Customer VIP Tier",
    "summary": "Auto classify customers and assign VIP pricelists",
    "version": "19.0.1.0.0",
    "category": "Sales",
    "author": "Custom",
    "license": "LGPL-3",
    "depends": ["base", "contacts", "product", "sale"],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_cron.xml",
        "views/customer_vip_tier_views.xml",
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "application": False,
}
