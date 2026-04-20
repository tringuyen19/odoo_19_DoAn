# HƯỚNG DẪN TRIỂN KHAI CHI TIẾT THEO TỪNG TUẦN (12-16 TUẦN)

Tài liệu này chi tiết hóa kế hoạch tại mục `7) Kế hoạch thời gian tham chiếu (12-16 tuần)` trong tài liệu chính.

Nguyên tắc triển khai:

- Làm chuẩn Odoo trước, custom sau.
- Mỗi tuần đều có đầu ra rõ ràng và tiêu chí pass/fail.
- Không mở rộng phạm vi khi tuần hiện tại chưa đạt điều kiện nghiệm thu.

---

## 1) Cách dùng tài liệu này

Mỗi tuần đều có 6 phần:

1. Mục tiêu tuần
2. Công việc chi tiết theo ngày
3. Cấu hình/module cần làm
4. Deliverable bắt buộc
5. Checklist nghiệm thu cuối tuần
6. Rủi ro và phương án xử lý

---

## 2) Tuần 1-2: Blueprint + Môi trường + Chuẩn dữ liệu

## Tuần 1 - Chốt blueprint nghiệp vụ và phạm vi

### Mục tiêu tuần

- Chốt quy trình TO-BE theo kênh online/offline.
- Chốt phạm vi Go-live phase chuẩn.
- Lập backlog phân loại standard/custom.

### Kế hoạch theo ngày

- Ngày 1:
  - Kickoff với Sales, Kho, Kế toán, Quản lý.
  - Thống nhất mục tiêu KPI Go-live.
- Ngày 2:
  - Workshop quy trình: tiếp nhận khách -> đơn hàng -> kho -> thanh toán -> hóa đơn.
  - Chốt nhánh online/offline riêng.
- Ngày 3:
  - Mapping TO-BE sang module Odoo chuẩn.
  - Đánh dấu điểm cần custom.
- Ngày 4:
  - Lập Fit/Gap Matrix (AS-IS / TO-BE / Standard / Custom).
  - Ưu tiên backlog theo mức độ ảnh hưởng.
- Ngày 5:
  - Review và ký xác nhận phạm vi phase 1.

### Deliverable bắt buộc

- Blueprint nghiệp vụ (đã ký).
- Fit/Gap Matrix.
- Backlog chuẩn + custom có ưu tiên.

### Checklist nghiệm thu cuối tuần

- [ ] Tất cả bộ phận xác nhận quy trình chung.
- [ ] Không còn mơ hồ giữa luồng online và offline.
- [ ] Có danh sách rõ: "làm chuẩn trước" và "custom sau".

### Rủi ro và xử lý

- Rủi ro: các phòng ban hiểu khác nhau về trạng thái đơn.
- Xử lý: chuẩn hóa từ điển trạng thái ngay tuần 1.

---

## Tuần 2 - Dựng môi trường và chuẩn dữ liệu import

### Mục tiêu tuần

- Sẵn sàng Dev/UAT/Prod.
- Chuẩn hóa dữ liệu master để import.

### Kế hoạch theo ngày

- Ngày 1:
  - Dựng môi trường Dev, UAT.
  - Thiết lập backup tự động.
- Ngày 2:
  - Cấu hình user, group nền tảng.
  - Thiết lập quy tắc naming SKU/mã khách/mã đơn.
- Ngày 3:
  - Chuẩn hóa file sản phẩm: SKU, category, UoM, giá.
  - Chuẩn hóa khách hàng: tên, sđt, email, địa chỉ.
- Ngày 4:
  - Chuẩn hóa dữ liệu kho: warehouse, location, tồn đầu kỳ.
  - Chuẩn hóa kế toán: taxes, payment terms, journals.
- Ngày 5:
  - Import thử trên UAT và sửa lỗi dữ liệu.

### Deliverable bắt buộc

- Môi trường Dev/UAT chạy ổn định.
- Bộ file import sạch.
- Biên bản kiểm tra import.

