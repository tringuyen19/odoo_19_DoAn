# HƯỚNG DẪN TRIỂN KHAI TO-BE TRÊN ODOO (STEP BY STEP)

Tài liệu này hướng dẫn triển khai chi tiết từ quy trình TO-BE sang Odoo theo nguyên tắc:

1. Làm **tính năng chuẩn (standard)** trước.
2. Chạy ổn định end-to-end.
3. Sau đó mới làm **custom module** theo ưu tiên.

---

## 0) Mục tiêu và phạm vi

### 0.1 Mục tiêu triển khai

- Chuẩn hóa quy trình bán hàng - kho - kế toán trên một hệ thống duy nhất.
- Đồng bộ tồn kho theo thời gian thực giữa các kênh.
- Tự động hóa các bước xác nhận đơn, giao hàng, hóa đơn, thanh toán.
- Tạo nền tảng dữ liệu sạch để làm báo cáo và custom nâng cao.

### 0.2 Phạm vi giai đoạn 1 (Go-live chuẩn Odoo)

- CRM + Sales + Inventory + Accounting.
- Website/POS (nếu dùng) đồng bộ với kho.
- Phân quyền rõ ràng theo vai trò.
- Báo cáo vận hành cơ bản.

### 0.3 Ngoài phạm vi giai đoạn 1

- Các module custom nâng cao như RFM, timeline, audit đầy đủ, tích hợp cổng thanh toán đặc thù, logic cảnh báo phức tạp.

---

## 1) Nguyên tắc triển khai

### 1.1 Nguyên tắc "Core trước, Custom sau"

- Nếu Odoo chuẩn đã đáp ứng >= 80% thì cấu hình dùng chuẩn.
- Chỉ custom khi có khoảng trống nghiệp vụ thật sự.
- Mọi custom phải có tài liệu: mục tiêu, đầu vào, đầu ra, dependency, test case.

### 1.2 Nguyên tắc dữ liệu

- Master data phải chuẩn ngay từ đầu: sản phẩm, khách hàng, kho, thuế, bảng giá.
- Dữ liệu sạch trước khi import.
- Có quy tắc đặt mã SKU, mã khách, mã đơn.

### 1.3 Nguyên tắc nghiệm thu

- Mỗi luồng nghiệp vụ đều có test case đầu-cuối.
- Chỉ chuyển phase khi pass UAT của phase trước.

---

## 2) Danh sách module cần dùng

## 2.1 Module chuẩn (triển khai trước)

- Nền tảng: `base`, `mail`, `contacts`
- Bán hàng: `sale`, `sale_management`, `sale_stock`
- Kho: `stock`, `stock_barcode`
- Mua hàng bổ sung: `purchase`, `purchase_stock`
- Kế toán: `account`, `account_accountant`
- CRM: `crm`
- Kênh online: `website_sale`, `website_sale_stock` (nếu có website)
- Bán tại quầy: `point_of_sale` (nếu có POS)

## 2.2 Module custom (triển khai sau)

Theo tài liệu giải pháp TO-BE, ví dụ:

- Thanh toán: `custom_payment_reconciliation`, `payment_vnpay`, `payment_qr_code`
- Đơn hàng: `sale_order_timeline`, `sale_order_audit`, `sale_order_return`
- CRM nâng cao: `crm_rfm_analysis`
- Dữ liệu/sản phẩm: `duplicate_check`, `product_sku_generator`, ...

---

## 3) Ánh xạ quy trình TO-BE sang module Odoo

Từ sơ đồ quy trình:

