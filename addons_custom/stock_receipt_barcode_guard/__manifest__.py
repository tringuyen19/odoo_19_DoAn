{
    "name": "Stock Receipt Barcode Guard",
    "summary": "Scan barcode to jump receipt and increment done qty",
    "version": "19.0.1.0.0",
    "category": "Inventory/Inventory",
    "author": "Custom",
    "license": "LGPL-3",
    "depends": ["stock", "web"],
    "assets": {
        "web.assets_backend": [
            "stock_receipt_barcode_guard/static/src/js/receipt_barcode_service.js",
        ],
    },
    "installable": True,
    "application": False,
}
