from odoo import http
from odoo.http import request


class PosMobileBarcodeController(http.Controller):
    @http.route(
        "/pos/mobile_scanner/<int:config_id>/<string:token>",
        type="http",
        auth="public",
        website=True,
    )
    def mobile_scanner_page(self, config_id, token, **kwargs):
        config = request.env["pos.config"].sudo().browse(config_id).exists()
        if not config:
            return request.not_found()
        if not config.mobile_barcode_enabled or config.mobile_barcode_token != token:
            return request.not_found()

        return request.render(
            "pos_mobile_barcode_bridge.mobile_scanner_page",
            {
                "config_id": config.id,
                "token": token,
                "config_name": config.name,
            },
        )

    @http.route(
        "/pos/mobile_scanner/push",
        type="json",
        auth="public",
        csrf=False,
    )
    def mobile_scanner_push(self, config_id, token, barcode):
        barcode = (barcode or "").strip()
        if not barcode:
            return {"ok": False, "error": "empty_barcode"}

        config = request.env["pos.config"].sudo().browse(int(config_id)).exists()
        if not config:
            return {"ok": False, "error": "config_not_found"}

        if not config.mobile_barcode_enabled or config.mobile_barcode_token != token:
            return {"ok": False, "error": "invalid_token"}

        channel = f"pos_mobile_barcode.{config.id}"
        request.env["bus.bus"].sudo()._sendone(
            channel,
            f"{channel}-mobile_barcode_scanned",
            {"barcode": barcode},
        )
        return {"ok": True}
