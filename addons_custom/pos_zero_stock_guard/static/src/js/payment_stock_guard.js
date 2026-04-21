/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import OrderPaymentValidation from "@point_of_sale/app/utils/order_payment_validation";

patch(OrderPaymentValidation.prototype, {
    _buildQuotationPayload(shortageLines) {
        const partner = this.order.getPartner();
        return {
            partner_id: partner?.id,
            origin: this.order.name || this.order.uuid,
            lines: shortageLines || [],
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

        const shortageLines = [];
        const availableQtyByProductId = new Map();
        for (const [product, qty] of quantityByProduct.entries()) {
            let result;
            try {
                result = await this.pos.getProductInfo(product.product_tmpl_id, qty, 0, product);
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
                    available_qty: availableQty,
                    requested_qty: qty,
                });
                availableQtyByProductId.set(product.id, availableQty);
            }
        }
        return shortageLines.length ? { shortageLines, availableQtyByProductId } : null;
    },

    _applyAvailableQtyToCurrentOrder(availableQtyByProductId) {
        const remainingQtyByProductId = new Map(availableQtyByProductId);
        for (const line of this.order.getOrderlines()) {
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
                this.order.removeOrderline(line);
            }
            remainingQtyByProductId.set(product.id, Math.max(0, remainingQty - keepQty));
        }
    },

    async isOrderValid(isForceValidate) {
        const stockIssue = await this._getInsufficientStockInfo();
        if (stockIssue) {
            const totalShortageQty = stockIssue.shortageLines.reduce(
                (sum, line) => sum + line.qty,
                0
            );
            this.pos.dialog.add(ConfirmationDialog, {
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
                    const payload = this._buildQuotationPayload(
                        stockIssue.shortageLines.map((line) => ({
                            product_id: line.product_id,
                            qty: line.qty,
                        }))
                    );
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
                        this._applyAvailableQtyToCurrentOrder(stockIssue.availableQtyByProductId);
                        window.open(`/odoo/sale.order/${result.sale_order_id}`, "_blank");
                        this.pos.notification.add(
                            _t(
                                "Draft quotation %(name)s has been created. Available quantities remain in POS for payment.",
                                { name: result.sale_order_name }
                            ),
                            { type: "success" }
                        );
                    } else {
                        this.pos.notification.add(
                            _t("Could not create draft quotation for insufficient quantities."),
                            { type: "danger" }
                        );
                    }
                },
            });
            return false;
        }

        return await super.isOrderValid(isForceValidate);
    },
});
