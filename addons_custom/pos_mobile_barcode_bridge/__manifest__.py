{
    "name": "POS Mobile Barcode Bridge",
    "summary": "Scan POS barcodes from a phone camera",
    "version": "19.0.1.0.0",
    "category": "Point of Sale",
    "author": "Custom",
    "license": "LGPL-3",
    "depends": ["point_of_sale", "barcodes", "bus"],
    "data": [
        "views/pos_config_views.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_mobile_barcode_bridge/static/src/js/pos_mobile_barcode_listener.js",
            "pos_mobile_barcode_bridge/static/src/js/control_buttons_mobile_scanner.js",
            "pos_mobile_barcode_bridge/static/src/xml/control_buttons_mobile_scanner.xml",
        ],
    },
    "installable": True,
    "application": False,
}
