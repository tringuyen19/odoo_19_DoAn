/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { PosStore } from "@point_of_sale/app/services/pos_store";

patch(PosStore.prototype, {
    _buildQuotationPayloadFromCurrentOrder(shortageLines) {
        const order = this.getOrder();
        const partner = order?.getPartner();
        return {
            partner_id: partner?.id,
            origin: order?.name || order?.uuid,
            lines: shortageLines || [],
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

        const shortageLines = [];
        const availableQtyByProductId = new Map();
        for (const [product, qty] of quantityByProduct.entries()) {
            let result;
            try {
                result = await this.getProductInfo(product.product_tmpl_id, qty, 0, product);
            } catch {
                continue;
            }
            const freeQty = result?.productInfo?.warehouses?.[0]?.free_qty;
            if (typeof freeQty !== "number") {
                continue;
            }
            const availableQty = Math.max(0, Math.min(qty, freeQty));
            const shortageQty = qty - availableQty;
            if (shortageQty > 0) {
                shortageLines.push({
                    product_id: product.id,
                    qty: shortageQty,
                    product_name: product.display_name || "",
                    available_qty: availableQty,
                    requested_qty: qty,
                });
                availableQtyByProductId.set(product.id, availableQty);
            }
        }
        return shortageLines.length ? { shortageLines, availableQtyByProductId } : null;
    },

    _applyAvailableQtyToCurrentOrder(availableQtyByProductId) {
        const order = this.getOrder();
        const orderLines = order?.getOrderlines() || [];
        const remainingQtyByProductId = new Map(availableQtyByProductId);
        for (const line of orderLines) {
            const product = line.product_id;
            const currentQty = line.getQuantity();
            if (!product?.is_storable || currentQty <= 0) {
                continue;
            }
            if (!remainingQtyByProductId.has(product.id)) {
                continue;
            }
            const remainingQty = remainingQtyByProductId.get(product.id) || 0;
            const keepQty = Math.min(currentQty, remainingQty);
            if (keepQty > 0) {
                line.setQuantity(keepQty);
            } else {
                order.removeOrderline(line);
            }
            remainingQtyByProductId.set(product.id, Math.max(0, remainingQty - keepQty));
        }
    },

    async pay() {
        const stockIssue = await this._getInsufficientStockInfoBeforePayment();
        if (stockIssue) {
            const totalShortageQty = stockIssue.shortageLines.reduce(
                (sum, line) => sum + line.qty,
                0
            );
            this.dialog.add(ConfirmationDialog, {
                title: _t("Insufficient Stock"),
                body: _t(
                    "Some products do not have enough stock. %(qty)s item(s) will be moved to a draft quotation, and available quantities will stay in POS for payment.",
                    {
                        qty: totalShortageQty,
                    }
                ),
                confirmLabel: _t("Create Draft Quotation"),
                cancelLabel: _t("Close"),
                confirm: async () => {
                    const payload = this._buildQuotationPayloadFromCurrentOrder(
                        stockIssue.shortageLines.map((line) => ({
                            product_id: line.product_id,
                            qty: line.qty,
                        }))
                    );
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
                        this._applyAvailableQtyToCurrentOrder(stockIssue.availableQtyByProductId);
                        window.open(`/odoo/sale.order/${result.sale_order_id}`, "_blank");
                        this.notification.add(
                            _t(
                                "Draft quotation %(name)s has been created. Available quantities remain in POS for payment.",
                                {
                                    name: result.sale_order_name,
                                }
                            ),
                            { type: "success" }
                        );
                        await this.pay();
                    } else {
                        this.notification.add(
                            _t("Could not create draft quotation for insufficient quantities."),
                            {
                                type: "danger",
                            }
                        );
                    }
                },
            });
            return;
        }

        return await super.pay(...arguments);
    },
});