1. Tiếp nhận nhu cầu mua hàng theo kênh -> khách đến shop thì đón/ghi nhận tại quầy (`point_of_sale`, `contacts`), khách nhắn online thì phản hồi online và ghi nhận lead (`crm`, `website_sale`, `contacts`)
2. Tư vấn/chọn sản phẩm theo kênh -> tư vấn trực tiếp tại shop (`point_of_sale`) hoặc tư vấn/chốt qua online (`sale`, `website_sale`)
3. Xác nhận đơn -> `sale` + trigger `sale_stock`
4. Kiểm tra và cập nhật tồn kho -> `stock`, `sale_stock`
5. Đóng gói/giao hàng -> `stock` (Delivery Order)
6. Thanh toán offline/online -> `account`, `payment` (+ custom gateway nếu cần)
7. Xuất hóa đơn điện tử -> `account` (+ tích hợp nhà cung cấp e-invoice)
8. Kết thúc và hậu mãi -> `crm`, activity/follow-up

---

## 4) Kế hoạch triển khai step by step (thực tế)

## Step 1 - Khởi động dự án và chốt blueprint

### Việc cần làm

- Chốt quy trình chuẩn TO-BE theo vai trò: Sales, Kho, Kế toán, Quản lý.
- Chốt danh sách tính năng:
  - Nhóm A: chuẩn Odoo.
  - Nhóm B: custom bắt buộc.
  - Nhóm C: custom nâng cao (làm sau).
- Chốt KPI nghiệm thu từng luồng.

### Deliverable

- Blueprint nghiệp vụ.
- Fit/Gap matrix (As-Is vs To-Be vs Odoo Standard vs Custom).
- Danh mục backlog theo ưu tiên.

### Tiêu chí hoàn thành

- Tất cả bộ phận ký xác nhận phạm vi giai đoạn 1.

---

## Step 2 - Chuẩn bị môi trường triển khai

### Việc cần làm

- Tạo môi trường: Dev, UAT, Production.
- Thiết lập backup định kỳ database và file store.
- Tạo quy ước cấu hình:
  - Naming convention cho SKU, customer code, sales order.
  - Quy tắc tạo user và phân quyền theo nhóm.

### Deliverable

- Môi trường sẵn sàng.
- Tài liệu vận hành và backup.

### Tiêu chí hoàn thành

- Có thể deploy module và restore backup thành công.

---

## Step 3 - Chuẩn hóa và chuẩn bị dữ liệu master

### Việc cần làm

- Chuẩn hóa danh mục sản phẩm:
  - Tên chuẩn, SKU chuẩn, UoM, category, giá bán/giá vốn.
- Chuẩn hóa khách hàng:
  - Tên, SĐT, email, địa chỉ, nguồn khách.
- Chuẩn hóa dữ liệu kho:
  - Warehouse, location (khu/kệ/ngăn), tồn đầu kỳ.
- Chuẩn hóa kế toán:
  - Thuế, payment terms, journals, chart of accounts.

### Checklist dữ liệu

- Không trùng SKU.
- Không trùng số điện thoại khách.
- Không thiếu trường bắt buộc.
- Mapping cột import khớp model Odoo.

### Deliverable

- File import sạch cho Product/Partner/Stock opening.

### Tiêu chí hoàn thành

- Import thử nghiệm thành công trên UAT, không lỗi dữ liệu nghiêm trọng.

---

## Step 4 - Cấu hình CRM (tiếp nhận lead và cơ hội)

### Việc cần làm

- Bật `crm`.
- Thiết lập pipeline:
  - New -> Qualified -> Proposal/Quotation -> Won/Lost.
- Tạo lead source:
  - Website, Facebook, Zalo, Walk-in, Referral.
- Thiết lập activity tự động:
  - Nhắc gọi lại, nhắc gửi báo giá, nhắc follow-up.

### Quyền truy cập

- Sales User: xem và xử lý lead của chính mình/team.
- Sales Manager: xem toàn bộ lead team.

### Tiêu chí hoàn thành

- Lead tạo được từ nhiều nguồn.
- Chuyển stage và tạo báo giá từ CRM không lỗi.

---

## Step 5 - Cấu hình Sales (báo giá, đơn hàng)

### Việc cần làm

- Bật `sale`, `sale_management`, `sale_stock`.
- Cấu hình:
  - Pricelist.
  - Payment terms.
  - Sales team.
  - Delivery policy.
