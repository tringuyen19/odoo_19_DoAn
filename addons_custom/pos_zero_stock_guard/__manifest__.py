{
    "name": "POS Zero Stock Guard",
    "summary": "Prevent adding out-of-stock variant in POS configurator",
    "version": "19.0.1.0.0",
    "category": "Point of Sale",
    "author": "Custom",
    "license": "LGPL-3",
    "depends": ["point_of_sale", "sale"],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_zero_stock_guard/static/src/js/product_configurator_guard.js",
            "pos_zero_stock_guard/static/src/js/payment_entry_guard.js",
            "pos_zero_stock_guard/static/src/js/orderline_vip_discount_display.js",
            "pos_zero_stock_guard/static/src/xml/partner_pricelist_badge.xml",
            "pos_zero_stock_guard/static/src/xml/orderline_vip_discount_display.xml",
        ],
    },
    "installable": True,
    "application": False,
}
