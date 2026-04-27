/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { markup } from "@odoo/owl";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";

patch(PaymentScreen.prototype, {
    async addNewPaymentLine(paymentMethod) {
        const isAdded = await super.addNewPaymentLine(...arguments);
        if (!isAdded || !paymentMethod?.manual_bank_qr_enabled) {
            return isAdded;
        }

        const paymentLine = this.paymentLines.at(-1);
        const amount = paymentLine?.amount || this.currentOrder.remainingDue || 0;
        try {
            const payload = await this.pos.data.call("pos.payment.method", "get_manual_qr_payload", [
                paymentMethod.id,
                amount,
                this.currentOrder.name,
            ]);
            const body = markup(`
                <div>
                    <p>${_t("Scan QR to transfer with exact amount.")}</p>
                    <p><strong>${_t("Receiver")}:</strong> ${payload.account_name}</p>
                    <p><strong>${_t("Account")}:</strong> ${payload.account_number}</p>
                    <p><strong>${_t("Amount")}:</strong> ${payload.amount}</p>
                    <p><strong>${_t("Reference")}:</strong> ${payload.reference}</p>
                    <img src="${payload.image_url}" alt="bank-qr" style="max-width: 260px; width: 100%; border: 1px solid #ddd; border-radius: 8px;"/>
                </div>
            `);
            this.dialog.add(AlertDialog, {
                title: _t("Bank Transfer QR"),
                body,
            });
        } catch (error) {
            this.notification.add(error?.message || _t("Cannot generate transfer QR."), {
                type: "warning",
            });
        }
        return isAdded;
    },
});