- Thiết lập flow:
  - Quotation -> Confirm SO -> Delivery -> Invoice.

### Fields nên có ngay (chuẩn hoặc studio)

- Kênh bán (online/offline).
- Nguồn đơn.
- Ngày giao dự kiến.
- Người phụ trách.

### Rule nghiệp vụ cơ bản

- Khi xác nhận SO -> tự động tạo phiếu giao và reserve tồn.
- Cảnh báo nếu thiếu tồn.

### Tiêu chí hoàn thành

- Tạo báo giá, xác nhận đơn, sinh chứng từ kho tự động hoạt động đúng.

---

## Step 6 - Cấu hình Inventory (kho, vị trí, barcode)

### Việc cần làm

- Bật `stock`, `stock_barcode`.
- Cấu hình warehouse và location theo thực tế kho.
- Cấu hình operation type:
  - Receipts, Delivery Orders, Internal Transfers.
- Thiết lập barcode cho:
  - Sản phẩm.
  - Vị trí kho.
- Thiết lập quy trình kiểm kho:
  - Inventory adjustment.
  - Cycle count theo tần suất.

### Rule tồn kho

- Reordering rules (min/max).
- Route Buy/MTO theo nhóm sản phẩm.

### Tiêu chí hoàn thành

- Từ SO có thể pick/pack/ship.
- Tồn kho cập nhật đúng sau giao hàng.
- Kiểm kho barcode chạy được trên thiết bị thực tế.

---

## Step 7 - Cấu hình Purchasing (bổ sung hàng tự động)

### Việc cần làm

- Bật `purchase`, `purchase_stock`.
- Cấu hình vendor, lead time mua.
- Liên kết reordering rule với vendor.
- Kiểm tra auto tạo RFQ/PO khi xuống ngưỡng tồn.

### Tiêu chí hoàn thành

- Khi tồn thấp hơn min, hệ thống đề xuất hoặc tạo đơn mua đúng quy tắc.

---

## Step 8 - Cấu hình Accounting & Payment

### Việc cần làm

- Bật `account`, `account_accountant`.
- Cấu hình:
  - Journals (Cash, Bank, Sales).
  - Taxes.
  - Payment methods (offline, chuyển khoản, COD).
- Cấu hình luồng:
  - Invoice từ Sales.
  - Ghi nhận thanh toán.
  - Reconciliation ngân hàng.

### Công nợ

- Bật báo cáo aging.
- Cấu hình lịch nhắc công nợ tự động (nếu dùng chuẩn được thì ưu tiên chuẩn).

### Tiêu chí hoàn thành

- Luồng SO -> Invoice -> Payment -> Reconciliation chạy thông suốt.

---

## Step 9 - Cấu hình Website/POS (nếu áp dụng)

### Website

- Bật `website_sale`, `website_sale_stock`.
- Bật hiển thị tồn khả dụng.
- Chặn mua khi hết hàng.

### POS

- Bật `point_of_sale`.
- Cấu hình POS session, POS payment methods, POS stock location.
- Kiểm tra đồng bộ tồn kho tức thời với backend.

### Tiêu chí hoàn thành

- Bán trên website/POS đều trừ chung một tồn kho và không oversell.

---

## Step 10 - Thiết kế phân quyền và kiểm soát truy cập

### Nhóm quyền chuẩn

- Sales User / Sales Manager
- Inventory User / Inventory Manager
- Accountant / Accounting Manager
- System Administrator

### Thiết kế access

- Access rights theo model (create/read/write/delete).
- Record rules theo team/kho/công ty.
- Field-level restriction với field nhạy cảm (nếu cần).

### Tiêu chí hoàn thành

- User đúng vai trò chỉ thấy đúng dữ liệu cần thiết.

---

## Step 11 - Thiết kế thông báo và phối hợp liên phòng ban

### Việc cần làm

