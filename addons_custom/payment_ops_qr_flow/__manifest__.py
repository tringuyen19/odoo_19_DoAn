{
    "name": "Payment Ops QR Flow",
    "summary": "POS bank QR and SO transfer/COD flow without accounting dependency",
    "version": "19.0.1.0.0",
    "category": "Sales/Point of Sale",
    "author": "Custom",
    "license": "LGPL-3",
    "depends": ["point_of_sale", "sale", "base_setup"],
    "data": [
        "views/pos_payment_method_views.xml",
        "views/res_config_settings_views.xml",
        "views/sale_order_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "payment_ops_qr_flow/static/src/js/payment_screen_bank_qr.js",
        ],
    },
    "installable": True,
    "application": False,
}