### Checklist nghiệm thu cuối tuần

- [ ] Import sản phẩm/khách hàng thành công > 95%.
- [ ] Không trùng SKU.
- [ ] Dữ liệu bắt buộc không còn thiếu.

---

## 3) Tuần 3-6: CRM + Sales + Inventory Core

## Tuần 3 - CRM và tiếp nhận khách theo kênh

### Mục tiêu tuần

- Vận hành được quy trình tiếp nhận khách online/offline.
- CRM có pipeline, nguồn khách, và hoạt động follow-up.

### Công việc cụ thể

- Cài module: `crm`, `contacts`.
- Cấu hình stages: New -> Qualified -> Proposal -> Won/Lost.
- Cấu hình Lead Source: Website, Facebook, Zalo, Walk-in, Referral.
- Cấu hình Sales Team: Online Team, Showroom Team.
- Tạo activity template: gọi lại, gửi báo giá, nhắc lịch hẹn.

### Deliverable bắt buộc

- Pipeline CRM chạy được.
- Mẫu lead theo từng kênh.
- Dashboard cơ bản theo source.

### Checklist nghiệm thu

- [ ] Tạo lead theo 5 nguồn khác nhau thành công.
- [ ] Chuyển stage không lỗi.
- [ ] Có thể convert lead sang báo giá.

---

## Tuần 4 - Sales: báo giá, xác nhận đơn, quy tắc đơn hàng

### Mục tiêu tuần

- Sales tạo báo giá, chốt đơn, sinh luồng kho tự động.

### Công việc cụ thể

- Cài/cấu hình: `sale`, `sale_management`, `sale_stock`.
- Cấu hình pricelist, payment terms, sales team.
- Tạo field nghiệp vụ:
  - Kênh bán
  - Nguồn đơn
  - Ngày giao dự kiến
  - Ghi chú phối hợp kho
- Test luồng:
  - Quotation -> Confirm SO -> tạo Delivery.

### Deliverable bắt buộc

- Bộ cấu hình Sales chuẩn.
- Mẫu SO cho online/offline.
- SOP thao tác cho Sales user.

### Checklist nghiệm thu

- [ ] Confirm SO tự sinh chứng từ kho.
- [ ] Đơn online/offline đều có metadata đúng.
- [ ] Báo giá -> đơn hàng không lỗi quyền.

---

## Tuần 5 - Inventory: kho, vị trí, xuất nhập và barcode

### Mục tiêu tuần

- Kho vận hành được theo vị trí, xử lý pick/pack/ship.

### Công việc cụ thể

- Cài/cấu hình: `stock`, `stock_barcode`.
- Cấu hình warehouse/location phân cấp.
- Cấu hình operation types: Receipt/Delivery/Internal Transfer.
- Cấu hình barcode sản phẩm và vị trí.
- Thiết lập inventory adjustment và cycle count.

### Deliverable bắt buộc

- Cấu trúc kho hoàn chỉnh.
- Mẫu phiếu kho chuẩn.
- SOP kho: nhận đơn, nhặt hàng, xuất hàng, kiểm kho.

### Checklist nghiệm thu

- [ ] Delivery validate thành công.
- [ ] Tồn kho giảm đúng sau xuất kho.
- [ ] Quét barcode chạy được trên thiết bị thực tế.

---

## Tuần 6 - Liên thông CRM-Sales-Inventory và hardening

### Mục tiêu tuần

- Chạy luồng end-to-end từ lead đến giao hàng hoàn chỉnh.

### Công việc cụ thể

- Test liên thông:
  - Lead -> Quotation -> SO -> Delivery -> Done.
- Rà lỗi dữ liệu, quyền, hiệu năng thao tác.
- Chuẩn hóa dashboard vận hành cho Sales/Kho.
- Khóa danh mục master data version 1.

### Deliverable bắt buộc

- Biên bản test E2E core (CRM-Sales-Stock).
- Danh sách lỗi + trạng thái xử lý.