- Dùng chatter + activities cho SO, picking, invoice.
- Tạo template thông báo cho các sự kiện:
  - SO xác nhận.
  - Đơn quá hạn giao.
  - Tồn kho thấp.
  - Công nợ quá hạn.

### Tiêu chí hoàn thành

- Sales/Kho/Kế toán nhận thông báo đúng thời điểm.

---

## Step 12 - Báo cáo và dashboard vận hành chuẩn

### Báo cáo bắt buộc

- Sales: doanh thu theo kênh/nhân viên/sản phẩm.
- Inventory: tồn hiện tại, tồn theo vị trí, stock moves, out-of-stock risk.
- Accounting: doanh thu, công nợ phải thu, tuổi nợ.
- CRM: tỷ lệ chuyển đổi lead -> đơn hàng.

### Tiêu chí hoàn thành

- Quản lý xem được dashboard realtime cho các KPI cốt lõi.

---

## Step 13 - UAT theo kịch bản nghiệp vụ end-to-end

### Kịch bản test tối thiểu

1. Lead mới -> báo giá -> xác nhận SO.
2. SO có hàng -> giao hàng -> xuất hóa đơn -> thanh toán.
3. SO thiếu hàng -> trigger reordering -> mua hàng -> nhập kho -> giao.
4. Website/POS bán hàng đồng thời -> kiểm tra tồn kho đồng bộ.
5. Kiểm tra phân quyền theo vai trò.

### Mẫu tiêu chí pass

- Không sai lệch tồn kho.
- Không sai lệch công nợ.
- Không có user truy cập dữ liệu ngoài phạm vi.

---

## Step 14 - Đào tạo, SOP, go-live

### Việc cần làm

- Đào tạo theo vai trò:
  - Sales.
  - Kho.
  - Kế toán.
  - Quản lý.
- Viết SOP chuẩn cho từng luồng.
- Chốt kế hoạch cutover dữ liệu và go-live.

### Tiêu chí hoàn thành

- Người dùng vận hành độc lập theo SOP.
- Go-live checklist đạt 100%.

---

## Step 15 - Giai đoạn custom sau go-live (theo sprint)

## 15.1 Cách ưu tiên custom

- Ưu tiên theo tác động doanh thu/rủi ro vận hành.
- Mỗi custom phải có business owner và test case rõ ràng.

## 15.2 Gợi ý thứ tự custom

1. Thanh toán tích hợp (`payment_vnpay`, `payment_qr_code`, đối soát nâng cao)
2. Đơn hàng nâng cao (`sale_order_timeline`, `sale_order_audit`, return/cancel flow)
3. CRM nâng cao (`crm_rfm_analysis`)
4. Data governance nâng cao (`duplicate_check`, SKU generator/validator)
5. Dashboard/KPI nâng cao theo quản trị

## 15.3 Quy trình mỗi sprint custom

- Phân tích yêu cầu chi tiết.
- Thiết kế kỹ thuật + dependency.
- Development + unit test.
- UAT.
- Deployment.
- Hypercare 1-2 tuần.

---

## 5) Dependency chính giữa module và dữ liệu

### 5.1 Dependency module

- `sale_stock` cần `sale` + `stock`.
- `website_sale_stock` cần `website_sale` + `stock`.
- `purchase_stock` cần `purchase` + `stock`.
- `account` nhận dữ liệu từ `sale`/`stock` để hóa đơn và đối soát.
- Custom payment phụ thuộc `account/payment`.

### 5.2 Dependency dữ liệu

- Product master là lõi của Sales + Inventory + Purchase + Accounting.
- Customer master là lõi của CRM + Sales + Accounting.
- Warehouse/location là lõi của mọi nghiệp vụ kho.
- Tax/journal/payment term là lõi cho hóa đơn và công nợ.

---

## 6) RACI triển khai đề xuất

