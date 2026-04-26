/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/services/pos_store";
import { getOnNotified } from "@point_of_sale/utils";

patch(PosStore.prototype, {
    async setup() {
        await super.setup(...arguments);
        this._registerMobileBarcodeChannel();
    },

    _registerMobileBarcodeChannel() {
        if (!this.config?.mobile_barcode_enabled || !this.config?.id) {
            return;
        }
        const channel = `pos_mobile_barcode.${this.config.id}`;
        getOnNotified(this.bus, channel)("mobile_barcode_scanned", async (payload) => {
            const barcode = (payload?.barcode || "").trim();
            if (!barcode) {
                return;
            }
            await this.barcodeReader.scan(barcode);
        });
    },

    getMobileBarcodeScannerUrl() {
        if (!this.config?.id || !this.config?.mobile_barcode_token) {
            return "";
        }
        return `${window.location.origin}/pos/mobile_scanner/${this.config.id}/${this.config.mobile_barcode_token}`;
    },
});
