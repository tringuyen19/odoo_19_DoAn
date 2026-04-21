/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import OrderPaymentValidation from "@point_of_sale/app/utils/order_payment_validation";

patch(OrderPaymentValidation.prototype, {
    _buildQuotationPayload() {
        const partner = this.order.getPartner();
        const lines = this.order
            .getOrderlines()
            .filter((line) => line.getQuantity() > 0)
            .map((line) => ({
                product_id: line.product_id.id,
                qty: line.getQuantity(),
            }));
        return {
            partner_id: partner?.id,
            origin: this.order.name || this.order.uuid,
            lines,
        };
    },

    async _getInsufficientStockInfo() {
        const quantityByProduct = new Map();
        for (const line of this.order.getOrderlines()) {
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
                result = await this.pos.getProductInfo(product.product_tmpl_id, qty, 0, product);
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

    async isOrderValid(isForceValidate) {
        const stockIssue = await this._getInsufficientStockInfo();
        if (stockIssue) {
            this.pos.dialog.add(ConfirmationDialog, {
                title: _t("Insufficient Stock"),
                body: _t(
                    "Product %(product)s has only %(free)s free to use, while this order needs %(need)s.\n\nYou can switch to Sales and create a quotation/backorder for this customer.",
                    {
                        product: stockIssue.product.display_name || "",
                        free: stockIssue.freeQty,
                        need: stockIssue.qty,
                    }
                ),
                confirmLabel: _t("Create Draft Quotation"),
                cancelLabel: _t("Close"),
                confirm: async () => {
                    const payload = this._buildQuotationPayload();
                    if (!payload.partner_id) {
                        this.pos.notification.add(_t("Please select a customer first."), {
                            type: "warning",
                        });
                        return;
                    }
                    const result = await this.pos.data.call(
                        "pos.order",
                        "create_draft_quotation_from_pos",
                        [payload]
                    );
                    if (result?.sale_order_id) {
                        window.open(`/odoo/sale.order/${result.sale_order_id}`, "_blank");
                        this.pos.notification.add(
                            _t("Draft quotation %(name)s has been created.", {
                                name: result.sale_order_name,
                            }),
                            { type: "success" }
                        );
                    }
                },
            });
            return false;
        }

        return await super.isOrderValid(isForceValidate);
    },
});