- Project Owner: chốt phạm vi và quyết định nghiệp vụ.
- Key User Sales: xác nhận quy trình bán.
- Key User Kho: xác nhận quy trình kho.
- Key User Kế toán: xác nhận hạch toán và công nợ.
- Technical Lead: phụ trách kiến trúc, custom, deployment.
- QA/UAT Lead: phụ trách test scenario và sign-off.

---

## 7) Kế hoạch thời gian tham chiếu (12-16 tuần)

- Tuần 1-2: Blueprint + môi trường + chuẩn dữ liệu
- Tuần 3-6: CRM + Sales + Inventory core
- Tuần 7-8: Purchase + Accounting core
- Tuần 9-10: Website/POS + phân quyền + báo cáo
- Tuần 11-12: UAT + đào tạo + go-live
- Tuần 13-16: Sprint custom ưu tiên cao

---

## 8) Checklist go-live cuối cùng

- [ ] Master data đã chốt và khóa quy tắc nhập liệu.
- [ ] Toàn bộ user đã được phân quyền đúng.
- [ ] Test E2E pass toàn bộ kịch bản bắt buộc.
- [ ] Backup/restore đã kiểm chứng.
- [ ] SOP và tài liệu đào tạo đã bàn giao.
- [ ] Hypercare plan sau go-live đã chuẩn bị.

---

## 9) Kết luận

Nếu đi theo đúng thứ tự trên, bạn sẽ:

- Go-live nhanh hơn vì tận dụng tối đa module chuẩn Odoo.
- Giảm rủi ro do custom sớm.
- Có nền dữ liệu và quy trình ổn định trước khi mở rộng custom.

Khuyến nghị thực thi: khóa phạm vi giai đoạn 1 thật chặt, chỉ nhận custom mới sau khi hoàn tất UAT của core flow.

---

## 10) SOP setup chi tiết từng module theo sơ đồ TO-BE

Mục này đi theo đúng logic trong sơ đồ: Tiếp nhận nhu cầu -> Tư vấn/chốt đơn -> Kiểm kho/giao hàng -> Thanh toán -> Hóa đơn.

Lưu ý:

- Đường dẫn menu có thể khác nhẹ theo edition/community/enterprise và ngôn ngữ giao diện.
- Nếu menu chưa thấy, bật Developer Mode để kiểm tra quyền và technical settings.

## 10.1 CRM - Tiếp nhận khách hàng và nhu cầu ban đầu

### Bước CRM-01: Cài module và bật tính năng cơ bản

- Module: `crm`, `contacts`
- Menu: Apps -> tìm "CRM" -> Install
- Menu cấu hình: CRM -> Configuration -> Settings
- Thiết lập:
  - Enable Leads: Bật
  - Enable Activities: Bật
  - Enable Multi Teams: Bật (nếu có nhiều nhóm sales)

Kết quả mong đợi:

- Có menu Leads/Pipeline.
- Nhân viên sales tạo lead mới được.

Test nhanh:

- Tạo lead mẫu "KH Walk-in - Nguyen A" và lưu thành công.

### Bước CRM-02: Tạo pipeline theo TO-BE

- Menu: CRM -> Configuration -> Pipeline Stages
- Tạo stages:
  1. New
  2. Qualified
  3. Proposal/Quotation
  4. Negotiation
  5. Won
  6. Lost

Giá trị mẫu:

- Probability: New 10%, Qualified 30%, Proposal 60%, Negotiation 80%, Won 100%

Kết quả mong đợi:

- Pipeline phản ánh đúng tiến trình chăm sóc khách trong sơ đồ.

Test nhanh:

- Kéo một lead đi qua các stage, hệ thống cập nhật timestamp stage.

### Bước CRM-03: Thiết lập nguồn khách và phân công

- Menu: CRM -> Configuration -> Lead Generation -> Lead Sources
- Tạo source:
  - Website
  - Facebook
  - Zalo
  - Walk-in
  - Referral
- Menu: CRM -> Configuration -> Sales Teams
  - Tạo team Online, team Offline

Kết quả mong đợi:

