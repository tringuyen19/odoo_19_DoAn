/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { PosStore } from "@point_of_sale/app/services/pos_store";

patch(PosStore.prototype, {
    _buildQuotationPayloadFromCurrentOrder() {
        const order = this.getOrder();
        const partner = order?.getPartner();
        const lines = (order?.getOrderlines() || [])
            .filter((line) => line.getQuantity() > 0)
            .map((line) => ({
                product_id: line.product_id.id,
                qty: line.getQuantity(),
            }));
        return {
            partner_id: partner?.id,
            origin: order?.name || order?.uuid,
            lines,
        };
    },

    async _getInsufficientStockInfoBeforePayment() {
        const order = this.getOrder();
        const quantityByProduct = new Map();
        for (const line of order?.getOrderlines() || []) {
            const product = line.product_id;
            const quantity = line.getQuantity();
            if (!product?.is_storable || quantity <= 0) {
                continue;
            }
            quantityByProduct.set(product, (quantityByProduct.get(product) || 0) + quantity);
        }

        for (const [product, qty] of quantityByProduct.entries()) {
            let result;
            try {
                result = await this.getProductInfo(product.product_tmpl_id, qty, 0, product);
            } catch {
                continue;
            }
            const freeQty = result?.productInfo?.warehouses?.[0]?.free_qty;
            if (typeof freeQty === "number" && freeQty < qty) {
                return { product, qty, freeQty };
            }
        }
        return null;
    },

    async pay() {
        const stockIssue = await this._getInsufficientStockInfoBeforePayment();
        if (stockIssue) {
            this.dialog.add(ConfirmationDialog, {
                title: _t("Insufficient Stock"),
                body: _t(
                    "Product %(product)s has only %(free)s free to use, while this order needs %(need)s.\n\nYou can create a draft quotation for this customer.",
                    {
                        product: stockIssue.product.display_name || "",
                        free: stockIssue.freeQty,
                        need: stockIssue.qty,
                    }
                ),
                confirmLabel: _t("Create Draft Quotation"),
                cancelLabel: _t("Close"),
                confirm: async () => {
                    const payload = this._buildQuotationPayloadFromCurrentOrder();
                    if (!payload.partner_id) {
                        this.notification.add(_t("Please select a customer first."), {
                            type: "warning",
                        });
                        return;
                    }
                    const result = await this.data.call(
                        "pos.order",
                        "create_draft_quotation_from_pos",
                        [payload]
                    );
                    if (result?.sale_order_id) {
                        window.open(`/odoo/sale.order/${result.sale_order_id}`, "_blank");
                        this.notification.add(
                            _t("Draft quotation %(name)s has been created.", {
                                name: result.sale_order_name,
                            }),
                            { type: "success" }
                        );
                    }
                },
            });
            return;
        }

        return await super.pay(...arguments);
    },
});
