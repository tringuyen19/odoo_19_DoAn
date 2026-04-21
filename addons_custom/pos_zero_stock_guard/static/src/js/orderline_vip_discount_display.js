/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { formatCurrency } from "@web/core/currency";
import { Orderline } from "@point_of_sale/app/components/orderline/orderline";

function formatPercent(value) {
    const rounded = Math.round(value * 100) / 100;
    return Number.isInteger(rounded)
        ? `${rounded}`
        : `${rounded.toFixed(2).replace(/0+$/, "").replace(/\.$/, "")}`;
}

function getDisplayAmountFromUnitPrice(line, unitPrice) {
    const config = line.config;
    const qty = line.getQuantity();
    const orderSign = line.order_id?.orderSign || 1;
    const taxDetails = line.product_id.getTaxDetails({
        overridedValues: {
            price: unitPrice,
            fiscalPosition: line.order_id?.fiscal_position_id || false,
        },
    });
    const unitDisplayAmount =
        config.iface_tax_included === "total"
            ? taxDetails.total_included
            : taxDetails.total_excluded;
    return line.currency.round(unitDisplayAmount * qty * orderSign);
}

patch(Orderline.prototype, {
    get lineScreenValues() {
        const vals = super.lineScreenValues;
        if (!this.line?.order_id || !vals) {
            return vals;
        }

        const isDisplay = this.props.mode === "display" && !this.props.basic_receipt;
        const finalPrice = this.line.displayPrice;
        const manualDiscount = this.line.getDiscount();
        const baseUnitPrice = this.line.product_id.getPrice(
            false,
            1,
            this.line.getPriceExtra(),
            false,
            this.line.product_id
        );
        const baseDisplayPrice = getDisplayAmountFromUnitPrice(this.line, baseUnitPrice);
        const hasPricelistDiscount =
            isDisplay &&
            !this.line.combo_parent_id &&
            !manualDiscount &&
            typeof baseDisplayPrice === "number" &&
            typeof finalPrice === "number" &&
            baseDisplayPrice > finalPrice;

        if (!hasPricelistDiscount) {
            return {
                ...vals,
                vipDiscountLabel: null,
                vipBasePrice: null,
                vipDiscountAmount: null,
                vipFinalPrice: null,
            };
        }

        const discountAmount = baseDisplayPrice - finalPrice;
        const discountPct = (discountAmount / baseDisplayPrice) * 100;
        return {
            ...vals,
            vipDiscountLabel: formatPercent(discountPct),
            vipBasePrice: formatCurrency(baseDisplayPrice, this.line.currency.id),
            vipDiscountAmount: formatCurrency(discountAmount, this.line.currency.id),
            vipFinalPrice: formatCurrency(finalPrice, this.line.currency.id),
        };
    },
});