- Mỗi lead có nguồn rõ ràng để đo hiệu quả kênh.

Test nhanh:

- Tạo 5 lead với 5 nguồn khác nhau, lọc theo source ra đúng dữ liệu.

---

## 10.2 Sales - Tư vấn, báo giá, xác nhận đơn

### Bước SALE-01: Bật cấu hình bán hàng cốt lõi

- Module: `sale`, `sale_management`, `sale_stock`
- Menu: Sales -> Configuration -> Settings
- Thiết lập:
  - Quotations: Bật
  - Online Signature: Bật (nếu dùng)
  - Online Payment: Bật (nếu dùng website)
  - Pricelists: Bật (nếu có nhiều chính sách giá)
  - Discounts: Bật (nếu có chiết khấu theo dòng)

Kết quả mong đợi:

- Luồng báo giá -> xác nhận đơn hoạt động đầy đủ.

### Bước SALE-02: Cấu hình dữ liệu bán hàng

- Menu: Sales -> Configuration -> Pricelists
  - Tạo "Retail Price", "VIP Price"
- Menu: Accounting -> Configuration -> Payment Terms
  - Tạo "Thanh toán ngay", "Công nợ 7 ngày"
- Menu: Sales -> Configuration -> Sales Teams
  - Online Team, Showroom Team

Kết quả mong đợi:

- Sales chọn nhanh bảng giá và điều khoản thanh toán khi lập báo giá.

### Bước SALE-03: Tạo trường nghiệp vụ theo TO-BE

- Cách làm: dùng Odoo Studio hoặc custom nhẹ sau.
- Fields đề xuất trên `sale.order`:
  - `x_sales_channel` (Selection): Online/Offline
  - `x_order_source` (Many2one/Selection): Facebook/Zalo/Walk-in/Website
  - `commitment_date` (Datetime): Ngày giao dự kiến
  - `x_internal_note` (Text): Ghi chú phối hợp kho

Kết quả mong đợi:

- Đơn hàng thể hiện đủ thông tin kênh và nguồn.

Test nhanh:

- Tạo báo giá có đủ trường và chuyển xác nhận thành công.

### Bước SALE-04: Rule xác nhận đơn và chuyển kho

- Menu: Sales -> Orders -> Quotations -> mở báo giá -> Confirm
- Kỳ vọng hệ thống:
  - Tạo Sales Order
  - Tạo Delivery Order
  - Reserve tồn kho nếu đủ hàng

Kết quả mong đợi:

- Bước "Xác nhận đơn hàng với khách hàng" trong sơ đồ đã được số hóa.

Test nhanh:

- SO có 1 sản phẩm tồn đủ: Delivery ở trạng thái Ready.
- SO có 1 sản phẩm thiếu: Delivery ở trạng thái Waiting/Not Available.

---

## 10.3 Inventory - Kiểm kho, xuất kho, cập nhật tồn theo thời gian thực

### Bước INV-01: Thiết lập kho và vị trí

- Module: `stock`, `stock_barcode`
- Menu: Inventory -> Configuration -> Settings
  - Storage Locations: Bật
  - Multi-Step Routes: Bật (nếu có pick-pack-ship)
  - Barcode: Bật
- Menu: Inventory -> Configuration -> Warehouses
  - Tạo "Kho chính"
- Menu: Inventory -> Configuration -> Locations
  - Tạo cấu trúc: Kho chính / Khu A / Kệ A1 / Ngăn 1

Kết quả mong đợi:

- Kho có cấu trúc vị trí rõ, hỗ trợ tìm hàng nhanh.

### Bước INV-02: Cấu hình operation type theo TO-BE

- Menu: Inventory -> Configuration -> Operation Types
- Đảm bảo có:
  - Receipts
  - Delivery Orders
  - Internal Transfers
- Nếu kho lớn:
  - Bật 2-step hoặc 3-step delivery (Pick + Pack + Ship)

Kết quả mong đợi:

- Luồng kho bám sát bước "NV kho xử lý đơn" trong sơ đồ.

