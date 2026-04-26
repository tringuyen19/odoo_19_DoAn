/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(ControlButtons.prototype, {
    async clickMobileScanner() {
        const url = this.pos.getMobileBarcodeScannerUrl();
        if (!url) {
            this.notification.add(_t("Mobile scanner URL is unavailable."), {
                type: "warning",
            });
            return;
        }
        try {
            await navigator.clipboard.writeText(url);
            this.notification.add(_t("Scanner URL copied. Open it on your phone."), {
                type: "success",
            });
        } catch {
            // Ignore clipboard errors and still show URL dialog.
        }
        this.dialog.add(AlertDialog, {
            title: _t("Mobile Scanner URL"),
            body: `${_t("Open this URL on your phone:")} ${url}`,
        });
    },
});
