/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { ProductConfiguratorPopup } from "@point_of_sale/app/components/popups/product_configurator_popup/product_configurator_popup";

patch(ProductConfiguratorPopup.prototype, {
    async confirm() {
        const productTemplate = this.props.productTemplate;
        if (productTemplate?.is_storable) {
            let result;
            try {
                result = await this.pos.getProductInfo(productTemplate, 1, 0, this.product);
            } catch {
                result = null;
            }
            const freeQty = result?.productInfo?.warehouses?.[0]?.free_qty;
            if (typeof freeQty === "number" && freeQty <= 0) {
                this.pos.notification.add(
                    _t("Cannot add product because Free To Use quantity is 0."),
                    { type: "warning" }
                );
                return;
            }
        }

        this.props.getPayload(this.computePayload());
        this.props.close();
    },
});
