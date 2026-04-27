/** @odoo-module **/

import { registry } from "@web/core/registry";
import { _t } from "@web/core/l10n/translation";

const barcodeGuardService = {
    dependencies: ["orm", "action", "notification"],
    start(env, { orm, action, notification }) {
        let buffer = "";
        let lastKeyTs = 0;
        let isProcessing = false;

        const resetBuffer = () => {
            buffer = "";
            lastKeyTs = 0;
        };

        const getCurrentStockPickingContext = () => {
            const controller = action.currentController;
            const resModel = controller?.props?.resModel || controller?.action?.res_model;
            const resId = controller?.props?.resId || controller?.state?.resId || controller?.action?.res_id;
            return {
                resModel,
                resId: Number.isInteger(resId) ? resId : false,
            };
        };

        const isEditableTarget = (target) => {
            if (!target) {
                return false;
            }
            const tagName = target.tagName?.toLowerCase();
            return (
                target.isContentEditable ||
                tagName === "input" ||
                tagName === "textarea" ||
                tagName === "select"
            );
        };

        const isSearchInputTarget = (target) => {
            if (!target || !target.closest) {
                return false;
            }
            return Boolean(
                target.closest(".o_searchview") ||
                    target.closest(".o_control_panel .o_input")
            );
        };

        const clearInputValue = (target) => {
            if (!target || typeof target.value === "undefined") {
                return;
            }
            target.value = "";
            target.dispatchEvent(new Event("input", { bubbles: true }));
        };

        const openReceiptForm = async (receiptId) => {
            await action.doAction({
                type: "ir.actions.act_window",
                res_model: "stock.picking",
                res_id: receiptId,
                views: [[false, "form"]],
                target: "current",
            });
        };

        const processBarcode = async (scannedBarcode) => {
            if (isProcessing) {
                return;
            }
            const { resModel, resId } = getCurrentStockPickingContext();
            if (resModel !== "stock.picking") {
                return;
            }
            isProcessing = true;
            try {
                const result = await orm.call("stock.picking", "scan_receipt_barcode", [
                    scannedBarcode,
                    resId || false,
                ]);
                if (!result) {
                    return;
                }

                if (result.status === "ok") {
                    if (!resId || result.receipt_id !== resId) {
                        await openReceiptForm(result.receipt_id);
                    }
                    notification.add(
                        _t(
                            "Scanned %(product)s and matched receipt %(receipt)s.",
                            {
                                product: result.product_display_name,
                                receipt: result.receipt_name,
                            }
                        ),
                        { type: "success" }
                    );
                    return;
                }

                if (result.status === "multiple_receipts") {
                    const suggestions = (result.receipt_suggestions || [])
                        .map((line) => line.name)
                        .join(", ");
                    notification.add(
                        _t(
                            "Barcode %(barcode)s (%(product)s) belongs to multiple receipts: %(receipts)s. Open the target receipt and scan again.",
                            {
                                barcode: result.barcode,
                                product: result.product_display_name,
                                receipts: suggestions || _t("N/A"),
                            }
                        ),
                        { type: "warning" }
                    );
                    return;
                }

                if (result.status === "not_in_open_receipts") {
                    notification.add(
                        _t(
                            "Barcode %(barcode)s (%(product)s) is not found in open incoming receipts.",
                            {
                                barcode: result.barcode,
                                product: result.product_display_name,
                            }
                        ),
                        { type: "warning" }
                    );
                    return;
                }

                if (result.status === "product_not_found") {
                    notification.add(
                        _t("Barcode %(barcode)s is not linked to any product.", {
                            barcode: result.barcode,
                        }),
                        { type: "warning" }
                    );
                    return;
                }

                notification.add(_t("Barcode scan could not be processed."), { type: "warning" });
            } finally {
                isProcessing = false;
            }
        };

        window.addEventListener(
            "keydown",
            (ev) => {
                const { resModel } = getCurrentStockPickingContext();
                const isPickingContext = resModel === "stock.picking";
                const allowBarcodeCaptureInInput =
                    isPickingContext && isSearchInputTarget(ev.target);

                if (isEditableTarget(ev.target) && !allowBarcodeCaptureInInput) {
                    resetBuffer();
                    return;
                }
                if (ev.ctrlKey || ev.altKey || ev.metaKey) {
                    return;
                }
                const now = Date.now();
                if (lastKeyTs && now - lastKeyTs > 120) {
                    resetBuffer();
                }

                if (ev.key === "Enter") {
                    const scanned = buffer.trim();
                    resetBuffer();
                    if (scanned.length >= 4) {
                        ev.preventDefault();
                        ev.stopPropagation();
                        if (allowBarcodeCaptureInInput) {
                            clearInputValue(ev.target);
                            ev.target.blur();
                        }
                        processBarcode(scanned);
                    }
                    return;
                }

                if (ev.key.length === 1) {
                    if (allowBarcodeCaptureInInput) {
                        ev.preventDefault();
                        ev.stopPropagation();
                    }
                    buffer += ev.key;
                    lastKeyTs = now;
                }
            },
            true
        );
    },
};

registry.category("services").add("stock_receipt_barcode_guard", barcodeGuardService);