### Bước INV-03: Reordering rules (min/max)

- Menu: Inventory -> Products -> mở sản phẩm -> Reordering Rules
- Giá trị mẫu:
  - Min Quantity: 5
  - Max Quantity: 20
  - To Order: Auto/Manual theo chính sách

Kết quả mong đợi:

- Khi tồn < min, hệ thống đề xuất mua bù.

Test nhanh:

- Giảm tồn xuống 4, chạy scheduler, kiểm tra RFQ/PO được tạo hoặc đề xuất.

### Bước INV-04: Barcode và kiểm kho định kỳ

- Menu: Inventory -> Operations -> Inventory Adjustments
  - Tạo phiếu kiểm kho theo khu vực
- Menu: Inventory -> Barcode (trên mobile gun)
  - Quét vị trí
  - Quét sản phẩm
  - Nhập số lượng thực tế

Kết quả mong đợi:

- Kiểm kho nhanh, giảm sai lệch Excel thủ công.

---

## 10.4 Purchase - Bổ sung hàng khi thiếu

### Bước PUR-01: Cấu hình mua hàng

- Module: `purchase`, `purchase_stock`
- Menu: Purchase -> Configuration -> Settings
  - Purchase Agreements (nếu cần)
  - Vendor Pricelists: Bật
- Menu: Purchase -> Configuration -> Vendors
  - Tạo nhà cung cấp chính cho từng nhóm hàng

Kết quả mong đợi:

- Sản phẩm có vendor để hệ thống phát sinh RFQ chính xác.

### Bước PUR-02: Liên kết sản phẩm với vendor và lead time

- Menu: Inventory -> Products -> mở sản phẩm -> tab Purchase
- Cấu hình:
  - Vendor
  - Price
  - Delivery Lead Time

Test nhanh:

- Tạo RFQ từ reordering rule, kiểm tra đúng vendor và thời gian giao.

---

## 10.5 Accounting - Thanh toán, công nợ, hóa đơn

### Bước ACC-01: Cấu hình kế toán nền tảng

- Module: `account`, `account_accountant`
- Menu: Accounting -> Configuration -> Settings
- Thiết lập:
  - Chart of Accounts (theo local chart)
  - Taxes
  - Fiscal Period Lock Date
  - Currencies (nếu cần đa tiền tệ)

Kết quả mong đợi:

- Có nền tảng để hạch toán doanh thu và công nợ chuẩn.

### Bước ACC-02: Journals và phương thức thanh toán

- Menu: Accounting -> Configuration -> Journals
  - Tạo/cập nhật journals:
    - Bank
    - Cash
    - Sales
- Menu: Accounting -> Configuration -> Payment Providers/Methods
  - Offline: tiền mặt/chuyển khoản/COD
  - Online: cổng chuẩn hoặc custom phase sau

Kết quả mong đợi:

- Bước "Thanh toán Offline/Online" trong sơ đồ có mapping rõ trong hệ thống.

### Bước ACC-03: Luồng hóa đơn từ đơn bán

- Menu: Sales -> Orders -> mở SO -> Create Invoice
- Trạng thái mục tiêu:
  - Invoice: Posted
  - Payment: In Payment/Paid
- Reconciliation:
  - Menu: Accounting -> Accounting -> Reconciliation

Kết quả mong đợi:

- Hoàn tất chuỗi SO -> Invoice -> Payment.

### Bước ACC-04: Công nợ và nhắc nợ

- Menu: Accounting -> Customers -> Aged Receivable
- Thiết lập lịch nhắc nợ (chuẩn hoặc custom sau)

Test nhanh:

- Tạo invoice chưa thanh toán, kiểm tra lên báo cáo tuổi nợ đúng.

---

## 10.6 Website/POS - Đồng bộ đa kênh theo TO-BE

### Bước CH-01: Website sale stock