### Checklist nghiệm thu

- [ ] E2E pass cho ít nhất 3 kịch bản.
- [ ] Không sai lệch tồn kho sau giao hàng.
- [ ] User nghiệp vụ thao tác độc lập theo SOP.

---

## 4) Tuần 7-8: Purchase + Accounting Core

## Tuần 7 - Purchase và reordering tự động

### Mục tiêu tuần

- Tự động đề xuất/khởi tạo mua hàng khi tồn xuống thấp.

### Công việc cụ thể

- Cài/cấu hình: `purchase`, `purchase_stock`.
- Khai báo vendor và vendor pricelist.
- Cấu hình lead time theo sản phẩm.
- Thiết lập reordering rules min/max.
- Test scheduler tạo RFQ/PO.

### Deliverable bắt buộc

- Danh mục vendor chuẩn.
- Bộ rule min/max cho nhóm hàng chính.
- SOP mua hàng bổ sung.

### Checklist nghiệm thu

- [ ] Tồn < min kích hoạt đúng cơ chế mua bù.
- [ ] Vendor, giá, lead time ra đúng trên RFQ/PO.

---

## Tuần 8 - Accounting: invoice, payment, reconciliation

### Mục tiêu tuần

- Hoàn chỉnh chuỗi kế toán từ đơn hàng đến thu tiền.

### Công việc cụ thể

- Cài/cấu hình: `account`, `account_accountant`.
- Cấu hình taxes, journals, payment terms.
- Cấu hình payment method offline (cash/bank/COD).
- Test luồng:
  - SO -> Invoice -> Post -> Register Payment -> Reconcile.
- Bật báo cáo công nợ tuổi nợ (Aged Receivable).

### Deliverable bắt buộc

- Cấu hình kế toán base hoàn chỉnh.
- SOP cho kế toán bán hàng và thu tiền.

### Checklist nghiệm thu

- [ ] Invoice tạo từ SO đúng giá, đúng thuế.
- [ ] Ghi nhận thanh toán và đối soát thành công.
- [ ] Báo cáo công nợ ra đúng số liệu mẫu.

---

## 5) Tuần 9-10: Website/POS + Phân quyền + Báo cáo

## Tuần 9 - Kênh bán website/POS và đồng bộ tồn kho

### Mục tiêu tuần

- Đảm bảo đa kênh dùng chung tồn kho, không oversell.

### Công việc cụ thể

- Cài/cấu hình `website_sale`, `website_sale_stock` (nếu dùng web).
- Cài/cấu hình `point_of_sale` (nếu dùng POS).
- Cấu hình stock policy hiển thị tồn.
- Test bán đồng thời nhiều kênh.

### Deliverable bắt buộc

- SOP vận hành đơn website.
- SOP vận hành đơn tại quầy POS.

### Checklist nghiệm thu

- [ ] Website hết hàng thì chặn checkout đúng.
- [ ] POS bán hàng trừ đúng kho dùng chung.

---

## Tuần 10 - Phân quyền và dashboard quản trị

### Mục tiêu tuần

- Hoàn tất bảo mật theo vai trò và dashboard vận hành.

### Công việc cụ thể

- Cấu hình groups/users:
  - Sales User/Manager
  - Inventory User/Manager
  - Accountant/Manager
- Rà record rules quan trọng theo team/kho.
- Cấu hình dashboard:
  - Sales KPI
  - Stock level/low stock
  - Aged receivable

### Deliverable bắt buộc

- Ma trận phân quyền phiên bản 1.
- Dashboard quản trị theo vai trò.

### Checklist nghiệm thu

- [ ] Đúng người đúng quyền.
- [ ] Không truy cập trái phạm vi dữ liệu.
- [ ] Quản lý xem KPI được theo ngày/tuần.

---

## 6) Tuần 11-12: UAT + Đào tạo + Go-live

## Tuần 11 - UAT toàn diện

### Mục tiêu tuần

- Kiểm thử và ký nghiệm thu nghiệp vụ chuẩn.

### Công việc cụ thể

- Chạy test case chuẩn:
  1. Đơn đủ hàng - thanh toán offline
  2. Đơn online - thanh toán online (mock nếu chưa tích hợp)
  3. Thiếu hàng - reordering - nhập bù - giao nốt
- Ghi lỗi, phân loại severity, fix nhanh lỗi blocker.
- Re-test sau fix.

### Deliverable bắt buộc

- UAT report.
- Defect list + trạng thái.
- Biên bản sign-off phase core.

### Checklist nghiệm thu

- [ ] Không còn lỗi blocker.
- [ ] Không lệch tồn kho và công nợ.
- [ ] Key user xác nhận dùng được hằng ngày.

---

## Tuần 12 - Đào tạo, cutover và Go-live

### Mục tiêu tuần

- Người dùng vận hành độc lập và chuyển sang production an toàn.

### Công việc cụ thể

- Đào tạo theo vai trò (Sales/Kho/Kế toán/Quản lý).
- Chốt cutover plan:
  - Freeze nhập liệu hệ cũ
  - Backup cuối
  - Import dữ liệu chốt
- Go-live và hypercare ngày đầu.

### Deliverable bắt buộc

- Tài liệu SOP bàn giao.
- Checklist go-live hoàn tất.
- Biên bản vận hành ngày đầu.

### Checklist nghiệm thu

- [ ] Go-live không gián đoạn nghiệp vụ chính.
- [ ] Có người trực hỗ trợ giờ cao điểm.
- [ ] Báo cáo ngày đầu khớp số.

---

## 7) Tuần 13-16: Sprint custom ưu tiên cao

Điều kiện vào phase này:

- Core flow ổn định.
- Vận hành production tối thiểu 2 tuần.
- Có số liệu thực tế để tối ưu.

## Tuần 13 - Custom thanh toán

- Ưu tiên: `payment_vnpay`, `payment_qr_code`, đối soát nâng cao.
- Kết quả: thanh toán online đi production có đối soát rõ.

## Tuần 14 - Custom đơn hàng nâng cao

- Ưu tiên: timeline đơn hàng, audit thay đổi, return/cancel nâng cao.
- Kết quả: truy vết đơn đầy đủ, giảm tranh chấp nội bộ.

## Tuần 15 - CRM nâng cao và dữ liệu

- Ưu tiên: RFM phân khúc khách, duplicate check, SKU rule nâng cao.
- Kết quả: chăm sóc khách chính xác, dữ liệu sạch hơn.

## Tuần 16 - Ổn định, tối ưu và bàn giao dài hạn

- Tối ưu hiệu năng, hoàn tất tài liệu kỹ thuật custom.
- Chốt roadmap quarter tiếp theo.

---

## 8) Bộ checklist điều hành theo tuần (dùng nhanh)

Mỗi cuối tuần, PM chỉ cần xác nhận:

- [ ] Kết quả tuần đạt mục tiêu đã đặt.
- [ ] Deliverable đã bàn giao đầy đủ.
- [ ] Defect nghiêm trọng đã xử lý.
- [ ] Không phát sinh scope ngoài kiểm soát.
- [ ] Sẵn sàng vào tuần kế tiếp.

---

## 9) Mẫu báo cáo tuần (template)

Nên dùng format cố định:

- Tuần số:
- Mục tiêu tuần:
- Kết quả đạt được:
- Hạng mục chưa đạt:
- Lỗi quan trọng:
- Quyết định cần phê duyệt:
- Kế hoạch tuần tới:

---

## 10) Kết luận

Làm đúng nhịp 12-16 tuần như trên sẽ giúp:

- Go-live nhanh và kiểm soát rủi ro tốt.
- Không bị sa đà custom quá sớm.
- Có nền tảng chuẩn trước khi mở rộng tính năng nâng cao.