- Module: `website_sale`, `website_sale_stock`
- Menu: Website -> Configuration -> Settings
  - Bật eCommerce
  - Hiển thị tồn khả dụng (nếu policy cho phép)
  - Chặn checkout khi hết hàng

Kết quả mong đợi:

- Khách hàng thấy tồn kho gần realtime trên website.

### Bước CH-02: POS (nếu có bán tại cửa hàng)

- Module: `point_of_sale`
- Menu: Point of Sale -> Configuration -> Point of Sale
  - Chọn kho/location trừ tồn
  - Chọn payment methods tại quầy

Kết quả mong đợi:

- Bán tại quầy trừ cùng kho với Sales/Website, tránh lệch tồn.

---

## 10.7 Security - Access rights và record rules

### Bước SEC-01: Tạo user group theo vai trò

- Menu: Settings -> Users & Companies -> Groups
- Nhóm bắt buộc:
  - Sales User/Manager
  - Inventory User/Manager
  - Accountant/Manager

### Bước SEC-02: Gán quyền và kiểm thử truy cập

- Menu: Settings -> Users & Companies -> Users
  - Gán user vào đúng nhóm
- Kiểm thử:
  - Sales không sửa tồn kho
  - Kho không post bút toán kế toán
  - Kế toán không chỉnh chứng từ kho vận hành

Kết quả mong đợi:

- Đúng người, đúng quyền, đúng dữ liệu.

---

## 10.8 Automation - Thông báo và nhắc việc theo sự kiện

### Bước AUTO-01: Hoạt động chuẩn không custom

- Dùng chatter, scheduled activities, email template.
- Sự kiện áp dụng:
  - SO được confirm -> kho nhận việc
  - Delivery quá hạn -> cảnh báo quản lý
  - Tồn thấp -> cảnh báo mua hàng
  - Invoice quá hạn -> nhắc công nợ

Kết quả mong đợi:

- Giảm phụ thuộc trao đổi thủ công giữa phòng ban.

---

## 10.9 Kịch bản test E2E bám sát sơ đồ TO-BE

### Test Case E2E-01: Đơn đủ hàng, thanh toán offline

1. Tạo lead từ nguồn Zalo.
2. Chuyển sang quotation, thêm sản phẩm.
3. Confirm SO.
4. Kho xử lý Delivery và Validate.
5. Kế toán tạo invoice, ghi nhận thanh toán tiền mặt.
6. Kiểm tra tồn kho đã trừ và đơn hoàn tất.

Kỳ vọng:

- Trạng thái SO done, delivery done, invoice paid.

### Test Case E2E-02: Đơn online, thanh toán online

1. Khách đặt hàng trên website.
2. Hệ thống kiểm tra tồn và giữ hàng.
3. Thanh toán qua provider online.
4. Kho giao hàng.
5. Hóa đơn và đối soát giao dịch.

Kỳ vọng:

- Không oversell, trạng thái thanh toán và đơn hàng khớp.

### Test Case E2E-03: Thiếu hàng và bù hàng tự động

1. Xác nhận SO làm tồn xuống dưới min.
2. Scheduler kích hoạt reordering.
3. Tạo RFQ/PO cho vendor.
4. Nhập kho.
5. Giao nốt đơn chờ.

Kỳ vọng:

- Chuỗi bổ sung hàng chạy đúng, không rơi đơn.

---

## 10.10 Danh sách custom chỉ mở sau khi hoàn tất setup chuẩn

Chỉ chuyển sang custom khi đạt đủ điều kiện:

- E2E core flow pass.
- Người dùng vận hành ổn định tối thiểu 2-4 tuần.
- Báo cáo chuẩn đủ dùng cho quản trị cơ bản.

Custom ưu tiên theo thứ tự:

1. `payment_vnpay` / `payment_qr_code` / đối soát nâng cao.
2. `sale_order_timeline` / `sale_order_audit` / return flow nâng cao.
3. `crm_rfm_analysis`.
4. Data governance nâng cao (duplicate/SKU rule nâng cao).
