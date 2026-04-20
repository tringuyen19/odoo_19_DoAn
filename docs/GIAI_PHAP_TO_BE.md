# **GIẢI PHÁP ĐỀ XUẤT - QUY TRÌNH TO BE**

**MỤC TIÊU**

Chuyển đổi từ quy trình thủ công sang hệ thống quản lý tích hợp (ERP), tự động hóa toàn bộ quy trình bán hàng, giải quyết triệt để các pain points đã xác định, nâng cao hiệu suất vận hành và trải nghiệm khách hàng.

---

## **📋 TỔNG QUAN GIẢI PHÁP**


| Nhóm vấn đề          | Giải pháp chính                                        | Mức độ ưu tiên | Lợi ích chính                                        |
| -------------------- | ------------------------------------------------------ | -------------- | ---------------------------------------------------- |
| Vấn đề về dữ liệu    | Hệ thống database tập trung, chuẩn hóa dữ liệu tự động | 🔴 Cao         | Dữ liệu chính xác, nhất quán, không mất mát          |
| Vấn đề về quy trình  | Workflow tự động hóa, thông báo và phối hợp real-time  | 🔴 Cao         | Tiết kiệm thời gian, giảm sai sót, tăng tốc độ xử lý |
| Vấn đề về tồn kho    | Quản lý kho thông minh, đồng bộ đa kênh real-time      | 🔴 Cao         | Kiểm soát tồn kho chính xác, tránh hết hàng/tồn đọng |
| Vấn đề về khách hàng | CRM tích hợp, cá nhân hóa trải nghiệm khách hàng       | 🟡 Trung bình  | Tăng sự hài lòng, tỷ lệ quay lại và giá trị đơn hàng |
| Vấn đề về báo cáo    | Dashboard real-time, phân tích thông minh tự động      | 🟢 Thấp        | Ra quyết định nhanh, chính xác dựa trên dữ liệu      |


---

## **🎯 1. GIẢI PHÁP CHO VẤN ĐỀ VỀ DỮ LIỆU**

### **1.1 Vấn đề: Nhập liệu thủ công**

**Pain Point hiện tại:**

- Nhân viên phải nhập tay tất cả thông tin vào Excel
- Nhập các thuộc tính sản phẩm sai (tên, size, màu sắc, giá,...)
- Tốn thời gian, dễ nhầm lẫn, mệt mỏi

**Giải pháp đề xuất:**

**A. Form nhập liệu chuẩn hóa với validation tự động**

**🔧 Odoo Module:** `product`, `sale`, `base` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Form nhập liệu chuẩn cho sản phẩm, khách hàng, đơn hàng
- ✅ Validation tự động cho các trường bắt buộc
- ✅ Dropdown/Selection cho dữ liệu chuẩn
- ✅ Tự động format số tiền, số điện thoại

**Cấu hình:**
- Thay thế Excel bằng form điện tử có cấu trúc rõ ràng
- Mỗi loại dữ liệu (sản phẩm, khách hàng, đơn hàng) có form riêng với các trường thông tin cố định
- Hệ thống tự động kiểm tra tính hợp lệ của dữ liệu khi nhập

**Ví dụ cụ thể - Form tạo sản phẩm:**

```
┌─────────────────────────────────────────┐
│ TẠO SẢN PHẨM MỚI                        │
├─────────────────────────────────────────┤
│ Mã sản phẩm*: [VDC-001]                 │ ← Tự động sinh hoặc nhập
│ Tên sản phẩm*: [Váy cưới cách tân A]    │ ← Bắt buộc nhập
│ Loại sản phẩm*: [▼ Váy cưới cách tân]   │ ← Dropdown, không cho nhập tự do
│ Size*: [▼ S] [▼ M] [▼ L] [▼ XL]        │ ← Chọn nhiều size
│ Màu sắc*: [▼ Trắng] [▼ Hồng]           │ ← Dropdown chuẩn
│ Giá bán*: [5,000,000] VNĐ              │ ← Chỉ nhận số, tự động format
│ Giá nhập: [3,000,000] VNĐ              │
│ Mô tả: [Textarea...]                    │
│                                         │
│ [Hủy]  [Lưu & Tạo mới]  [Lưu]          │
└─────────────────────────────────────────┘
```

**B. Tính năng Auto-complete và gợi ý thông minh**

**🔧 Odoo Module:** `web` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Many2one field có auto-complete tự động
- ✅ Tìm kiếm theo tên, mã, số điện thoại
- ✅ Hiển thị thông tin bổ sung (số đơn đã mua, tổng chi tiêu)

**Cấu hình:**
- Khi nhập tên khách hàng hoặc sản phẩm, hệ thống tự động gợi ý các bản ghi đã có
- Giảm thời gian nhập, tránh tạo trùng lặp

**Ví dụ:**

```
Nhập: "Nguyễn Văn A"
Hệ thống gợi ý:
  → Nguyễn Văn An - 0901234567 (Đã mua 3 lần)
  → Nguyễn Văn Anh - 0912345678 (Khách mới)
```

**C. Import dữ liệu hàng loạt từ Excel**

**🔧 Odoo Module:** `base_import` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Import từ CSV/Excel với template chuẩn
- ✅ Validate dữ liệu trước khi import
- ✅ Báo lỗi chi tiết từng dòng
- ✅ Mapping cột tự động

**Cấu hình:**
- Cung cấp template Excel chuẩn để nhập hàng loạt sản phẩm/khách hàng
- Hệ thống validate dữ liệu trước khi import
- Báo lỗi chi tiết nếu có dữ liệu không hợp lệ

**Quy trình import:**

```
1. Tải template Excel chuẩn từ hệ thống
2. Điền dữ liệu vào template
3. Upload file lên hệ thống
4. Hệ thống kiểm tra và báo lỗi (nếu có)
5. Xác nhận import → Dữ liệu được tạo tự động
```

**D. Quét mã vạch (Barcode) để nhập nhanh**

**🔧 Odoo Module:** `barcodes`, `stock_barcode` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Tự động sinh barcode cho sản phẩm
- ✅ Quét barcode bằng máy quét hoặc camera
- ✅ Tự động thêm sản phẩm vào đơn hàng khi quét
- ✅ Hỗ trợ nhiều loại barcode (EAN13, Code128, QR Code)

**Cấu hình:**
- Mỗi sản phẩm có mã vạch duy nhất
- Sử dụng máy quét hoặc camera điện thoại để quét mã
- Tự động điền thông tin sản phẩm vào đơn hàng

**Ví dụ quy trình bán hàng:**

```
1. Khách chọn sản phẩm
2. Nhân viên quét barcode → Sản phẩm tự động thêm vào đơn
3. Nhập số lượng → Giá tự động tính
4. Xác nhận → Hoàn thành
```

**Lợi ích:**

- ✅ Giảm 70% thời gian nhập liệu
- ✅ Giảm 90% lỗi nhập sai thông tin
- ✅ Dữ liệu chuẩn hóa, dễ tìm kiếm và báo cáo

---

### **1.2 Vấn đề: Dữ liệu không real-time**

**Pain Point hiện tại:**

- File Excel lưu trên máy cá nhân, không đồng bộ
- Cập nhật tồn kho không kịp thời trong giờ cao điểm
- Nhân viên bán hàng tư vấn sai, nhân viên kho tốn thời gian tìm sản phẩm

**Giải pháp đề xuất:**

**A. Hệ thống database tập trung trên server**

**🔧 Odoo Module:** `base` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Database PostgreSQL tập trung trên server
- ✅ Tất cả user truy cập cùng 1 nguồn dữ liệu
- ✅ Hỗ trợ cloud (Odoo.sh) hoặc on-premise
- ✅ Backup tự động, bảo mật cao

**Cấu hình:**
- Tất cả dữ liệu lưu trữ trên 1 server duy nhất (cloud hoặc local server)
- Tất cả nhân viên truy cập vào cùng 1 nguồn dữ liệu
- Không còn file Excel riêng lẻ trên từng máy

**Kiến trúc hệ thống:**

```
                    ┌─────────────────┐
                    │  SERVER (Cloud) │
                    │   Database      │
                    └────────┬────────┘
                             │
        ┌────────────────────┼
        │                    │                    
   ┌────▼────┐         ┌────▼────┐         
   │ Máy tính│         │ Máy tính│        
   │ NV Bán  │         │ NV Kho  │         
   └─────────┘         └─────────┘       
   
   → Tất cả cùng xem 1 dữ liệu, cập nhật tức thời
```

**B. Cập nhật dữ liệu tức thời (Real-time sync)**

**🔧 Odoo Module:** `bus`, `web` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Real-time notification qua bus messaging
- ✅ Tự động cập nhật UI khi có thay đổi
- ✅ Multi-user concurrent access
- ✅ Conflict detection tự động

**Cấu hình:**
- Khi 1 nhân viên thay đổi dữ liệu → Tất cả nhân viên khác thấy ngay lập tức
- Không cần refresh, không cần đóng mở file

**Ví dụ thực tế:**

```
Tình huống: Khách mua sản phẩm tại cửa hàng

10:00:00 - NV Bán tạo đơn hàng cho sản phẩm "Váy cưới A"
10:00:01 - Hệ thống tự động trừ tồn kho: 10 → 9 cái
10:00:02 - NV Kho thấy ngay thông báo: "Đơn hàng mới #SO001"
10:00:04 - Website tự động cập nhật: "Còn 9 sản phẩm"
```

**C. Multi-user access với phân quyền**

**🔧 Odoo Module:** `base` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ User & Group management
- ✅ Role-based access control (RBAC)
- ✅ Record rules (phân quyền theo dữ liệu)
- ✅ Field-level security

**Cấu hình:**
- Nhiều người có thể làm việc đồng thời trên hệ thống
- Mỗi người có quyền truy cập khác nhau theo vai trò

**Phân quyền đề xuất:**

```
┌─────────────────┬─────────┬─────────┬─────────┬─────────┐
│ Chức năng       │ NV Bán  │ NV Kho  │ Quản lý │ Kế toán │
├─────────────────┼─────────┼─────────┼─────────┼─────────┤
│ Tạo đơn hàng    │    ✓    │    ✗    │    ✓    │    ✗    │
│ Xem tồn kho     │    ✓    │    ✓    │    ✓    │    ✗    │
│ Cập nhật kho    │    ✗    │    ✓    │    ✓    │    ✗    │
│ Xem báo cáo     │    ✗    │    ✗    │    ✓    │    ✓    │
│ Sửa giá        │    ✗    │    ✗    │    ✓    │    ✗    │
└─────────────────┴─────────┴─────────┴─────────┴─────────┘
```

**D. Thông báo tự động khi có thay đổi quan trọng**

**🔧 Odoo Module:** `mail` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Activity notifications
- ✅ Real-time pop-up alerts
- ✅ Email notifications
- ✅ Badge counter cho thông báo chưa đọc

**Cấu hình:**
- Pop-up notification trên màn hình
- Âm thanh cảnh báo (nếu cần)
- Badge đếm số thông báo chưa đọc

**Ví dụ thông báo:**

```
🔔 Thông báo mới (3)
├─ 10:05 - Đơn hàng #SO001 đã được xác nhận
├─ 10:10 - Sản phẩm "Váy cưới B" sắp hết hàng (còn 2)
└─ 10:15 - Khách hàng "Nguyễn Thị B" vừa nhắn tin
```

**Lợi ích:**

- ✅ 100% dữ liệu luôn chính xác, cập nhật
- ✅ Không còn xung đột dữ liệu giữa các nhân viên
- ✅ Giảm 90% thời gian chờ đợi thông tin
- ✅ Làm việc linh hoạt, không bị ràng buộc vị trí

---

### **1.3 Vấn đề: Không có validation**

**Pain Point hiện tại:**

- Nhập chữ vào ô số lượng
- Cột dữ liệu có nhiều định dạng khác nhau (váy cưới cách tân, váy cưới c.tân), (Size XL, XL)
- Dữ liệu không chuẩn → Khó tìm kiếm, báo cáo sai

**Giải pháp đề xuất:**

**A. Validation rules tự động theo từng loại dữ liệu**

**🔧 Odoo Module:** `base`, `product`, `sale` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Field type validation (Integer, Float, Char, Email, Phone)
- ✅ Required field validation
- ✅ Domain constraints
- ✅ Auto-format cho số tiền, số điện thoại

**1. Validation cho trường số (Số lượng, Giá, Số điện thoại)**

```
Trường: Số lượng
- Chỉ cho phép nhập số nguyên dương
- Không cho phép nhập chữ, ký tự đặc biệt
- Không cho phép số âm hoặc số thập phân

Ví dụ:
✓ Hợp lệ: 1, 10, 100
✗ Không hợp lệ: "abc", -5, 10.5, "10 cái"
→ Hiển thị lỗi: "Số lượng phải là số nguyên dương"
```

**2. Validation cho trường giá tiền**

```
Trường: Giá bán
- Chỉ cho phép số dương
- Cho phép số thập phân (VD: 1,500,000.50)
- Tự động format theo định dạng tiền tệ

Ví dụ:
Nhập: 5000000
Hiển thị: 5,000,000 VNĐ
```

**3. Validation cho email**

```
Trường: Email khách hàng
- Phải có định dạng email hợp lệ
- Phải có @ và domain

Ví dụ:
✓ Hợp lệ: customer@gmail.com
✗ Không hợp lệ: "customer", "customer@", "@gmail.com"
→ Hiển thị lỗi: "Email không hợp lệ"
```

**4. Validation cho số điện thoại**

```
Trường: Số điện thoại
- Chỉ cho phép số
- Độ dài 10-11 số
- Tự động format: 0901234567 → 090 123 4567

Ví dụ:
✓ Hợp lệ: 0901234567, 0123456789
✗ Không hợp lệ: "090-123-4567", "090.123.4567", "12345"
```

**B. Dropdown/Selection cho dữ liệu chuẩn (không cho nhập tự do)**

**🔧 Odoo Module:** `product`, `sale` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Selection field cho dropdown
- ✅ Many2one field cho danh mục
- ✅ Product attributes cho size, màu sắc
- ✅ Status workflow cho trạng thái đơn hàng

**1. Danh mục sản phẩm**

```
Loại sản phẩm: [Dropdown ▼]
  - Váy cưới cách tân
  - Váy cưới truyền thống
  - Váy cưới công chúa
  - Váy dạ hội
  - Phụ kiện

→ Nhân viên CHỈ được chọn, KHÔNG được nhập tự do
→ Đảm bảo 100% dữ liệu chuẩn
```

**2. Size sản phẩm**

```
Size: [Multi-select ▼]
  □ XS
  □ S
  □ M
  □ L
  □ XL
  □ XXL

→ Chọn nhiều size cho 1 sản phẩm
→ Không còn "XL", "X-L", "size XL" khác nhau
```

**3. Màu sắc**

```
Màu sắc: [Dropdown với color picker ▼]
  - 🔴 Đỏ
  - ⚪ Trắng
  - 🔵 Xanh dương
  - 🟡 Vàng
  - 🟣 Tím
  - 🟤 Nâu
  - ⚫ Đen

→ Hiển thị màu trực quan
→ Dữ liệu chuẩn hóa
```

**4. Trạng thái đơn hàng**

```
Trạng thái: [Dropdown ▼]
  - Báo giá (Quotation)
  - Đã xác nhận (Confirmed)
  - Đang đóng gói (Packing)
  - Đã giao hàng (Delivered)
  - Hoàn thành (Done)
  - Hủy (Cancelled)

→ Quy trình chuẩn, dễ theo dõi
```

**C. Ràng buộc dữ liệu (Constraints)**

**🔧 Odoo Module:** `base`, `product`, `sale` (Cần customize một phần)

**Tính năng có sẵn trong Odoo:**
- ✅ Required field validation
- ⚠️ Custom business logic constraints (Cần customize)

**💻 Customize Python cho ràng buộc nghiệp vụ:**

```python
# Module: product_constraints
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.constrains('list_price', 'standard_price')
    def _check_price_logic(self):
        """Kiểm tra giá bán phải lớn hơn giá nhập"""
        for product in self:
            if product.list_price > 0 and product.standard_price > 0:
                if product.list_price < product.standard_price:
                    raise ValidationError(
                        f"Giá bán ({product.list_price:,.0f} VNĐ) phải lớn hơn "
                        f"giá nhập ({product.standard_price:,.0f} VNĐ)"
                    )

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.constrains('product_uom_qty', 'product_id')
    def _check_stock_availability(self):
        """Kiểm tra số lượng bán không vượt quá tồn kho"""
        for line in self:
            if line.product_id.type == 'product':
                available_qty = line.product_id.qty_available
                if line.product_uom_qty > available_qty:
                    raise ValidationError(
                        f"Không đủ hàng trong kho!\n"
                        f"Sản phẩm: {line.product_id.name}\n"
                        f"Tồn kho: {available_qty:.0f}\n"
                        f"Yêu cầu: {line.product_uom_qty:.0f}"
                    )

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.constrains('commitment_date', 'date_order')
    def _check_delivery_date(self):
        """Kiểm tra ngày giao hàng phải >= ngày đặt hàng"""
        for order in self:
            if order.commitment_date and order.date_order:
                if order.commitment_date < order.date_order.date():
                    raise ValidationError(
                        "Ngày giao hàng không hợp lệ!\n"
                        f"Ngày đặt: {order.date_order.strftime('%d/%m/%Y')}\n"
                        f"Ngày giao: {order.commitment_date.strftime('%d/%m/%Y')}"
                    )
```

**1. Trường bắt buộc (Required fields)**

```
Khi tạo sản phẩm:
- Mã sản phẩm*     ← Bắt buộc
- Tên sản phẩm*    ← Bắt buộc
- Giá bán*         ← Bắt buộc
- Loại sản phẩm*   ← Bắt buộc
- Mô tả            ← Không bắt buộc

→ Không thể lưu nếu thiếu trường bắt buộc
→ Hiển thị: "Vui lòng điền đầy đủ thông tin"
```

**2. Ràng buộc logic nghiệp vụ**

```
Rule 1: Giá bán phải > Giá nhập
- Giá nhập: 3,000,000 VNĐ
- Giá bán: 2,000,000 VNĐ
→ Lỗi: "Giá bán phải lớn hơn giá nhập"

Rule 2: Số lượng bán không được > Tồn kho
- Tồn kho: 5 cái
- Số lượng bán: 10 cái
→ Lỗi: "Không đủ hàng trong kho (còn 5 cái)"

Rule 3: Ngày giao hàng phải >= Ngày đặt hàng
- Ngày đặt: 15/04/2026
- Ngày giao: 10/04/2026
→ Lỗi: "Ngày giao hàng không hợp lệ"
```

**D. Cảnh báo dữ liệu bất thường (Warning)**

**🔧 Odoo Module:** `base` (Cần customize)

**💻 Customize Python cho cảnh báo:**

```python
# Module: data_warning
from odoo import models, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        """Cảnh báo trước khi xác nhận đơn hàng"""
        warnings = []
        
        # Kiểm tra đơn hàng không có sản phẩm
        if not self.order_line:
            raise UserError("⚠️ Đơn hàng không có sản phẩm!")
        
        # Kiểm tra giá bán = 0
        for line in self.order_line:
            if line.price_unit == 0:
                warnings.append(f"⚠️ Sản phẩm '{line.product_id.name}' có giá = 0")
            
            # Kiểm tra giảm giá > 50%
            if line.discount > 50:
                warnings.append(
                    f"⚠️ Sản phẩm '{line.product_id.name}' "
                    f"giảm giá {line.discount}% (>50%)"
                )
        
        # Kiểm tra khách hàng không có SĐT
        if not self.partner_id.phone and not self.partner_id.mobile:
            warnings.append(f"⚠️ Khách hàng '{self.partner_id.name}' không có số điện thoại")
        
        # Hiển thị cảnh báo nếu có
        if warnings:
            warning_msg = "\n".join(warnings)
            warning_msg += "\n\nBạn có chắc chắn muốn tiếp tục?"
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order.warning.wizard',
                'view_mode': 'form',
                'target': 'new',
                'context': {
                    'default_warning_message': warning_msg,
                    'default_order_id': self.id
                }
            }
        
        return super().action_confirm()
```

**Cảnh báo:**

```
Cảnh báo khi:
⚠️ Giá bán = 0 hoặc quá thấp
⚠️ Số lượng = 0
⚠️ Khách hàng không có số điện thoại
⚠️ Đơn hàng không có sản phẩm
⚠️ Giảm giá > 50%

→ Cho phép lưu nhưng hiển thị cảnh báo
→ Nhân viên phải xác nhận: "Tôi chắc chắn muốn tiếp tục"
```

**E. Chuẩn hóa dữ liệu tự động**

**🔧 Odoo Module:** `base` (Cần customize)

**💻 Customize Python cho chuẩn hóa dữ liệu:**

```python
# Module: data_normalization
from odoo import models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        """Chuẩn hóa dữ liệu khi tạo khách hàng"""
        vals = self._normalize_data(vals)
        return super().create(vals)

    def write(self, vals):
        """Chuẩn hóa dữ liệu khi cập nhật"""
        vals = self._normalize_data(vals)
        return super().write(vals)

    def _normalize_data(self, vals):
        """Chuẩn hóa tên, số điện thoại"""
        # 1. Viết hoa chữ cái đầu
        if vals.get('name'):
            vals['name'] = vals['name'].title().strip()
        
        # 2. Xóa khoảng trắng thừa
        for field in ['name', 'street', 'city']:
            if vals.get(field):
                vals[field] = ' '.join(vals[field].split())
        
        # 3. Format số điện thoại (loại bỏ ký tự đặc biệt)
        if vals.get('phone'):
            vals['phone'] = ''.join(filter(str.isdigit, vals['phone']))
        if vals.get('mobile'):
            vals['mobile'] = ''.join(filter(str.isdigit, vals['mobile']))
        
        return vals

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, vals):
        """Chuẩn hóa tên sản phẩm"""
        if vals.get('name'):
            # Xóa khoảng trắng thừa
            vals['name'] = ' '.join(vals['name'].split())
        return super().create(vals)
```

**Ví dụ:**

```
1. Tự động viết hoa chữ cái đầu
   Nhập: "nguyễn văn a"
   Lưu: "Nguyễn Văn A"

2. Tự động xóa khoảng trắng thừa
   Nhập: "Váy  cưới   A"
   Lưu: "Váy cưới A"

3. Tự động format số điện thoại
   Nhập: "0901234567"
   Hiển thị: "090 123 4567"

4. Tự động format giá tiền
   Nhập: "5000000"
   Hiển thị: "5,000,000 VNĐ"
```

**Lợi ích:**

- ✅ 100% dữ liệu chuẩn hóa, nhất quán
- ✅ Giảm 95% lỗi nhập liệu
- ✅ Dễ dàng tìm kiếm, lọc, báo cáo
- ✅ Tiết kiệm thời gian sửa lỗi sau này

---

### **1.4 Vấn đề: Trùng lặp dữ liệu**

**Pain Point hiện tại:**

- Khách hàng mua nhiều lần nhưng mỗi lần là một khách hàng mới
- Sản phẩm được tạo nhiều lần khi quản lý kho
- Khó quản lý, báo cáo sai

**Giải pháp đề xuất:**

**A. Kiểm tra trùng lặp tự động khi tạo mới**

**🔧 Odoo Module:** `base` (Cần customize)

**💻 Customize Python cho kiểm tra trùng lặp:**

```python
# Module: duplicate_check
from odoo import models, api
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        """Kiểm tra trùng lặp khách hàng theo SĐT"""
        if vals.get('phone') or vals.get('mobile'):
            phone = vals.get('phone') or vals.get('mobile')
            
            # Tìm khách hàng có cùng SĐT
            existing = self.search([
                '|',
                ('phone', '=', phone),
                ('mobile', '=', phone)
            ], limit=1)
            
            if existing:
                # Tính tổng đơn hàng
                order_count = self.env['sale.order'].search_count([
                    ('partner_id', '=', existing.id)
                ])
                total_spent = sum(self.env['sale.order'].search([
                    ('partner_id', '=', existing.id),
                    ('state', 'in', ['sale', 'done'])
                ]).mapped('amount_total'))
                
                raise UserError(
                    f"⚠️ KHÁCH HÀNG ĐÃ TỒN TẠI\n\n"
                    f"Tìm thấy khách hàng:\n"
                    f"• Tên: {existing.name}\n"
                    f"• SĐT: {existing.phone or existing.mobile}\n"
                    f"• Email: {existing.email or 'Chưa có'}\n"
                    f"• Đã mua: {order_count} lần\n"
                    f"• Tổng chi tiêu: {total_spent:,.0f} VNĐ\n\n"
                    f"Vui lòng sử dụng khách hàng có sẵn hoặc kiểm tra lại thông tin."
                )
        
        return super().create(vals)

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, vals):
        """Kiểm tra trùng lặp sản phẩm theo tên"""
        if vals.get('name'):
            # Tìm sản phẩm có tên tương tự (fuzzy search)
            existing = self.search([
                ('name', '=ilike', vals['name'])
            ], limit=5)
            
            if existing:
                product_list = "\n".join([
                    f"• {p.name} (Mã: {p.default_code or 'N/A'}, Giá: {p.list_price:,.0f} VNĐ)"
                    for p in existing
                ])
                
                raise UserError(
                    f"⚠️ SẢN PHẨM TƯƠNG TỰ ĐÃ TỒN TẠI\n\n"
                    f"Tìm thấy sản phẩm:\n{product_list}\n\n"
                    f"Vui lòng kiểm tra lại hoặc sử dụng sản phẩm có sẵn."
                )
        
        return super().create(vals)
```

**1. Kiểm tra khách hàng trùng lặp theo số điện thoại**

```
Tình huống: Nhân viên tạo khách hàng mới

Bước 1: Nhập thông tin khách hàng
┌──────────────────────────────────┐
│ Tên: Nguyễn Văn A                │
│ SĐT: 0901234567                  │
│ Email: nguyenvana@gmail.com      │
└──────────────────────────────────┘

Bước 2: Hệ thống tự động kiểm tra
→ Tìm thấy khách hàng có SĐT: 0901234567

Bước 3: Hiển thị cảnh báo
┌──────────────────────────────────────────────┐
│ ⚠️  KHÁCH HÀNG ĐÃ TỒN TẠI                    │
├──────────────────────────────────────────────┤
│ Tìm thấy khách hàng:                         │
│ • Tên: Nguyễn Văn An                         │
│ • SĐT: 0901234567                            │
│ • Email: an.nguyen@gmail.com                 │
│ • Đã mua: 3 lần                              │
│ • Tổng chi tiêu: 15,000,000 VNĐ              │
│                                              │
│ Bạn có muốn:                                 │
│ [Sử dụng khách hàng này] [Tạo mới]          │
└──────────────────────────────────────────────┘
```

**2. Kiểm tra sản phẩm trùng lặp theo mã SKU/tên**

```
Tình huống: Tạo sản phẩm mới

Nhập: 
- Mã SP: VDC-001
- Tên: Váy cưới cách tân A

Hệ thống kiểm tra:
→ Đã tồn tại sản phẩm VDC-001

Cảnh báo:
┌──────────────────────────────────────────────┐
│ ⚠️  MÃ SẢN PHẨM ĐÃ TỒN TẠI                   │
├──────────────────────────────────────────────┤
│ Sản phẩm VDC-001 đã tồn tại:                 │
│ • Tên: Váy cưới cách tân A                   │
│ • Giá: 5,000,000 VNĐ                         │
│ • Tồn kho: 10 cái                            │
│                                              │
│ [Xem sản phẩm] [Thay đổi mã] [Hủy]          │
└──────────────────────────────────────────────┘
```

**B. Gợi ý thông minh khi nhập liệu (Smart suggestions)**

**🔧 Odoo Module:** `web` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Many2one field có auto-complete
- ✅ Tìm kiếm fuzzy (tìm gần đúng)
- ✅ Hiển thị thông tin bổ sung trong dropdown
- ✅ Tìm theo nhiều trường (tên, SĐT, email, mã)

**1. Auto-complete khi nhập tên khách hàng**

```
Nhân viên đang tạo đơn hàng:

Nhập tên khách: "Nguyễn V..."

Hệ thống gợi ý ngay:
┌──────────────────────────────────────────────┐
│ 🔍 Gợi ý khách hàng:                         │
├──────────────────────────────────────────────┤
│ 1. Nguyễn Văn An - 0901234567               │
│    Đã mua 3 lần | Lần cuối: 01/04/2026      │
│                                              │
│ 2. Nguyễn Văn Anh - 0912345678              │
│    Khách mới | Chưa mua lần nào             │
│                                              │
│ 3. Nguyễn Thị Vân - 0923456789              │
│    Đã mua 1 lần | Lần cuối: 15/03/2026      │
└──────────────────────────────────────────────┘

→ Nhân viên chọn khách hàng có sẵn
→ Không tạo khách hàng trùng
```

**2. Auto-complete khi nhập tên sản phẩm**

```
Nhập tên sản phẩm: "Váy c..."

Gợi ý:
┌──────────────────────────────────────────────┐
│ 🔍 Gợi ý sản phẩm:                           │
├──────────────────────────────────────────────┤
│ 1. Váy cưới cách tân A - VDC-001            │
│    Giá: 5,000,000 VNĐ | Còn: 10 cái         │
│                                              │
│ 2. Váy cưới công chúa B - VCC-002           │
│    Giá: 7,000,000 VNĐ | Còn: 5 cái          │
│                                              │
│ 3. Váy cưới truyền thống C - VCT-003        │
│    Giá: 6,000,000 VNĐ | Hết hàng            │
└──────────────────────────────────────────────┘
```

**C. Công cụ tìm và gộp bản ghi trùng lặp (Merge duplicates)**

**🔧 Odoo Module:** `base` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Deduplicate contacts tool
- ✅ Tự động tìm bản ghi trùng lặp
- ✅ Merge wizard để gộp bản ghi
- ✅ Chuyển toàn bộ dữ liệu liên quan sang bản ghi chính

**1. Tìm kiếm bản ghi trùng lặp**

```
Chức năng: Tìm khách hàng trùng lặp

Hệ thống quét toàn bộ database và tìm:
- Khách hàng có cùng SĐT
- Khách hàng có tên giống nhau (>90%)
- Khách hàng có cùng email

Kết quả:
┌──────────────────────────────────────────────┐
│ 📋 TÌM THẤY 5 NHÓM KHÁCH HÀNG TRÙNG LẶP      │
├──────────────────────────────────────────────┤
│ Nhóm 1: (Cùng SĐT: 0901234567)              │
│ ├─ Nguyễn Văn A (ID: 001)                   │
│ └─ Nguyễn Văn An (ID: 005)                  │
│                                              │
│ Nhóm 2: (Tên giống nhau 95%)                │
│ ├─ Trần Thị B (ID: 010)                     │
│ └─ Tran Thi B (ID: 015)                     │
│                                              │
│ [Xem chi tiết] [Gộp tự động]                │
└──────────────────────────────────────────────┘
```

**2. Gộp bản ghi trùng lặp**

```
Chọn 2 khách hàng trùng lặp:
┌──────────────────────────────────────────────┐
│ GỘP KHÁCH HÀNG                               │
├──────────────────────────────────────────────┤
│ Khách hàng 1 (ID: 001)                       │
│ • Tên: Nguyễn Văn A                          │
│ • SĐT: 0901234567                            │
│ • Email: (trống)                             │
│ • Đơn hàng: 2 đơn                            │
│                                              │
│ Khách hàng 2 (ID: 005)                       │
│ • Tên: Nguyễn Văn An                         │
│ • SĐT: 0901234567                            │
│ • Email: an@gmail.com                        │
│ • Đơn hàng: 1 đơn                            │
│                                              │
│ Sau khi gộp:                                 │
│ • Tên: [○ Nguyễn Văn A  ● Nguyễn Văn An]    │
│ • SĐT: 0901234567                            │
│ • Email: an@gmail.com                        │
│ • Đơn hàng: 3 đơn (gộp cả 2)                 │
│                                              │
│ [Hủy] [Xác nhận gộp]                         │
└──────────────────────────────────────────────┘

Sau khi gộp:
- Giữ lại 1 bản ghi (ID: 001)
- Xóa bản ghi trùng (ID: 005)
- Tất cả đơn hàng của ID: 005 chuyển sang ID: 001
```

**D. Unique constraints (Ràng buộc duy nhất)**

**🔧 Odoo Module:** `product` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Unique constraint cho `default_code` (SKU)
- ✅ Tự động kiểm tra trùng lặp khi tạo/sửa
- ✅ Hiển thị lỗi rõ ràng

**1. Mã sản phẩm (SKU) phải duy nhất**

```
Rule: Không được có 2 sản phẩm cùng mã SKU

Ví dụ:
- Sản phẩm A: VDC-001
- Sản phẩm B: VDC-001 ← Không cho phép

→ Lỗi: "Mã sản phẩm VDC-001 đã tồn tại"
```

**2. Số điện thoại khách hàng nên duy nhất**

```
Rule: Cảnh báo nếu SĐT đã tồn tại (không chặn cứng)

Lý do: Có thể 1 SĐT cho nhiều người (gia đình)
→ Cảnh báo nhưng vẫn cho phép tạo nếu xác nhận
```

**E. Lịch sử và audit log**

**🔧 Odoo Module:** `auditlog` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Tracking changes cho mọi model
- ✅ Ghi lại user, thời gian, giá trị cũ/mới
- ✅ Chatter/Activity log cho từng record
- ✅ Audit trail report

**Cấu hình:**

```
Theo dõi:
- Ai tạo bản ghi này?
- Khi nào tạo?
- Ai sửa lần cuối?
- Sửa những gì?

Ví dụ:
┌──────────────────────────────────────────────┐
│ LỊCH SỬ THAY ĐỔI - Khách hàng #001          │
├──────────────────────────────────────────────┤
│ 01/04/2026 10:00 - Tạo bởi: NV Bán A         │
│ 05/04/2026 14:30 - Sửa SĐT: NV Bán B         │
│   Cũ: 0901234567                             │
│   Mới: 0901234568                            │
│ 10/04/2026 09:15 - Thêm email: NV Bán A      │
└──────────────────────────────────────────────┘

→ Dễ dàng truy vết, tìm nguyên nhân trùng lặp
```

**Lợi ích:**

- ✅ Giảm 95% bản ghi trùng lặp
- ✅ Database sạch, dễ quản lý
- ✅ Báo cáo chính xác (không đếm trùng)
- ✅ Tiết kiệm dung lượng lưu trữ

---

### **1.5 Vấn đề: Mất dữ liệu**

**Pain Point hiện tại:**

- File Excel lưu trên máy tính cá nhân bị lỗi hoặc bị xóa nhầm
- Không có backup
- Rủi ro mất toàn bộ dữ liệu kinh doanh

**Giải pháp đề xuất:**

**A. Lưu trữ tập trung trên server (không phụ thuộc máy cá nhân)**

**🔧 Odoo Module:** `base` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ PostgreSQL database trên server
- ✅ Filestore cho attachments
- ✅ Multi-user access
- ✅ Hỗ trợ cloud deployment (Odoo.sh, AWS, GCP)

**1. Kiến trúc lưu trữ đề xuất**

```
Cách cũ (AS-IS):
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Máy NV Bán  │  │ Máy NV Kho  │  │ Máy Quản lý │
│ Excel riêng │  │ Excel riêng │  │ Excel riêng │
└─────────────┘  └─────────────┘  └─────────────┘
     ↓                ↓                 ↓
  Máy hỏng       Xóa nhầm          Virus
     ↓                ↓                 ↓
  MẤT DỮ LIỆU!   MẤT DỮ LIỆU!     MẤT DỮ LIỆU!

Cách mới (TO-BE):
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Máy NV Bán  │  │ Máy NV Kho  │  │ Máy Quản lý │
│ (Chỉ xem)   │  │ (Chỉ xem)   │  │ (Chỉ xem)   │
└──────┬──────┘  └──────┬──────┘  └──────┬──────┘
       │                │                │
       └────────────────┼────────────────┘
                        ↓
              ┌─────────────────┐
              │  SERVER         │
              │  Database       │
              │  (An toàn)      │
              └─────────────────┘
                        ↓
              ┌─────────────────┐
              │  BACKUP         │
              │  Tự động        │
              └─────────────────┘

→ Dữ liệu lưu trên server, không trên máy cá nhân
→ Máy hỏng → Không mất dữ liệu
```

**2. Lựa chọn server**

**Cloud Server (Đề xuất cho shop nhỏ)**

```
Ưu điểm:
✓ Không cần đầu tư phần cứng
✓ Truy cập từ mọi nơi có internet
✓ Nhà cung cấp lo backup tự động
✓ Bảo mật cao, có chuyên gia quản lý

Nhược điểm:
✗ Phụ thuộc internet
✗ Chi phí hàng tháng

Nhà cung cấp đề xuất:
- AWS (Amazon Web Services)
- Google Cloud
- Microsoft Azure
- Odoo.sh (nếu dùng Odoo)
```



**B. Backup tự động định kỳ**

**🔧 Odoo Module:** `base` + Cron jobs (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Database backup manager
- ✅ Scheduled actions (cron) cho backup tự động
- ✅ Backup to local/S3/FTP
- ✅ Email notification khi backup thành công/thất bại

**💻 Cấu hình Backup (không cần code):**

Odoo có sẵn tính năng backup tự động qua:
- Settings → Database Manager → Backup
- Scheduled Actions → Create backup cron job

**1. Chiến lược backup 3-2-1**

```
Quy tắc 3-2-1:
- 3 bản sao dữ liệu
- 2 phương tiện lưu trữ khác nhau
- 1 bản lưu ở nơi khác (offsite)

Áp dụng:
┌─────────────────────────────────────────┐
│ Bản 1: Database chính trên server       │ ← Đang sử dụng
├─────────────────────────────────────────┤
│ Bản 2: Backup hàng ngày trên ổ cứng     │ ← Cùng server
├─────────────────────────────────────────┤
│ Bản 3: Backup hàng tuần lên cloud       │ ← Offsite
└─────────────────────────────────────────┘
```

**2. Lịch backup tự động**

```
Backup hàng ngày (Daily):
- Thời gian: 2:00 AM (lúc không có người dùng)
- Nội dung: Toàn bộ database
- Lưu trữ: 30 ngày gần nhất
- Vị trí: Ổ cứng thứ 2 trên server

Backup hàng tuần (Weekly):
- Thời gian: Chủ nhật 3:00 AM
- Nội dung: Toàn bộ database + files đính kèm
- Lưu trữ: 12 tuần gần nhất
- Vị trí: Cloud storage (Google Drive, Dropbox,...)

Backup hàng tháng (Monthly):
- Thời gian: Ngày 1 hàng tháng 4:00 AM
- Nội dung: Toàn bộ hệ thống
- Lưu trữ: 12 tháng gần nhất
- Vị trí: Ổ cứng ngoài + Cloud

Backup trước khi nâng cấp:
- Thời gian: Trước mỗi lần update hệ thống
- Nội dung: Snapshot toàn bộ
- Lưu trữ: Vĩnh viễn (hoặc ít nhất 1 năm)
```

**3. Thông báo kết quả backup**

```
Email tự động gửi cho quản lý:

Tiêu đề: ✅ Backup thành công - 04/04/2026

Nội dung:
┌──────────────────────────────────────────┐
│ BÁO CÁO BACKUP HÀNG NGÀY                 │
├──────────────────────────────────────────┤
│ Thời gian: 04/04/2026 02:00 AM           │
│ Trạng thái: Thành công ✓                 │
│ Dung lượng: 2.5 GB                       │
│ Thời gian backup: 5 phút                 │
│ Vị trí: /backup/daily/2026-04-04.sql    │
│                                          │
│ Thống kê:                                │
│ - Khách hàng: 1,250 bản ghi             │
│ - Sản phẩm: 350 bản ghi                 │
│ - Đơn hàng: 5,420 bản ghi               │
│                                          │
│ Backup tiếp theo: 05/04/2026 02:00 AM    │
└──────────────────────────────────────────┘

Nếu backup thất bại:
Tiêu đề: ❌ Backup thất bại - 04/04/2026
→ Gửi SMS + Email khẩn cấp cho quản lý
→ Cần xử lý ngay
```

**C. Khôi phục dữ liệu khi cần (Restore)**

**🔧 Odoo Module:** `base` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Database restore từ backup file
- ✅ Duplicate database để test restore
- ✅ Archive/Unarchive records (soft delete)

**1. Khôi phục toàn bộ hệ thống**

```
Tình huống: Server bị hỏng hoàn toàn

Quy trình:
1. Chuẩn bị server mới
2. Cài đặt hệ điều hành + phần mềm
3. Restore database từ backup gần nhất
4. Kiểm tra dữ liệu
5. Đưa hệ thống vào hoạt động

Thời gian: 2-4 giờ
Mất dữ liệu: Tối đa 1 ngày (từ lần backup cuối)
```

**2. Khôi phục dữ liệu bị xóa nhầm**

```
Tình huống: Nhân viên xóa nhầm 1 khách hàng

Quy trình:
1. Xác định thời điểm xóa
2. Tìm backup trước thời điểm đó
3. Restore chỉ bản ghi bị xóa (không restore toàn bộ)
4. Kiểm tra và xác nhận

Thời gian: 15-30 phút
Mất dữ liệu: Không (khôi phục chính xác)
```

**3. Khôi phục về thời điểm cụ thể (Point-in-time recovery)**

```
Tình huống: Phát hiện lỗi dữ liệu từ 3 ngày trước

Quy trình:
1. Xác định thời điểm cần khôi phục (VD: 01/04/2026 10:00 AM)
2. Restore backup ngày 01/04/2026
3. So sánh dữ liệu cũ vs mới
4. Chọn dữ liệu đúng để giữ lại

Thời gian: 1-2 giờ
```

**D. Lịch sử thay đổi và audit log**

**🔧 Odoo Module:** `auditlog`, `mail` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Chatter (message & activity log)
- ✅ Auditlog module (track all changes)
- ✅ Create/Write user & date tracking
- ✅ Archived records history

**1. Theo dõi mọi thay đổi dữ liệu**

```
Hệ thống tự động ghi lại:
- Ai thay đổi?
- Thay đổi gì?
- Khi nào?
- Giá trị cũ là gì?
- Giá trị mới là gì?

Ví dụ:
┌──────────────────────────────────────────────┐
│ LỊCH SỬ THAY ĐỔI - Đơn hàng #SO001          │
├──────────────────────────────────────────────┤
│ 01/04/2026 10:00 - Tạo đơn                   │
│   Người tạo: Nguyễn Văn A (NV Bán)           │
│   Khách hàng: Trần Thị B                     │
│   Tổng tiền: 5,000,000 VNĐ                   │
│                                              │
│ 01/04/2026 10:15 - Sửa số lượng              │
│   Người sửa: Nguyễn Văn A (NV Bán)           │
│   Cũ: 1 cái                                  │
│   Mới: 2 cái                                 │
│   Tổng tiền: 5,000,000 → 10,000,000 VNĐ      │
│                                              │
│ 01/04/2026 14:30 - Xác nhận đơn              │
│   Người xác nhận: Trần Văn C (Quản lý)       │
│   Trạng thái: Quotation → Sale Order         │
│                                              │
│ 02/04/2026 09:00 - Xóa đơn                   │
│   Người xóa: Nguyễn Văn A (NV Bán)           │
│   Lý do: Khách hủy                           │
└──────────────────────────────────────────────┘

→ Có thể khôi phục chính xác từng bước
```

**2. Soft delete (Xóa mềm)**

```
Thay vì xóa hẳn → Chỉ đánh dấu "đã xóa"

Cách hoạt động:
- Khi xóa: Không xóa khỏi database, chỉ set flag "deleted = true"
- Khi xem: Không hiển thị các bản ghi đã xóa
- Khi cần: Có thể khôi phục lại (undelete)

Ví dụ:
Khách hàng #001:
- Tên: Nguyễn Văn A
- SĐT: 0901234567
- Deleted: false ← Đang hoạt động

Nhân viên xóa nhầm → Deleted: true ← Ẩn đi

Quản lý khôi phục → Deleted: false ← Hiển thị lại

→ An toàn, không mất dữ liệu vĩnh viễn
```

**E. Bảo mật và phân quyền**

**🔧 Odoo Module:** `base`, `auth_totp` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Role-based access control (RBAC)
- ✅ Record rules cho phân quyền chi tiết
- ✅ SSL/TLS encryption
- ✅ Two-factor authentication (2FA)
- ✅ Password encryption

**1. Phân quyền xóa dữ liệu**

```
Quy tắc:
- Nhân viên thường: KHÔNG được xóa
- Quản lý: Được xóa (có audit log)
- Admin: Được xóa vĩnh viễn (cần xác nhận 2 lần)

Ví dụ:
NV Bán muốn xóa khách hàng:
→ Hệ thống: "Bạn không có quyền xóa. Vui lòng liên hệ quản lý"

Quản lý muốn xóa khách hàng:
→ Hệ thống: "Xác nhận xóa? [Có] [Không]"
→ Sau khi xóa: Ghi log "Quản lý X đã xóa khách hàng Y lúc Z"
```

**2. Mã hóa dữ liệu (Encryption)**

```
Mã hóa khi lưu trữ:
- Database được mã hóa
- Backup files được mã hóa
- Chỉ có key mới giải mã được

Mã hóa khi truyền tải:
- Kết nối HTTPS (SSL/TLS)
- Dữ liệu truyền đi được mã hóa
- Tránh bị đánh cắp giữa đường
```

**3. Xác thực 2 lớp (2FA) cho tài khoản quan trọng**

```
Đăng nhập tài khoản quản lý:
1. Nhập username + password
2. Nhập mã OTP từ điện thoại (Google Authenticator)
3. Mới đăng nhập được

→ Tăng bảo mật, tránh bị hack
```

**Lợi ích:**

- ✅ 99.9% an toàn dữ liệu
- ✅ Khôi phục nhanh chóng khi có sự cố
- ✅ Theo dõi được mọi thay đổi
- ✅ Yên tâm kinh doanh, không lo mất dữ liệu

---

## **🎯 2. GIẢI PHÁP CHO VẤN ĐỀ VỀ QUY TRÌNH**

### **2.1 Vấn đề: Không có workflow tự động**

**Pain Point hiện tại:**

- Nhân viên bán hàng quên báo nhân viên kho đóng hàng
- Nhân viên kho quên báo đã tìm thấy sản phẩm trong kho
- Khách hàng phải chờ lâu, không biết tình trạng đơn hàng

**Giải pháp đề xuất:**

**A. Workflow tự động theo trạng thái đơn hàng**

**🔧 Odoo Module:** `sale`, `stock`, `mail` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Sale order workflow (Quotation → Sale Order → Done)
- ✅ Delivery order workflow (Ready → Done)
- ✅ Automated actions (khi đổi trạng thái → tự động thực hiện hành động)
- ✅ Activity scheduling (tạo task tự động cho user)
- ✅ Email/SMS notifications tự động

**1. Quy trình bán hàng tự động (Sales Order Workflow)**

```
BƯỚC 1: TẠO BÁO GIÁ (Quotation)
┌──────────────────────────────────────────┐
│ Nhân viên bán hàng:                      │
│ - Tạo báo giá cho khách                  │
│ - Chọn sản phẩm, số lượng                │
│ - Hệ thống tự động tính giá              │
│                                          │
│ Trạng thái: QUOTATION                    │
│ Màu: Xám                                 │
└──────────────────────────────────────────┘
                ↓
        [Khách đồng ý]
                ↓
BƯỚC 2: XÁC NHẬN ĐƠN HÀNG (Sale Order)
┌──────────────────────────────────────────┐
│ Nhân viên click "Xác nhận"               │
│                                          │
│ Hệ thống TỰ ĐỘNG:                        │
│ ✓ Chuyển trạng thái → SALE ORDER         │
│ ✓ Tạo phiếu giao hàng (Delivery Order)   │
│ ✓ Gửi thông báo cho kho                  │
│ ✓ Gửi email xác nhận cho khách           │
│ ✓ Khóa tồn kho (reserved)                │
│                                          │
│ Trạng thái: SALE ORDER                   │
│ Màu: Xanh dương                          │
└──────────────────────────────────────────┘
                ↓
        [Tự động tạo]
                ↓
BƯỚC 3: CHUẨN BỊ HÀNG (Picking)
┌──────────────────────────────────────────┐
│ Nhân viên kho nhận thông báo:            │
│ "Đơn hàng #SO001 cần đóng gói"           │
│                                          │
│ Nhân viên kho:                           │
│ - Xem danh sách sản phẩm cần lấy         │
│ - Xem vị trí kho của từng sản phẩm       │
│ - Quét barcode để xác nhận lấy hàng      │
│ - Click "Validate" khi đóng gói xong     │
│                                          │
│ Hệ thống TỰ ĐỘNG:                        │
│ ✓ Trừ tồn kho                            │
│ ✓ Gửi thông báo cho NV bán hàng          │
│ ✓ Cập nhật trạng thái đơn hàng           │
│                                          │
│ Trạng thái: READY TO SHIP                │
│ Màu: Xanh lá                             │
└──────────────────────────────────────────┘
                ↓
        [Giao hàng]
                ↓
BƯỚC 4: HOÀN THÀNH (Done)
┌──────────────────────────────────────────┐
│ Shipper/NV giao hàng:                    │
│ - Click "Đã giao hàng"                   │
│                                          │
│ Hệ thống TỰ ĐỘNG:                        │
│ ✓ Chuyển trạng thái → DONE               │
│ ✓ Gửi SMS cảm ơn khách hàng              │
│ ✓ Tạo hóa đơn (nếu chưa thanh toán)     │
│ ✓ Cập nhật doanh thu                     │
│ ✓ Tạo điểm thưởng cho khách (nếu có)     │
│                                          │
│ Trạng thái: DONE                         │
│ Màu: Xanh đậm                            │
└──────────────────────────────────────────┘
```

**2. Kanban Board để theo dõi trực quan**

```
┌─────────────┬─────────────┬─────────────┬─────────────┬─────────────┐
│  QUOTATION  │ SALE ORDER  │   PICKING   │   READY     │    DONE     │
│   (Báo giá) │ (Đã xác nhận│  (Đang đóng)│ (Sẵn sàng)  │ (Hoàn thành)│
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤
│             │             │             │             │             │
│ ┌─────────┐ │ ┌─────────┐ │ ┌─────────┐ │ ┌─────────┐ │ ┌─────────┐ │
│ │ SO001   │ │ │ SO003   │ │ │ SO005   │ │ │ SO007   │ │ │ SO009   │ │
│ │ Nguyễn A│ │ │ Trần B  │ │ │ Lê C    │ │ │ Phạm D  │ │ │ Hoàng E │ │
│ │ 5tr VNĐ │ │ │ 10tr VNĐ│ │ │ 7tr VNĐ │ │ │ 8tr VNĐ │ │ │ 6tr VNĐ │ │
│ └─────────┘ │ └─────────┘ │ └─────────┘ │ └─────────┘ │ └─────────┘ │
│             │             │             │             │             │
│ ┌─────────┐ │ ┌─────────┐ │ ┌─────────┐ │             │ ┌─────────┐ │
│ │ SO002   │ │ │ SO004   │ │ │ SO006   │ │             │ │ SO010   │ │
│ │ Võ F    │ │ │ Đỗ G    │ │ │ Bùi H   │ │             │ │ Mai I   │ │
│ │ 12tr VNĐ│ │ │ 9tr VNĐ │ │ │ 11tr VNĐ│ │             │ │ 7tr VNĐ │ │
│ └─────────┘ │ └─────────┘ │ └─────────┘ │             │ └─────────┘ │
│             │             │             │             │             │
│             │             │             │             │             │
│ [+ Thêm]    │ [+ Thêm]    │             │             │             │
└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┘

→ Kéo thả card để chuyển trạng thái
→ Nhìn 1 cái biết ngay tình trạng tất cả đơn hàng
→ Lọc theo nhân viên, ngày, khách hàng,...
```

**3. Automated Actions (Hành động tự động)**

```
Rule 1: Khi xác nhận đơn hàng
┌──────────────────────────────────────────┐
│ TRIGGER: Trạng thái = "Sale Order"       │
│                                          │
│ ACTIONS:                                 │
│ 1. Tạo Delivery Order                    │
│ 2. Gửi email cho khách:                  │
│    "Đơn hàng #SO001 đã được xác nhận"    │
│ 3. Gửi thông báo cho kho:                │
│    "Đơn hàng mới cần đóng gói"           │
│ 4. Khóa tồn kho (reserved)               │
│ 5. Tạo task cho shipper (nếu cần)        │
└──────────────────────────────────────────┘

Rule 2: Khi đóng gói xong
┌──────────────────────────────────────────┐
│ TRIGGER: Delivery Order = "Done"         │
│                                          │
│ ACTIONS:                                 │
│ 1. Trừ tồn kho                           │
│ 2. Gửi thông báo cho NV bán hàng:        │
│    "Đơn #SO001 đã sẵn sàng giao"         │
│ 3. Gửi SMS cho khách:                    │
│    "Đơn hàng đang được giao"             │
│ 4. Cập nhật trạng thái đơn hàng          │
└──────────────────────────────────────────┘

Rule 3: Khi giao hàng thành công
┌──────────────────────────────────────────┐
│ TRIGGER: Trạng thái = "Done"             │
│                                          │
│ ACTIONS:                                 │
│ 1. Gửi SMS cảm ơn khách:                 │
│    "Cảm ơn bạn đã mua hàng!"             │
│ 2. Tạo hóa đơn (nếu chưa thanh toán)     │
│ 3. Cộng điểm thưởng cho khách            │
│ 4. Lên lịch chăm sóc sau bán (7 ngày)    │
│ 5. Cập nhật báo cáo doanh thu            │
└──────────────────────────────────────────┘

Rule 4: Cảnh báo đơn hàng quá hạn
┌──────────────────────────────────────────┐
│ TRIGGER: Đơn hàng > 24h chưa xử lý       │
│                                          │
│ ACTIONS:                                 │
│ 1. Gửi email cảnh báo cho quản lý        │
│ 2. Đổi màu card thành đỏ trên Kanban     │
│ 3. Gửi thông báo cho NV phụ trách        │
└──────────────────────────────────────────┘
```

**B. Button chuyển trạng thái nhanh**

```
Giao diện đơn hàng:
┌──────────────────────────────────────────────┐
│ ĐƠN HÀNG #SO001                              │
├──────────────────────────────────────────────┤
│ Khách hàng: Nguyễn Văn A                     │
│ Ngày: 04/04/2026                             │
│ Tổng tiền: 5,000,000 VNĐ                     │
│ Trạng thái: QUOTATION                        │
│                                              │
│ Sản phẩm:                                    │
│ - Váy cưới A × 1 = 5,000,000 VNĐ             │
│                                              │
│ [XÁC NHẬN ĐƠN]  [GỬI EMAIL]  [IN]  [HỦY]    │
└──────────────────────────────────────────────┘

→ Click "XÁC NHẬN ĐƠN" → Tự động chuyển trạng thái + trigger actions
→ Không cần nhập thủ công, không cần nhớ các bước
```

**Lợi ích:**

- ✅ Giảm 80% thời gian xử lý đơn hàng
- ✅ Không còn quên bước nào
- ✅ Khách hàng được thông báo liên tục
- ✅ Quản lý nắm được tiến độ real-time

---

### **2.2 Vấn đề: Giao tiếp giữa các bộ phận kém**

**Pain Point hiện tại:**

- Nhân viên không có hệ thống chung, phải liên lạc qua điện thoại hoặc tin nhắn

**Giải pháp đề xuất:**

**🔧 Odoo Module:** `mail`, `project` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Chatter (comment thread trên mỗi record)
- ✅ Internal notes & mentions (@user)
- ✅ Activity scheduling (assign task)
- ✅ Email integration
- ✅ Real-time notifications
- Trong giờ cao điểm, nhiều tin nhắn bị trôi hoặc bị bỏ sót
- Không có lịch sử giao tiếp, khó truy vết

**Giải pháp đề xuất:**

**A. Hệ thống chat nội bộ tích hợp (Internal Messaging)**

**1. Chatter trên mỗi đơn hàng/sản phẩm/khách hàng**

```
Giao diện đơn hàng #SO001:
┌──────────────────────────────────────────────┐
│ ĐƠN HÀNG #SO001 - Nguyễn Văn A              │
├──────────────────────────────────────────────┤
│ [Thông tin đơn hàng...]                      │
│                                              │
├──────────────────────────────────────────────┤
│ 💬 CHATTER (Thảo luận)                       │
├──────────────────────────────────────────────┤
│                                              │
│ 10:00 - NV Bán A:                            │
│ @NV_Kho_B Anh kiểm tra giúp em sản phẩm      │
│ "Váy cưới A" còn hàng không ạ?               │
│                                              │
│ 10:05 - NV Kho B:                            │
│ Em check rồi, còn 10 cái ở kệ A1 nhé!        │
│                                              │
│ 10:10 - NV Bán A:                            │
│ Cảm ơn anh! Em xác nhận đơn cho khách luôn.  │
│                                              │
│ 10:15 - HỆ THỐNG:                            │
│ 🤖 Đơn hàng đã được xác nhận bởi NV Bán A    │
│                                              │
│ 10:20 - NV Kho B:                            │
│ Em đã đóng gói xong, sẵn sàng giao!          │
│ 📎 [Ảnh hàng đã đóng gói]                    │
│                                              │
├──────────────────────────────────────────────┤
│ Nhập tin nhắn...                             │
│ [@] [📎] [😊]                     [GỬI]      │
└──────────────────────────────────────────────┘

Tính năng:
✓ Tag người (@username) → Người đó nhận thông báo
✓ Đính kèm file, ảnh
✓ Emoji
✓ Lịch sử đầy đủ, không bị mất
✓ Tìm kiếm tin nhắn
```

**2. Channels (Kênh chat nhóm)**

```
Danh sách channels:
┌──────────────────────────────────────────┐
│ 📢 CHANNELS                              │
├──────────────────────────────────────────┤
│ # general (50 người)                     │
│   Thảo luận chung                        │
│                                          │
│ # sales (10 người)                       │
│   Team bán hàng                          │
│                                          │
│ # warehouse (5 người)                    │
│   Team kho                               │
│                                          │
│ # urgent (Tất cả)                        │
│   Vấn đề khẩn cấp                        │
│                                          │
│ [+ Tạo channel mới]                      │
└──────────────────────────────────────────┘

Ví dụ chat trong #sales:
┌──────────────────────────────────────────┐
│ # sales                                  │
├──────────────────────────────────────────┤
│ 09:00 - Quản lý:                         │
│ Chào team! Hôm nay có chương trình giảm  │
│ giá 10% cho váy cưới cách tân nhé!       │
│                                          │
│ 09:05 - NV Bán A:                        │
│ Dạ em nhận được ạ! Áp dụng đến khi nào?  │
│                                          │
│ 09:10 - Quản lý:                         │
│ Đến hết tuần này (10/04/2026)            │
│                                          │
│ 14:30 - NV Bán B:                        │
│ Mọi người có khách hỏi về váy cưới công  │
│ chúa size XL không? Em hết hàng rồi.     │
│                                          │
│ 14:35 - NV Bán C:                        │
│ Em còn 1 cái, nếu cần em chuyển sang!    │
└──────────────────────────────────────────┘
```

**3. Direct Messages (Tin nhắn riêng)**

```
┌──────────────────────────────────────────┐
│ 💬 DIRECT MESSAGES                       │
├──────────────────────────────────────────┤
│ 🟢 NV Kho B (Online)                     │
│ 🟡 Quản lý (Away)                        │
│ 🔴 NV Bán C (Offline)                    │
│ 🟢 Kế toán (Online)                      │
└──────────────────────────────────────────┘

→ Chat 1-1 riêng tư
→ Thấy trạng thái online/offline
```

**B. Activities & Tasks (Công việc và nhắc nhở)**

**1. Tạo task cho người khác**

```
Trên đơn hàng #SO001:
┌──────────────────────────────────────────┐
│ [Lên lịch công việc]                     │
├──────────────────────────────────────────┤
│ Loại: [▼ To Do]                          │
│ Tiêu đề: Đóng gói đơn hàng #SO001        │
│ Giao cho: [▼ NV Kho B]                   │
│ Hạn: 04/04/2026 15:00                    │
│ Mô tả: Ưu tiên đóng gói, khách cần gấp   │
│                                          │
│ [Hủy]  [Lưu]                             │
└──────────────────────────────────────────┘

→ NV Kho B nhận thông báo ngay
→ Task hiển thị trong danh sách công việc của NV Kho B
```

**2. Dashboard công việc cá nhân**

```
Màn hình của NV Kho B:
┌──────────────────────────────────────────┐
│ CÔNG VIỆC CỦA TÔI                        │
├──────────────────────────────────────────┤
│ 🔴 QUÁ HẠN (1)                           │
│ ├─ Kiểm kho khu A (Hạn: 03/04)           │
│                                          │
│ 🟡 HÔM NAY (3)                           │
│ ├─ Đóng gói #SO001 (15:00) 🔥 Gấp       │
│ ├─ Đóng gói #SO003 (16:00)               │
│ └─ Nhập hàng mới (17:00)                 │
│                                          │
│ 🟢 TUẦN NÀY (5)                          │
│ ├─ Kiểm kho khu B (05/04)                │
│ ├─ Sắp xếp lại kệ C (06/04)              │
│ └─ ...                                   │
└──────────────────────────────────────────┘

→ Nhìn 1 cái biết ngay phải làm gì
→ Ưu tiên công việc gấp
```

**3. Nhắc nhở tự động**

```
Hệ thống tự động nhắc:
- 1 giờ trước deadline: Thông báo pop-up
- Khi quá hạn: Email + SMS cho người được giao
- Khi quá hạn 24h: Thông báo cho quản lý

Ví dụ:
┌──────────────────────────────────────────┐
│ 🔔 NHẮC NHỞ                              │
├──────────────────────────────────────────┤
│ Task "Đóng gói #SO001" sẽ đến hạn sau    │
│ 1 giờ nữa (15:00)                        │
│                                          │
│ [Đánh dấu hoàn thành] [Xem chi tiết]     │
└──────────────────────────────────────────┘
```

**C. Thông báo tự động thông minh**

**1. Phân loại thông báo theo mức độ**

```
🔴 KHẨN CẤP (Urgent):
- Đơn hàng quá hạn chưa xử lý
- Sản phẩm hết hàng
- Khách hàng khiếu nại
→ Hiển thị pop-up + âm thanh + email + SMS

🟡 QUAN TRỌNG (Important):
- Đơn hàng mới
- Task được giao
- Tin nhắn được tag @
→ Hiển thị pop-up + âm thanh

🟢 THÔNG TIN (Info):
- Đơn hàng chuyển trạng thái
- Ai đó comment trong chatter
- Cập nhật hệ thống
→ Hiển thị badge đếm số, không làm phiền
```

**2. Trung tâm thông báo**

```
┌──────────────────────────────────────────┐
│ 🔔 THÔNG BÁO (15 chưa đọc)               │
├──────────────────────────────────────────┤
│ [Tất cả] [Chưa đọc] [Đã đọc]            │
├──────────────────────────────────────────┤
│ 🔴 10:00 - Đơn #SO001 quá hạn           │
│    [Xem đơn hàng]                        │
│                                          │
│ 🟡 10:15 - @NV_Kho_B tag bạn trong #SO003│
│    "Anh check giúp em..."                │
│    [Xem tin nhắn]                        │
│                                          │
│ 🟢 10:30 - Đơn #SO005 đã hoàn thành     │
│    [Xem chi tiết]                        │
│                                          │
│ 🟡 11:00 - Task mới: "Kiểm kho khu A"   │
│    Hạn: 05/04/2026                       │
│    [Xem task]                            │
└──────────────────────────────────────────┘

→ Không bỏ sót thông báo nào
→ Xem lại lịch sử thông báo
```

**D. Email notification tự động**

```
Khi không online trên hệ thống:
→ Gửi email tổng hợp thông báo

Ví dụ email:
┌──────────────────────────────────────────┐
│ Tiêu đề: [Hệ thống] Bạn có 5 thông báo   │
│          mới                             │
├──────────────────────────────────────────┤
│ Xin chào NV Kho B,                       │
│                                          │
│ Bạn có 5 thông báo mới:                  │
│                                          │
│ 1. 🔴 Đơn #SO001 quá hạn                │
│    → Xem ngay: [Link]                    │
│                                          │
│ 2. 🟡 @NV_Bán_A tag bạn trong #SO003     │
│    → Trả lời: [Link]                     │
│                                          │
│ 3. 🟡 Task mới: "Đóng gói #SO005"       │
│    Hạn: 04/04/2026 16:00                 │
│    → Xem task: [Link]                    │
│                                          │
│ ...                                      │
│                                          │
│ [Đăng nhập hệ thống]                     │
└──────────────────────────────────────────┘
```

**Lợi ích:**

- ✅ Giao tiếp nhanh, không bị trôi tin nhắn
- ✅ Lịch sử đầy đủ, dễ truy vết
- ✅ Không cần điện thoại, Zalo, Facebook
- ✅ Tất cả tập trung trong 1 hệ thống

---

### **2.3 Vấn đề: Không có thông báo tự động**

**Pain Point hiện tại:**

- Sau khi tạo đơn hàng, nhân viên phải tự nhớ để theo dõi tiến độ
- Phải nhớ báo kho đóng hàng, nhớ gửi SMS cho khách,...
- Dễ quên, bỏ sót

**Giải pháp đề xuất:**

**A. Automated Notifications theo sự kiện**

**🔧 Odoo Module:** `mail`, `sms` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Email templates với dynamic content
- ✅ SMS gateway integration
- ✅ Automated actions (trigger-based)
- ✅ Activity scheduling
- ✅ Notification preferences per user

**1. Thông báo khi tạo đơn hàng**

```
Sự kiện: Nhân viên tạo đơn hàng mới #SO001

Hệ thống TỰ ĐỘNG:
┌──────────────────────────────────────────┐
│ GỬI CHO:                                 │
├──────────────────────────────────────────┤
│ ✓ Nhân viên bán hàng:                    │
│   💬 "Đơn #SO001 đã được tạo thành công" │
│                                          │
│ ✓ Khách hàng:                            │
│   📧 Email: "Cảm ơn bạn đã đặt hàng"     │
│   📱 SMS: "Đơn hàng #SO001 đang xử lý"   │
│                                          │
│ ✓ Quản lý:                               │
│   💬 "Đơn hàng mới: #SO001 - 5tr VNĐ"    │
└──────────────────────────────────────────┘
```

**2. Thông báo khi xác nhận đơn hàng**

```
Sự kiện: Đơn hàng được xác nhận

Hệ thống TỰ ĐỘNG:
┌──────────────────────────────────────────┐
│ GỬI CHO:                                 │
├──────────────────────────────────────────┤
│ ✓ Nhân viên kho:                         │
│   💬 "Đơn #SO001 cần đóng gói"           │
│   📋 Task: "Đóng gói #SO001"             │
│                                          │
│ ✓ Khách hàng:                            │
│   📧 Email: "Đơn hàng đã được xác nhận"  │
│   📱 SMS: "Đơn #SO001 đang chuẩn bị"     │
│                                          │
│ ✓ Shipper (nếu có):                      │
│   💬 "Đơn #SO001 sẽ sẵn sàng lúc 15:00"  │
└──────────────────────────────────────────┘
```

**3. Thông báo khi đóng gói xong**

```
Sự kiện: Nhân viên kho đóng gói xong

Hệ thống TỰ ĐỘNG:
┌──────────────────────────────────────────┐
│ GỬI CHO:                                 │
├──────────────────────────────────────────┤
│ ✓ Nhân viên bán hàng:                    │
│   💬 "Đơn #SO001 đã sẵn sàng giao"       │
│                                          │
│ ✓ Khách hàng:                            │
│   📱 SMS: "Đơn hàng đang được giao đến"  │
│                                          │
│ ✓ Shipper:                               │
│   💬 "Lấy hàng #SO001 tại kho"           │
│   📍 Địa chỉ giao: [Link Google Maps]    │
└──────────────────────────────────────────┘
```

**4. Thông báo khi giao hàng thành công**

```
Sự kiện: Đơn hàng hoàn thành

Hệ thống TỰ ĐỘNG:
┌──────────────────────────────────────────┐
│ GỬI CHO:                                 │
├──────────────────────────────────────────┤
│ ✓ Khách hàng:                            │
│   📱 SMS: "Cảm ơn bạn đã mua hàng!"      │
│   📧 Email: "Đánh giá sản phẩm" + Link   │
│                                          │
│ ✓ Nhân viên bán hàng:                    │
│   💬 "Đơn #SO001 đã hoàn thành"          │
│   💰 "Doanh thu: +5,000,000 VNĐ"         │
│                                          │
│ ✓ Quản lý:                               │
│   📊 Cập nhật dashboard doanh thu        │
└──────────────────────────────────────────┘
```

**B. Scheduled Actions (Hành động định kỳ)**

**1. Báo cáo hàng ngày**

```
Thời gian: Mỗi sáng 8:00 AM

Hệ thống TỰ ĐỘNG:
┌──────────────────────────────────────────┐
│ GỬI EMAIL CHO QUẢN LÝ:                   │
├──────────────────────────────────────────┤
│ Tiêu đề: Báo cáo kinh doanh 03/04/2026   │
│                                          │
│ Nội dung:                                │
│ • Doanh thu hôm qua: 50,000,000 VNĐ      │
│ • Số đơn hàng: 25 đơn                    │
│ • Đơn chưa xử lý: 3 đơn 🔴              │
│ • Sản phẩm sắp hết: 5 sản phẩm 🟡       │
│ • Top bán chạy: Váy cưới A (10 cái)      │
│                                          │
│ [Xem chi tiết]                           │
└──────────────────────────────────────────┘
```

**2. Nhắc nhở đơn hàng chưa xử lý**

```
Thời gian: Mỗi 2 giờ kiểm tra 1 lần

Điều kiện: Đơn hàng > 24h chưa chuyển trạng thái

Hệ thống TỰ ĐỘNG:
┌──────────────────────────────────────────┐
│ GỬI CHO NV PHỤ TRÁCH:                    │
├──────────────────────────────────────────┤
│ 🔴 CẢNH BÁO: Đơn hàng quá hạn            │
│                                          │
│ Đơn #SO001 đã 26 giờ chưa xử lý          │
│ Khách hàng: Nguyễn Văn A                 │
│ SĐT: 0901234567                          │
│                                          │
│ Vui lòng xử lý ngay!                     │
│ [Xem đơn hàng]                           │
└──────────────────────────────────────────┘

Đồng thời:
- Gửi email cho quản lý
- Đổi màu card thành đỏ trên Kanban
- Gửi SMS cho NV phụ trách (nếu không phản hồi)
```

**3. Cảnh báo tồn kho thấp**

```
Thời gian: Mỗi ngày 9:00 AM

Điều kiện: Sản phẩm có tồn kho < mức tối thiểu

Hệ thống TỰ ĐỘNG:
┌──────────────────────────────────────────┐
│ GỬI EMAIL CHO QUẢN LÝ:                   │
├──────────────────────────────────────────┤
│ 🟡 CẢNH BÁO TỒN KHO THẤP                 │
│                                          │
│ 5 sản phẩm sắp hết hàng:                 │
│                                          │
│ 1. Váy cưới A                            │
│    Còn: 2 cái | Tối thiểu: 5 cái        │
│    → Cần nhập: 10 cái                    │
│                                          │
│ 2. Váy cưới B                            │
│    Còn: 1 cái | Tối thiểu: 3 cái        │
│    → Cần nhập: 5 cái                     │
│                                          │
│ ...                                      │
│                                          │
│ [Tạo đơn nhập hàng]                      │
└──────────────────────────────────────────┘
```



**C. Email/SMS Templates tự động**

**1. Template email xác nhận đơn hàng**

```
Tiêu đề: Đơn hàng #SO001 đã được xác nhận

Nội dung:
┌──────────────────────────────────────────┐
│ Xin chào Nguyễn Văn A,                   │
│                                          │
│ Cảm ơn bạn đã đặt hàng tại [Tên shop]!   │
│                                          │
│ Đơn hàng #SO001 đã được xác nhận:        │
│ • Váy cưới A × 1 = 5,000,000 VNĐ         │
│ • Tổng cộng: 5,000,000 VNĐ               │
│                                          │
│ Dự kiến giao hàng: 05/04/2026            │
│ Địa chỉ: [Địa chỉ khách hàng]            │
│                                          │
│ Theo dõi đơn hàng: [Link]                │
│                                          │
│ Hotline: 0909123456                      │
│                                          │
│ Trân trọng,                              │
│ [Tên shop]                               │
└──────────────────────────────────────────┘

→ Tự động điền thông tin đơn hàng
→ Gửi ngay sau khi xác nhận
```

**Lợi ích:**

- ✅ Không cần nhớ, hệ thống tự động
- ✅ Không bỏ sót bất kỳ bước nào
- ✅ Khách hàng luôn được cập nhật
- ✅ Tiết kiệm 90% thời gian giao tiếp

---

## **🎯 3. GIẢI PHÁP CHO VẤN ĐỀ VỀ TỒN KHO**

### **3.1 Vấn đề: Tồn kho không real-time**

**Pain Point hiện tại:**

- Shop bán hàng cả online và offline nhưng tồn kho chỉ được cập nhật trên Excel
- Khi khách mua trực tiếp tại cửa hàng, nhân viên không cập nhật ngay
- Nếu sản phẩm hết mà có khách online mua, nhân viên online vẫn nhận đơn cho sản phẩm đó

**Giải pháp đề xuất:**

**🔧 Odoo Module:** `stock`, `sale_stock`, `website_sale_stock` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Real-time inventory tracking
- ✅ Automatic stock reservation khi confirm sale order
- ✅ Multi-channel inventory sync (POS, Website, Sale)
- ✅ Stock forecasting
- ✅ Low stock alerts

**A. Quản lý tồn kho tập trung real-time**

**1. Single source of truth (Nguồn dữ liệu duy nhất)**

```
Cách cũ (AS-IS):
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Excel NV 1  │  │ Excel NV 2  │  │ Excel NV 3  │
│ Váy A: 10   │  │ Váy A: 8    │  │ Váy A: 12   │
└─────────────┘  └─────────────┘  └─────────────┘
     ↓                ↓                 ↓
  Không biết số nào đúng!

Cách mới (TO-BE):
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ NV Offline  │  │ NV Online   │  │ Website     │
│ (Xem)       │  │ (Xem)       │  │ (Hiển thị)  │
└──────┬──────┘  └──────┬──────┘  └──────┬──────┘
       │                │                │
       └────────────────┼────────────────┘
                        ↓
              ┌─────────────────┐
              │  DATABASE       │
              │  Váy A: 10 cái  │ ← Duy nhất, chính xác
              └─────────────────┘
```

**2. Cập nhật tồn kho tức thời (Real-time sync)**

```
Timeline cập nhật tồn kho:

10:00:00 - Tồn kho ban đầu: Váy A = 10 cái
           ├─ NV Offline thấy: 10 cái
           ├─ NV Online thấy: 10 cái
           └─ Website hiển thị: "Còn hàng"

10:00:05 - Khách mua tại cửa hàng: 2 cái
           └─ NV Offline tạo đơn → Click "Xác nhận"

10:00:06 - Hệ thống TỰ ĐỘNG trừ tồn kho: 10 → 8 cái
           ├─ NV Offline thấy: 8 cái (cập nhật ngay)
           ├─ NV Online thấy: 8 cái (cập nhật ngay)
           └─ Website hiển thị: "Còn 8 sản phẩm"

10:00:10 - Khách online đặt mua: 3 cái
           └─ NV Online tạo đơn → Click "Xác nhận"

10:00:11 - Hệ thống TỰ ĐỘNG trừ tồn kho: 8 → 5 cái
           ├─ NV Offline thấy: 5 cái (cập nhật ngay)
           ├─ NV Online thấy: 5 cái (cập nhật ngay)
           └─ Website hiển thị: "Còn 5 sản phẩm"

→ Tất cả đồng bộ trong < 1 giây
→ Không bao giờ bán hàng không có
```

**3. Stock reservation (Khóa tồn kho)**

```
Tình huống: Khách đang xem hàng, chưa quyết định mua

Giải pháp:
┌──────────────────────────────────────────┐
│ KHÓA TỒN KHO TẠM THỜI                    │
├──────────────────────────────────────────┤
│ Váy A - Tồn kho: 10 cái                  │
│                                          │
│ 10:00 - Khách A đang xem (Báo giá)       │
│ → Khóa: 2 cái (30 phút)                  │
│ → Tồn khả dụng: 10 - 2 = 8 cái           │
│                                          │
│ 10:15 - Khách B đang xem (Báo giá)       │
│ → Khóa: 1 cái (30 phút)                  │
│ → Tồn khả dụng: 8 - 1 = 7 cái            │
│                                          │
│ 10:20 - Khách A xác nhận mua             │
│ → Trừ tồn kho: 10 - 2 = 8 cái            │
│ → Mở khóa: 0 cái                         │
│ → Tồn khả dụng: 8 - 1 = 7 cái            │
│                                          │
│ 10:45 - Khách B hết hạn (30 phút)        │
│ → Tự động mở khóa: 1 cái                 │
│ → Tồn khả dụng: 7 + 1 = 8 cái            │
└──────────────────────────────────────────┘

Công thức:
Tồn khả dụng = Tồn kho thực tế - Đã khóa

→ Tránh bán quá số lượng có sẵn
→ Tự động mở khóa nếu khách không mua
```

**B. Multi-channel inventory (Đồng bộ đa kênh)**

**🔧 Odoo Module:** `stock`, `point_of_sale`, `website_sale`, `sale` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Unified inventory across all channels
- ✅ POS real-time stock update
- ✅ Website real-time stock display
- ✅ Sale order stock reservation

**1. Tích hợp tất cả kênh bán hàng**

```
┌─────────────────────────────────────────┐
│          DATABASE TỒN KHO               │
│          Váy A: 10 cái                  │
└────────────┬────────────────────────────┘
             │
     ┌───────┼───────┬───────┬───────┐
     │       │       │       │       │
┌────▼───┐ ┌─▼────┐ ┌▼────┐ ┌▼────┐ ┌▼────┐
│ Cửa    │ │Website│ │Shopee│ │Lazada│ │Tiki│
│ hàng   │ │       │ │      │ │      │ │     │
└────────┘ └───────┘ └──────┘ └──────┘ └─────┘

→ Bán ở đâu cũng trừ cùng 1 kho
→ Tồn kho luôn đồng bộ
```

**2. Quy tắc phân bổ tồn kho (Stock allocation)**

```
Tình huống: Muốn dành riêng tồn kho cho từng kênh

Ví dụ:
┌──────────────────────────────────────────┐
│ Váy A - Tổng tồn kho: 10 cái             │
├──────────────────────────────────────────┤
│ Phân bổ:                                 │
│ • Cửa hàng: 5 cái (50%)                  │
│ • Website: 3 cái (30%)                   │
│ • Shopee: 2 cái (20%)                    │
│                                          │
│ Khi cửa hàng bán hết 5 cái:              │
│ → Tự động lấy từ kênh khác (nếu cần)     │
│ → Hoặc hiển thị "Hết hàng" tại cửa hàng  │
└──────────────────────────────────────────┘

→ Linh hoạt theo chiến lược kinh doanh
```

**C. Hiển thị tồn kho real-time cho khách hàng**

**🔧 Odoo Module:** `website_sale_stock` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Display available quantity on website
- ✅ "Out of Stock" badge
- ✅ Stock availability by variant (size, color)
- ✅ Prevent purchase when out of stock

**1. Trên website/app**

```
Trang sản phẩm:
┌──────────────────────────────────────────┐
│ VÁY CƯỚI CÁCH TÂN A                      │
├──────────────────────────────────────────┤
│ [Ảnh sản phẩm]                           │
│                                          │
│ Giá: 5,000,000 VNĐ                       │
│                                          │
│ Tình trạng:                              │
│ 🟢 Còn hàng (8 sản phẩm)                 │
│                                          │
│ Size: [○ S] [○ M] [● L] [○ XL]          │
│       Còn 2   Còn 3  Còn 8   Hết hàng    │
│                                          │
│ Số lượng: [- 1 +]                        │
│                                          │
│ [THÊM VÀO GIỎ HÀNG]                      │
└──────────────────────────────────────────┘

Khi chọn size XL (hết hàng):
→ Button "THÊM VÀO GIỎ" bị disable
→ Hiển thị: "Size này tạm hết hàng. Đặt hàng trước?"
```

**2. Cảnh báo khi sắp hết hàng**

```
Khi tồn kho < 5 cái:
┌──────────────────────────────────────────┐
│ VÁY CƯỚI CÁCH TÂN A                      │
├──────────────────────────────────────────┤
│ Giá: 5,000,000 VNĐ                       │
│                                          │
│ Tình trạng:                              │
│ 🟡 Chỉ còn 3 sản phẩm!                   │
│    Đặt hàng ngay kẻo hết!                │
│                                          │
│ [ĐẶT HÀNG NGAY]                          │
└──────────────────────────────────────────┘

→ Tạo cảm giác khan hiếm
→ Thúc đẩy khách mua nhanh
```

**D. Stock moves (Lịch sử biến động tồn kho)**

**🔧 Odoo Module:** `stock` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Stock move history với full traceability
- ✅ Inventory adjustments tracking
- ✅ Stock valuation history
- ✅ Lot/Serial number tracking

```
Xem lịch sử tồn kho của "Váy A":
┌──────────────────────────────────────────┐
│ LỊCH SỬ TỒN KHO - VÁY A                  │
├──────────────────────────────────────────┤
│ 01/04/2026 08:00 - Nhập kho              │
│   Số lượng: +20 cái                      │
│   Tồn kho: 5 → 25 cái                    │
│   Người nhập: NV Kho B                   │
│   Tham chiếu: PO001                      │
│                                          │
│ 01/04/2026 10:00 - Bán hàng              │
│   Số lượng: -2 cái                       │
│   Tồn kho: 25 → 23 cái                   │
│   Đơn hàng: SO001                        │
│                                          │
│ 01/04/2026 14:30 - Bán hàng              │
│   Số lượng: -3 cái                       │
│   Tồn kho: 23 → 20 cái                   │
│   Đơn hàng: SO003                        │
│                                          │
│ 02/04/2026 09:00 - Trả hàng              │
│   Số lượng: +1 cái                       │
│   Tồn kho: 20 → 21 cái                   │
│   Đơn hàng: SO001 (Khách trả)            │
│                                          │
│ 02/04/2026 16:00 - Kiểm kho              │
│   Thực tế: 20 cái                        │
│   Chênh lệch: -1 cái (Thiếu)             │
│   Tồn kho: 21 → 20 cái                   │
│   Người kiểm: NV Kho B                   │
└──────────────────────────────────────────┘

→ Truy vết được mọi biến động
→ Dễ dàng tìm nguyên nhân chênh lệch
```

**Lợi ích:**

- ✅ 100% tồn kho chính xác, real-time
- ✅ Không bao giờ bán hàng không có
- ✅ Đồng bộ tất cả kênh bán hàng
- ✅ Khách hàng biết rõ tình trạng hàng

---

### **3.2 Vấn đề: Không có cảnh báo tồn kho thấp**

**Pain Point hiện tại:**
- Shop không có hệ thống cảnh báo khi sản phẩm sắp hết hàng
- Chỉ khi hết hàng hoàn toàn mới phát hiện ra
- Điều này xảy ra thường xuyên với các sản phẩm bán chạy
- Mất doanh thu vì không có hàng để bán

**Giải pháp đề xuất:**

**🔧 Odoo Module:** `stock`, `purchase_stock` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Reordering rules (Min/Max stock levels)
- ✅ Automated purchase order generation
- ✅ Low stock alerts
- ✅ Stock forecasting
- ✅ Email notifications

**Giải pháp đề xuất:**

**A. Reordering Rules (Quy tắc đặt hàng lại tự động)**

**1. Thiết lập mức tồn kho tối thiểu cho từng sản phẩm**

```
Cấu hình cho mỗi sản phẩm:
┌──────────────────────────────────────────┐
│ SẢN PHẨM: Váy cưới A                     │
├──────────────────────────────────────────┤
│ QUY TẮC TỒN KHO:                         │
│                                          │
│ Tồn kho tối thiểu: [5] cái              │ ← Min quantity
│ Tồn kho tối đa: [20] cái                │ ← Max quantity
│ Số lượng đặt mỗi lần: [15] cái          │ ← Quantity to order
│                                          │
│ Thời gian giao hàng: [7] ngày            │ ← Lead time
│ Nhà cung cấp: [▼ Công ty A]             │
│                                          │
│ Hành động khi < Min:                     │
│ [●] Cảnh báo                             │
│ [○] Tự động tạo đơn mua hàng             │
│ [○] Cảnh báo + Tạo đơn                   │
└──────────────────────────────────────────┘

Cách hoạt động:
1. Tồn kho hiện tại: 10 cái → OK
2. Bán 6 cái → Tồn kho: 4 cái
3. Hệ thống phát hiện: 4 < 5 (Min)
4. Trigger hành động:
   - Gửi cảnh báo cho quản lý
   - Hoặc tự động tạo đơn mua 15 cái
```

**2. Phân loại mức độ cảnh báo**

```
🟢 AN TOÀN (Safe Stock)
Tồn kho >= Mức tối thiểu × 2
Ví dụ: Váy A - Min: 5, Hiện tại: 12
→ Không cần làm gì

🟡 CẦN CHÚ Ý (Low Stock)
Mức tối thiểu < Tồn kho < Mức tối thiểu × 2
Ví dụ: Váy A - Min: 5, Hiện tại: 7
→ Cảnh báo sớm, chuẩn bị nhập hàng

🔴 NGUY HIỂM (Critical Stock)
Tồn kho <= Mức tối thiểu
Ví dụ: Váy A - Min: 5, Hiện tại: 3
→ Cảnh báo khẩn cấp, nhập hàng ngay

⚫ HẾT HÀNG (Out of Stock)
Tồn kho = 0
→ Không thể bán, mất doanh thu
```

**3. Dashboard cảnh báo tồn kho**

```
Màn hình quản lý:
┌──────────────────────────────────────────┐
│ 📊 DASHBOARD TỒN KHO                     │
├──────────────────────────────────────────┤
│ Tổng quan:                               │
│ • 🟢 An toàn: 45 sản phẩm                │
│ • 🟡 Cần chú ý: 8 sản phẩm               │
│ • 🔴 Nguy hiểm: 3 sản phẩm               │
│ • ⚫ Hết hàng: 2 sản phẩm                 │
│                                          │
├──────────────────────────────────────────┤
│ 🔴 NGUY HIỂM - CẦN XỬ LÝ NGAY           │
├──────────────────────────────────────────┤
│ 1. Váy cưới A                            │
│    Còn: 3 cái | Min: 5 cái              │
│    Bán trung bình: 2 cái/ngày           │
│    → Hết hàng sau: 1.5 ngày              │
│    [Đặt hàng ngay]                       │
│                                          │
│ 2. Váy cưới B                            │
│    Còn: 1 cái | Min: 3 cái              │
│    Bán trung bình: 1 cái/ngày           │
│    → Hết hàng sau: 1 ngày                │
│    [Đặt hàng ngay]                       │
│                                          │
│ 3. Phụ kiện C                            │
│    Còn: 2 cái | Min: 5 cái              │
│    Bán trung bình: 3 cái/ngày           │
│    → Hết hàng sau: 0.7 ngày (17 giờ)     │
│    [Đặt hàng ngay] 🔥                    │
│                                          │
├──────────────────────────────────────────┤
│ 🟡 CẦN CHÚ Ý                             │
├──────────────────────────────────────────┤
│ [Xem danh sách 8 sản phẩm]              │
│                                          │
├──────────────────────────────────────────┤
│ ⚫ HẾT HÀNG                               │
├──────────────────────────────────────────┤
│ 1. Váy cưới D - Hết từ: 02/04/2026       │
│    Đơn hàng chờ: 3 đơn                   │
│    [Xem đơn hàng]                        │
│                                          │
│ 2. Phụ kiện E - Hết từ: 03/04/2026       │
│    Đơn hàng chờ: 1 đơn                   │
│    [Xem đơn hàng]                        │
└──────────────────────────────────────────┘
```

**B. Automated Alerts (Cảnh báo tự động)**

**1. Email cảnh báo hàng ngày**

```
Thời gian: Mỗi sáng 8:00 AM

Email gửi cho quản lý:
┌──────────────────────────────────────────┐
│ Tiêu đề: 🔴 Cảnh báo tồn kho - 04/04/2026│
├──────────────────────────────────────────┤
│ Xin chào Quản lý,                        │
│                                          │
│ Hệ thống phát hiện 3 sản phẩm cần nhập   │
│ hàng khẩn cấp:                           │
│                                          │
│ 🔴 NGUY HIỂM (3 sản phẩm)                │
│                                          │
│ 1. Váy cưới A                            │
│    • Tồn kho: 3 cái (Min: 5)            │
│    • Tốc độ bán: 2 cái/ngày             │
│    • Dự kiến hết: 1.5 ngày nữa          │
│    • Đề xuất: Nhập 15 cái               │
│    • NCC: Công ty A (Lead time: 7 ngày) │
│    → [Tạo đơn mua hàng]                  │
│                                          │
│ 2. Váy cưới B                            │
│    • Tồn kho: 1 cái (Min: 3)            │
│    • Tốc độ bán: 1 cái/ngày             │
│    • Dự kiến hết: 1 ngày nữa            │
│    • Đề xuất: Nhập 10 cái               │
│    • NCC: Công ty B (Lead time: 5 ngày) │
│    → [Tạo đơn mua hàng]                  │
│                                          │
│ 3. Phụ kiện C                            │
│    • Tồn kho: 2 cái (Min: 5)            │
│    • Tốc độ bán: 3 cái/ngày             │
│    • Dự kiến hết: 17 giờ nữa 🔥         │
│    • Đề xuất: Nhập 20 cái               │
│    • NCC: Công ty C (Lead time: 3 ngày) │
│    → [Tạo đơn mua hàng]                  │
│                                          │
│ ⚫ HẾT HÀNG (2 sản phẩm)                  │
│ • Váy cưới D - 3 đơn hàng đang chờ       │
│ • Phụ kiện E - 1 đơn hàng đang chờ       │
│                                          │
│ [Xem dashboard đầy đủ]                   │
│                                          │
│ Trân trọng,                              │
│ Hệ thống quản lý kho                     │
└──────────────────────────────────────────┘
```

**2. Thông báo real-time khi tồn kho xuống thấp**

```
Khi tồn kho < Min:
┌──────────────────────────────────────────┐
│ 🔔 THÔNG BÁO KHẨN CẤP                    │
├──────────────────────────────────────────┤
│ 🔴 Sản phẩm "Váy cưới A" sắp hết hàng!   │
│                                          │
│ Tồn kho hiện tại: 4 cái                  │
│ Mức tối thiểu: 5 cái                     │
│                                          │
│ Tốc độ bán: 2 cái/ngày                   │
│ Dự kiến hết hàng sau: 2 ngày             │
│                                          │
│ Đề xuất:                                 │
│ • Nhập 15 cái từ Công ty A               │
│ • Thời gian giao: 7 ngày                 │
│                                          │
│ [Tạo đơn mua hàng] [Xem chi tiết] [Đóng] │
└──────────────────────────────────────────┘

→ Pop-up hiển thị ngay trên màn hình
→ Âm thanh cảnh báo (nếu cấu hình)
→ Gửi đồng thời email + SMS
```

**3. SMS cảnh báo khẩn cấp**

```
SMS gửi cho quản lý khi tồn kho = 0:

"[KHẨN CẤP] Sản phẩm 'Váy cưới A' đã HẾT HÀNG!
Có 3 đơn hàng đang chờ.
Vui lòng nhập hàng ngay.
Xem chi tiết: [Link]"

→ Gửi khi hết hàng hoàn toàn
→ Đảm bảo quản lý biết ngay lập tức
```

**C. Phân tích và dự báo tồn kho**

**1. Tính toán tốc độ bán (Sales velocity)**

```
Công thức:
Tốc độ bán = Tổng số lượng bán / Số ngày

Ví dụ:
Váy cưới A:
- 30 ngày qua bán: 60 cái
- Tốc độ bán: 60 / 30 = 2 cái/ngày

Dự báo:
- Tồn kho hiện tại: 10 cái
- Dự kiến hết hàng sau: 10 / 2 = 5 ngày
- Thời gian nhập hàng: 7 ngày
- Kết luận: CẦN NHẬP HÀNG NGAY (vì 7 > 5)

Hiển thị:
┌──────────────────────────────────────────┐
│ Váy cưới A                               │
├──────────────────────────────────────────┤
│ Tồn kho: 10 cái                          │
│ Tốc độ bán: 2 cái/ngày                   │
│ Dự kiến hết: 5 ngày nữa (09/04/2026)     │
│                                          │
│ ⚠️  CẢNH BÁO:                            │
│ Thời gian nhập hàng (7 ngày) > Thời gian │
│ hết hàng (5 ngày). Cần nhập hàng ngay!   │
│                                          │
│ [Đặt hàng ngay]                          │
└──────────────────────────────────────────┘
```

**2. Phân tích theo mùa (Seasonal analysis)**

```
Nhận diện pattern:
┌──────────────────────────────────────────┐
│ PHÂN TÍCH BÁN HÀNG - Váy cưới A          │
├──────────────────────────────────────────┤
│ Tốc độ bán theo tháng:                   │
│                                          │
│ Tháng 1: 1 cái/ngày (Thấp)              │
│ Tháng 2: 1.5 cái/ngày                    │
│ Tháng 3: 2 cái/ngày                      │
│ Tháng 4: 3 cái/ngày (Cao - Mùa cưới)    │
│ Tháng 5: 4 cái/ngày (Cao - Mùa cưới)    │
│ Tháng 6: 2.5 cái/ngày                    │
│ ...                                      │
│                                          │
│ 🔍 NHẬN XÉT:                             │
│ • Tháng 4-5: Mùa cao điểm (mùa cưới)     │
│ • Tháng 1-2: Mùa thấp điểm               │
│                                          │
│ 💡 ĐỀ XUẤT:                              │
│ Hiện tại: Tháng 4 (mùa cao điểm)         │
│ → Nên tăng mức tồn kho tối thiểu         │
│   từ 5 lên 10 cái                        │
│ → Nhập hàng nhiều hơn bình thường        │
└──────────────────────────────────────────┘
```

**3. ABC Analysis (Phân loại sản phẩm theo giá trị)**

```
Phân loại sản phẩm:
┌──────────────────────────────────────────┐
│ ABC ANALYSIS                             │
├──────────────────────────────────────────┤
│ A - Sản phẩm quan trọng nhất (20%)       │
│   • Chiếm 80% doanh thu                  │
│   • Cần giám sát chặt chẽ                │
│   • Luôn đảm bảo có hàng                 │
│   • Mức tồn kho cao                      │
│                                          │
│   Ví dụ:                                 │
│   - Váy cưới A: 50tr/tháng               │
│   - Váy cưới B: 45tr/tháng               │
│   - Váy cưới C: 40tr/tháng               │
│                                          │
│ B - Sản phẩm trung bình (30%)            │
│   • Chiếm 15% doanh thu                  │
│   • Giám sát định kỳ                     │
│   • Mức tồn kho trung bình               │
│                                          │
│ C - Sản phẩm ít quan trọng (50%)         │
│   • Chiếm 5% doanh thu                   │
│   • Giám sát lỏng lẻo                    │
│   • Mức tồn kho thấp                     │
│   • Có thể hết hàng tạm thời             │
└──────────────────────────────────────────┘

Áp dụng:
- Sản phẩm A: Cảnh báo khi < 10 cái
- Sản phẩm B: Cảnh báo khi < 5 cái
- Sản phẩm C: Cảnh báo khi < 2 cái
```

**D. Tự động tạo đơn mua hàng (Auto-procurement)**

**1. Quy trình tự động**

```
Khi tồn kho < Min:
┌──────────────────────────────────────────┐
│ BƯỚC 1: Phát hiện tồn kho thấp           │
│ Váy A: 4 cái < 5 cái (Min)              │
│                                          │
│         ↓                                │
│                                          │
│ BƯỚC 2: Tính toán số lượng cần nhập      │
│ Số lượng = Max - Tồn kho hiện tại        │
│          = 20 - 4 = 16 cái               │
│                                          │
│         ↓                                │
│                                          │
│ BƯỚC 3: Tự động tạo đơn mua hàng         │
│ ┌────────────────────────────────────┐   │
│ │ PURCHASE ORDER #PO001              │   │
│ │ Nhà cung cấp: Công ty A            │   │
│ │ Sản phẩm: Váy cưới A               │   │
│ │ Số lượng: 16 cái                   │   │
│ │ Giá: 3,000,000 VNĐ/cái            │   │
│ │ Tổng: 48,000,000 VNĐ               │   │
│ │ Dự kiến giao: 11/04/2026 (7 ngày)  │   │
│ │                                    │   │
│ │ Trạng thái: DRAFT (Chờ duyệt)      │   │
│ └────────────────────────────────────┘   │
│                                          │
│         ↓                                │
│                                          │
│ BƯỚC 4: Gửi thông báo cho quản lý        │
│ "Đơn mua hàng #PO001 đã được tạo tự động"│
│ "Vui lòng xem xét và phê duyệt"          │
│                                          │
│         ↓                                │
│                                          │
│ BƯỚC 5: Quản lý phê duyệt                │
│ [Phê duyệt] [Sửa] [Hủy]                  │
│                                          │
│         ↓                                │
│                                          │
│ BƯỚC 6: Gửi đơn cho nhà cung cấp         │
│ Email tự động gửi PO cho NCC             │
└──────────────────────────────────────────┘
```

**2. Cấu hình linh hoạt**

```
Tùy chọn cho từng sản phẩm:
┌──────────────────────────────────────────┐
│ REORDERING RULE - Váy cưới A             │
├──────────────────────────────────────────┤
│ Khi tồn kho < Min:                       │
│                                          │
│ Option 1: [○] Chỉ cảnh báo               │
│   → Quản lý tự quyết định                │
│                                          │
│ Option 2: [●] Tạo đơn mua (chờ duyệt)    │
│   → Tạo đơn tự động, quản lý phê duyệt   │
│                                          │
│ Option 3: [○] Tạo đơn mua (tự động gửi)  │
│   → Hoàn toàn tự động, không cần duyệt   │
│   ⚠️  Cẩn thận: Chỉ dùng cho sản phẩm    │
│      tin cậy và NCC uy tín               │
└──────────────────────────────────────────┘

Khuyến nghị:
- Sản phẩm A (quan trọng): Option 2 hoặc 3
- Sản phẩm B (trung bình): Option 2
- Sản phẩm C (ít quan trọng): Option 1
```

**Lợi ích:**
- ✅ Không bao giờ hết hàng đột ngột
- ✅ Tiết kiệm 90% thời gian theo dõi tồn kho
- ✅ Dự báo chính xác, chủ động nhập hàng
- ✅ Tối ưu vốn lưu động (không nhập quá nhiều)

---

### **3.3 Vấn đề: Kiểm kho khó khăn**

**Pain Point hiện tại:**
- Shop phải kiểm kho bằng cách đếm thủ công và đối chiếu với Excel
- Quá trình này tốn nhiều thời gian và dễ xảy ra sai lệch giữa thực tế và dữ liệu
- Không biết nguyên nhân chênh lệch

**Giải pháp đề xuất:**

**A. Inventory Adjustment (Điều chỉnh tồn kho) với Barcode**

**🔧 Odoo Module:** `stock`, `stock_barcode` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Inventory adjustment wizard
- ✅ Barcode scanning cho kiểm kho
- ✅ Mobile app support
- ✅ Automatic discrepancy calculation
- ✅ Inventory valuation adjustment
- ✅ Audit trail

**1. Quy trình kiểm kho truyền thống (AS-IS)**

```
Cách cũ - Thủ công:
┌──────────────────────────────────────────┐
│ BƯỚC 1: In danh sách sản phẩm từ Excel   │
│ Thời gian: 30 phút                       │
│                                          │
│ BƯỚC 2: Đi kiểm kho thực tế              │
│ - Đếm từng sản phẩm                      │
│ - Ghi tay vào giấy                       │
│ Thời gian: 4-6 giờ (cho 200 sản phẩm)   │
│                                          │
│ BƯỚC 3: Nhập lại vào Excel               │
│ - Gõ từng con số                         │
│ - Dễ nhập sai                            │
│ Thời gian: 1-2 giờ                       │
│                                          │
│ BƯỚC 4: So sánh và tìm chênh lệch        │
│ - Dùng công thức Excel                   │
│ - Kiểm tra từng dòng                     │
│ Thời gian: 1 giờ                         │
│                                          │
│ TỔNG THỜI GIAN: 6-9 giờ                  │
│ SAI SÓT: Cao (nhập tay, đếm sai,...)    │
└──────────────────────────────────────────┘
```

**2. Quy trình kiểm kho mới (TO-BE) với Barcode**

```
Cách mới - Tự động:
┌──────────────────────────────────────────┐
│ BƯỚC 1: Tạo phiếu kiểm kho trên hệ thống │
│ - Click "Tạo phiếu kiểm kho"             │
│ - Chọn khu vực cần kiểm (hoặc toàn bộ)   │
│ Thời gian: 1 phút                        │
│                                          │
│ BƯỚC 2: Quét barcode bằng điện thoại     │
│ - Mở app trên điện thoại                 │
│ - Quét barcode sản phẩm                  │
│ - Nhập số lượng thực tế (hoặc tự đếm)    │
│ - Dữ liệu tự động đồng bộ lên server     │
│ Thời gian: 1-2 giờ (cho 200 sản phẩm)   │
│                                          │
│ BƯỚC 3: Hệ thống tự động so sánh         │
│ - Tự động tính chênh lệch                │
│ - Highlight sản phẩm có vấn đề           │
│ Thời gian: Tức thời                      │
│                                          │
│ BƯỚC 4: Xác nhận và cập nhật             │
│ - Review chênh lệch                      │
│ - Click "Xác nhận"                       │
│ - Tồn kho tự động cập nhật               │
│ Thời gian: 15 phút                       │
│                                          │
│ TỔNG THỜI GIAN: 1.5-2.5 giờ              │
│ SAI SÓT: Rất thấp (quét barcode tự động) │
│ TIẾT KIỆM: 70-80% thời gian              │
└──────────────────────────────────────────┘
```

**3. Giao diện kiểm kho trên mobile**

```
App mobile (Android/iOS):
┌──────────────────────────────────────────┐
│ 📱 KIỂM KHO - Khu A                      │
├──────────────────────────────────────────┤
│ Tiến độ: 45/100 sản phẩm (45%)           │
│ [████████░░░░░░░░░░░░]                   │
│                                          │
├──────────────────────────────────────────┤
│ [📷 QUÉT BARCODE]                        │
│                                          │
│ Hoặc tìm kiếm:                           │
│ [🔍 Tìm sản phẩm...]                     │
│                                          │
├──────────────────────────────────────────┤
│ Sản phẩm vừa quét:                       │
│                                          │
│ ┌────────────────────────────────────┐   │
│ │ Váy cưới A - VDC001                │   │
│ │ Vị trí: Khu A / Kệ 1 / Ngăn 3      │   │
│ │                                    │   │
│ │ Tồn kho hệ thống: 10 cái          │   │
│ │ Số lượng thực tế: [____]           │   │
│ │                                    │   │
│ │ [- 1 +]  [Xác nhận]                │   │
│ └────────────────────────────────────┘   │
│                                          │
│ Đã kiểm:                                 │
│ ✓ Váy cưới B - 8 cái (OK)                │
│ ✓ Váy cưới C - 5 cái (OK)                │
│ ⚠️  Phụ kiện D - 3 cái (Chênh -2)        │
│                                          │
│ [Lưu và tiếp tục] [Hoàn thành]           │
└──────────────────────────────────────────┘

Tính năng:
✓ Quét barcode bằng camera
✓ Offline mode (không cần internet)
✓ Tự động đồng bộ khi có mạng
✓ Hiển thị vị trí kho
✓ Tự động tính chênh lệch
```

**B. Cycle Counting (Kiểm kho tuần hoàn)**

**1. Thay vì kiểm kho toàn bộ 1 lần → Kiểm từng phần định kỳ**

```
Chiến lược Cycle Counting:
┌──────────────────────────────────────────┐
│ LỊCH KIỂM KHO TUẦN HOÀN                  │
├──────────────────────────────────────────┤
│ Thứ 2: Kiểm Khu A (20 sản phẩm)          │
│   • Thời gian: 30 phút                   │
│   • Không ảnh hưởng hoạt động            │
│                                          │
│ Thứ 3: Kiểm Khu B (25 sản phẩm)          │
│   • Thời gian: 40 phút                   │
│                                          │
│ Thứ 4: Kiểm Khu C (30 sản phẩm)          │
│   • Thời gian: 45 phút                   │
│                                          │
│ Thứ 5: Kiểm Khu D (25 sản phẩm)          │
│   • Thời gian: 40 phút                   │
│                                          │
│ Thứ 6: Kiểm sản phẩm A (quan trọng)      │
│   • Thời gian: 30 phút                   │
│   • Kiểm kỹ hơn, tần suất cao hơn        │
│                                          │
│ → Mỗi tuần kiểm hết 1 lượt               │
│ → Không cần đóng cửa hàng                │
│ → Phát hiện sai lệch sớm                 │
└──────────────────────────────────────────┘

Lợi ích:
✓ Không cần đóng cửa hàng để kiểm kho
✓ Phát hiện vấn đề sớm (không đợi cuối tháng)
✓ Nhẹ nhàng, không áp lực
✓ Độ chính xác cao hơn (tập trung từng khu)
```

**2. Phân loại tần suất kiểm kho theo ABC**

```
┌──────────────────────────────────────────┐
│ TẦN SUẤT KIỂM KHO                        │
├──────────────────────────────────────────┤
│ Sản phẩm A (Quan trọng nhất):            │
│ • Kiểm: Mỗi tuần                         │
│ • Lý do: Giá trị cao, bán chạy           │
│ • Ví dụ: Váy cưới A, B, C                │
│                                          │
│ Sản phẩm B (Trung bình):                 │
│ • Kiểm: Mỗi 2 tuần                       │
│ • Lý do: Giá trị trung bình              │
│ • Ví dụ: Váy cưới D, E, F                │
│                                          │
│ Sản phẩm C (Ít quan trọng):              │
│ • Kiểm: Mỗi tháng                        │
│ • Lý do: Giá trị thấp, ít bán            │
│ • Ví dụ: Phụ kiện nhỏ                    │
└──────────────────────────────────────────┘

→ Tối ưu thời gian, tập trung vào sản phẩm quan trọng
```

**C. Báo cáo và phân tích chênh lệch**

**1. Báo cáo kiểm kho chi tiết**

```
┌──────────────────────────────────────────┐
│ BÁO CÁO KIỂM KHO - 04/04/2026            │
├──────────────────────────────────────────┤
│ Khu vực: Khu A                           │
│ Người kiểm: NV Kho B                     │
│ Thời gian: 09:00 - 10:30 (1.5 giờ)      │
│                                          │
│ TỔNG QUAN:                               │
│ • Tổng sản phẩm kiểm: 50                 │
│ • Khớp đúng: 45 (90%)                    │
│ • Chênh lệch: 5 (10%)                    │
│   - Thừa: 2 sản phẩm (+3 cái)           │
│   - Thiếu: 3 sản phẩm (-5 cái)          │
│                                          │
│ CHI TIẾT CHÊNH LỆCH:                     │
│                                          │
│ 🔴 THIẾU:                                │
│ 1. Váy cưới A (VDC001)                   │
│    Hệ thống: 10 | Thực tế: 8 | Chênh: -2│
│    Giá trị: -10,000,000 VNĐ              │
│    Nguyên nhân: [▼ Chọn...]              │
│      - Bán mà chưa cập nhật              │
│      - Hỏng/mất                          │
│      - Sai vị trí                        │
│      - Khác                              │
│    Ghi chú: [________________]           │
│                                          │
│ 2. Phụ kiện B (PK002)                    │
│    Hệ thống: 15 | Thực tế: 13 | Chênh: -2│
│    Giá trị: -1,000,000 VNĐ               │
│                                          │
│ 3. Váy cưới C (VDC003)                   │
│    Hệ thống: 5 | Thực tế: 4 | Chênh: -1 │
│    Giá trị: -5,000,000 VNĐ               │
│                                          │
│ 🟢 THỪA:                                 │
│ 1. Váy cưới D (VDC004)                   │
│    Hệ thống: 7 | Thực tế: 9 | Chênh: +2 │
│    Giá trị: +12,000,000 VNĐ              │
│    Nguyên nhân: Trả hàng chưa cập nhật   │
│                                          │
│ 2. Phụ kiện E (PK005)                    │
│    Hệ thống: 20 | Thực tế: 21 | Chênh: +1│
│    Giá trị: +500,000 VNĐ                 │
│                                          │
│ TỔNG GIÁ TRỊ CHÊNH LỆCH: -3,500,000 VNĐ  │
│                                          │
│ [Xác nhận điều chỉnh] [In báo cáo] [Hủy] │
└──────────────────────────────────────────┘
```

**2. Phân tích nguyên nhân chênh lệch**

```
┌──────────────────────────────────────────┐
│ PHÂN TÍCH NGUYÊN NHÂN CHÊNH LỆCH         │
├──────────────────────────────────────────┤
│ Tháng 4/2026:                            │
│                                          │
│ Nguyên nhân THIẾU:                       │
│ 1. Bán chưa cập nhật: 45% (9 trường hợp) │
│    → Giải pháp: Đào tạo NV cập nhật ngay │
│                                          │
│ 2. Hỏng/mất: 30% (6 trường hợp)          │
│    → Giải pháp: Kiểm tra quy trình bảo quản│
│                                          │
│ 3. Sai vị trí: 15% (3 trường hợp)        │
│    → Giải pháp: Dán nhãn rõ ràng hơn     │
│                                          │
│ 4. Khác: 10% (2 trường hợp)              │
│                                          │
│ Nguyên nhân THỪA:                        │
│ 1. Trả hàng chưa cập nhật: 60%           │
│    → Giải pháp: Quy trình trả hàng rõ ràng│
│                                          │
│ 2. Nhập kho chưa cập nhật: 30%           │
│    → Giải pháp: Cập nhật ngay khi nhập   │
│                                          │
│ 3. Đếm sai: 10%                          │
│    → Giải pháp: Kiểm tra lại kỹ hơn      │
│                                          │
│ HÀNH ĐỘNG CẦN LÀM:                       │
│ ☐ Đào tạo nhân viên về quy trình cập nhật│
│ ☐ Cải thiện quy trình bảo quản           │
│ ☐ Dán lại nhãn vị trí kho                │
│ ☐ Review quy trình trả hàng              │
└──────────────────────────────────────────┘
```

**D. Inventory Accuracy (Độ chính xác tồn kho)**

**1. Theo dõi KPI độ chính xác**

```
┌──────────────────────────────────────────┐
│ KPI ĐỘ CHÍNH XÁC TỒN KHO                 │
├──────────────────────────────────────────┤
│ Công thức:                               │
│ Accuracy = (Số SP khớp / Tổng SP) × 100% │
│                                          │
│ Tháng 4/2026:                            │
│ • Tuần 1: 85% (Chưa tốt)                 │
│ • Tuần 2: 88% (Cải thiện)                │
│ • Tuần 3: 92% (Tốt)                      │
│ • Tuần 4: 95% (Rất tốt) ✓                │
│                                          │
│ Mục tiêu: >= 95%                         │
│ Hiện tại: 95% ✓ Đạt mục tiêu             │
│                                          │
│ [Xem chi tiết] [Xuất báo cáo]            │
└──────────────────────────────────────────┘

Benchmark:
• < 90%: Kém, cần cải thiện ngay
• 90-95%: Trung bình
• 95-98%: Tốt
• > 98%: Xuất sắc
```

**2. Dashboard theo dõi**

```
┌──────────────────────────────────────────┐
│ 📊 DASHBOARD KIỂM KHO                    │
├──────────────────────────────────────────┤
│ Độ chính xác: 95% ████████████░░ (Tốt)   │
│                                          │
│ Lịch sử 6 tháng:                         │
│ 100%│                                    │
│  95%│         ●─────●─────●              │
│  90%│     ●───                           │
│  85%│ ●───                               │
│  80%│                                    │
│     └─────────────────────────────────   │
│      T11  T12  T1   T2   T3   T4        │
│                                          │
│ Xu hướng: ↗️ Đang cải thiện               │
│                                          │
│ Lần kiểm gần nhất:                       │
│ • Ngày: 04/04/2026                       │
│ • Khu vực: Khu A                         │
│ • Độ chính xác: 90% (45/50 SP)           │
│ • Chênh lệch: -3,500,000 VNĐ             │
│                                          │
│ Lịch kiểm tiếp theo:                     │
│ • 05/04/2026: Khu B (25 SP)              │
│ • 06/04/2026: Khu C (30 SP)              │
│                                          │
│ [Tạo phiếu kiểm kho mới]                 │
└──────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Tiết kiệm 70-80% thời gian kiểm kho
- ✅ Độ chính xác cao (95%+)
- ✅ Phát hiện vấn đề sớm
- ✅ Không cần đóng cửa hàng
- ✅ Truy vết được nguyên nhân chênh lệch

---

### **3.4 Vấn đề: Không quản lý vị trí kho**

**Pain Point hiện tại:**
- Trong kho, hàng hóa không được sắp xếp theo vị trí cụ thể
- Nhân viên phải tìm sản phẩm bằng cách nhớ vị trí hoặc tìm thủ công
- Khi kho có nhiều hàng, việc tìm kiếm trở nên mất thời gian

**Giải pháp đề xuất:**

**A. Multi-location Inventory (Quản lý kho đa vị trí)**

**🔧 Odoo Module:** `stock` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Multi-location & multi-warehouse
- ✅ Hierarchical location structure (Warehouse > Location > Sublocation)
- ✅ Stock by location tracking
- ✅ Location barcode
- ✅ Picking routes & strategies

**1. Cấu trúc kho phân cấp**

```
Cấu trúc đề xuất cho shop váy cưới:
┌──────────────────────────────────────────┐
│ KHO CHÍNH                                │
├──────────────────────────────────────────┤
│ ├─ KHU A: Váy cưới cách tân              │
│ │  ├─ Kệ A1                              │
│ │  │  ├─ Ngăn 1: Size S                 │
│ │  │  ├─ Ngăn 2: Size M                 │
│ │  │  └─ Ngăn 3: Size L                 │
│ │  ├─ Kệ A2                              │
│ │  │  ├─ Ngăn 1: Size XL                │
│ │  │  └─ Ngăn 2: Size XXL               │
│ │  └─ Kệ A3                              │
│ │                                        │
│ ├─ KHU B: Váy cưới truyền thống          │
│ │  ├─ Kệ B1                              │
│ │  ├─ Kệ B2                              │
│ │  └─ Kệ B3                              │
│ │                                        │
│ ├─ KHU C: Váy cưới công chúa             │
│ │  ├─ Kệ C1                              │
│ │  └─ Kệ C2                              │
│ │                                        │
│ ├─ KHU D: Phụ kiện                       │
│ │  ├─ Kệ D1: Voan                        │
│ │  ├─ Kệ D2: Giày                        │
│ │  └─ Kệ D3: Trang sức                   │
│ │                                        │
│ └─ KHU E: Khu trưng bày (Showroom)       │
│    ├─ Mannequin 1                        │
│    ├─ Mannequin 2                        │
│    └─ Mannequin 3                        │
└──────────────────────────────────────────┘

Trong hệ thống:
Warehouse: Kho chính
  └─ Location: Khu A
      └─ Sublocation: Kệ A1
          └─ Sublocation: Ngăn 1
```

**2. Gán vị trí cho sản phẩm**

```
Thông tin sản phẩm:
┌──────────────────────────────────────────┐
│ SẢN PHẨM: Váy cưới A (Size M)            │
├──────────────────────────────────────────┤
│ Mã: VDC001-M                             │
│ Tồn kho: 10 cái                          │
│                                          │
│ VỊ TRÍ KHO:                              │
│ • Kho chính > Khu A > Kệ A1 > Ngăn 2     │
│ • Số lượng: 8 cái                        │
│                                          │
│ • Kho chính > Khu E > Mannequin 1        │
│ • Số lượng: 2 cái (Trưng bày)            │
│                                          │
│ TỔNG: 10 cái                             │
│                                          │
│ [Chỉnh sửa vị trí] [Xem lịch sử]        │
└──────────────────────────────────────────┘

→ 1 sản phẩm có thể ở nhiều vị trí
→ Hệ thống theo dõi số lượng từng vị trí
```

**B. Picking Optimization (Tối ưu lấy hàng)**

**1. Hiển thị vị trí khi lấy hàng**

```
Đơn hàng #SO001 cần đóng gói:
┌──────────────────────────────────────────┐
│ PHIẾU GIAO HÀNG #DO001                   │
├──────────────────────────────────────────┤
│ Danh sách sản phẩm cần lấy:              │
│                                          │
│ ☐ 1. Váy cưới A (Size M) × 1             │
│    📍 Vị trí: Khu A > Kệ A1 > Ngăn 2     │
│    [Quét barcode để xác nhận]            │
│                                          │
│ ☐ 2. Voan cưới B × 1                     │
│    📍 Vị trí: Khu D > Kệ D1 > Ngăn 1     │
│    [Quét barcode để xác nhận]            │
│                                          │
│ ☐ 3. Giày cưới C (Size 37) × 1           │
│    📍 Vị trí: Khu D > Kệ D2 > Ngăn 3     │
│    [Quét barcode để xác nhận]            │
│                                          │
│ Tiến độ: 0/3 (0%)                        │
│ [░░░░░░░░░░░░░░░░░░░░]                   │
│                                          │
│ [Bắt đầu lấy hàng]                       │
└──────────────────────────────────────────┘

Khi quét barcode:
✓ Sản phẩm 1: Váy cưới A - Đúng! ✓
  Tiến độ: 1/3 (33%)
  
→ Nhân viên biết chính xác phải đi đâu
→ Không tốn thời gian tìm kiếm
```

**2. Đường đi tối ưu (Route optimization)**

```
Hệ thống tự động sắp xếp thứ tự lấy hàng:
┌──────────────────────────────────────────┐
│ ĐƯỜNG ĐI TỐI ƯU                          │
├──────────────────────────────────────────┤
│ Đơn hàng #SO001 có 5 sản phẩm            │
│                                          │
│ Thứ tự lấy hàng:                         │
│ 1. Khu A > Kệ A1 > Ngăn 2 (Váy A)        │
│    ↓ (5m)                                │
│ 2. Khu A > Kệ A3 > Ngăn 1 (Váy B)        │
│    ↓ (10m)                               │
│ 3. Khu B > Kệ B1 > Ngăn 3 (Váy C)        │
│    ↓ (8m)                                │
│ 4. Khu D > Kệ D1 > Ngăn 1 (Voan)         │
│    ↓ (6m)                                │
│ 5. Khu D > Kệ D2 > Ngăn 3 (Giày)         │
│                                          │
│ Tổng quãng đường: 29m                    │
│ Thời gian ước tính: 5 phút               │
│                                          │
│ [Bắt đầu] [Xem bản đồ kho]               │
└──────────────────────────────────────────┘

Nếu không tối ưu:
→ Có thể đi lung tung: A1 → D1 → A3 → D2 → B1
→ Tổng quãng đường: 45m (dài hơn 55%)
→ Lãng phí thời gian
```

**C. Barcode cho vị trí kho**

**1. Dán barcode trên từng vị trí**

```
Vật lý trong kho:
┌──────────────────────────────────────────┐
│ KỆ A1                                    │
├──────────────────────────────────────────┤
│ ┌────────────┐                           │
│ │ NGĂN 1     │ ← Dán barcode: LOC-A1-N1  │
│ │ Size S     │                           │
│ │ [BARCODE]  │                           │
│ └────────────┘                           │
│                                          │
│ ┌────────────┐                           │
│ │ NGĂN 2     │ ← Dán barcode: LOC-A1-N2  │
│ │ Size M     │                           │
│ │ [BARCODE]  │                           │
│ └────────────┘                           │
│                                          │
│ ┌────────────┐                           │
│ │ NGĂN 3     │ ← Dán barcode: LOC-A1-N3  │
│ │ Size L     │                           │
│ │ [BARCODE]  │                           │
│ └────────────┘                           │
└──────────────────────────────────────────┘
```

**2. Quy trình nhập kho với vị trí**

```
Khi nhập hàng mới:
┌──────────────────────────────────────────┐
│ BƯỚC 1: Quét barcode sản phẩm            │
│ Quét: VDC001-M (Váy cưới A - Size M)     │
│ Số lượng: [10] cái                       │
│                                          │
│ BƯỚC 2: Quét barcode vị trí kho          │
│ Quét: LOC-A1-N2 (Khu A > Kệ A1 > Ngăn 2) │
│                                          │
│ BƯỚC 3: Xác nhận                         │
│ ✓ Đã lưu:                                │
│   - Sản phẩm: Váy cưới A (Size M)        │
│   - Số lượng: 10 cái                     │
│   - Vị trí: Khu A > Kệ A1 > Ngăn 2       │
│   - Người nhập: NV Kho B                 │
│   - Thời gian: 04/04/2026 10:00          │
│                                          │
│ [Tiếp tục nhập] [Hoàn thành]             │
└──────────────────────────────────────────┘

→ Không cần nhớ, không cần ghi tay
→ Dữ liệu chính xác 100%
```

**D. Putaway Strategy (Chiến lược sắp xếp hàng)**

**1. Quy tắc sắp xếp tự động**

```
Rule 1: Sản phẩm bán chạy → Vị trí gần cửa
┌──────────────────────────────────────────┐
│ Váy cưới A (Bán 10 cái/tuần)             │
│ → Đặt ở: Khu A > Kệ A1 (Gần cửa nhất)    │
│                                          │
│ Váy cưới Z (Bán 1 cái/tháng)             │
│ → Đặt ở: Khu C > Kệ C3 (Xa, ít dùng)     │
└──────────────────────────────────────────┘

Rule 2: Sản phẩm nặng → Tầng dưới
┌──────────────────────────────────────────┐
│ Giày cưới (Nặng)                         │
│ → Đặt ở: Kệ D2 > Tầng 1 (Dưới cùng)      │
│                                          │
│ Voan cưới (Nhẹ)                          │
│ → Đặt ở: Kệ D1 > Tầng 3 (Trên cao)       │
└──────────────────────────────────────────┘

Rule 3: Sản phẩm cùng loại → Cùng khu
┌──────────────────────────────────────────┐
│ Tất cả váy cưới cách tân → Khu A          │
│ Tất cả váy cưới truyền thống → Khu B     │
│ Tất cả phụ kiện → Khu D                  │
└──────────────────────────────────────────┘
```

**2. Gợi ý vị trí khi nhập hàng**

```
Nhập hàng mới: Váy cưới A (Size M) - 10 cái
┌──────────────────────────────────────────┐
│ GỢI Ý VỊ TRÍ LƯU TRỮ                     │
├──────────────────────────────────────────┤
│ Hệ thống đề xuất:                        │
│                                          │
│ 1. ⭐ Khu A > Kệ A1 > Ngăn 2 (Khuyến nghị)│
│    • Đã có 8 cái Váy A (Size M)          │
│    • Còn chỗ: 12 cái                     │
│    • Lý do: Cùng sản phẩm, cùng size     │
│    [Chọn vị trí này]                     │
│                                          │
│ 2. Khu A > Kệ A1 > Ngăn 3                │
│    • Trống                               │
│    • Còn chỗ: 20 cái                     │
│    • Lý do: Gần vị trí hiện tại          │
│    [Chọn vị trí này]                     │
│                                          │
│ 3. Tự chọn vị trí khác                   │
│    [Quét barcode vị trí]                 │
└──────────────────────────────────────────┘

→ Hệ thống gợi ý thông minh
→ Nhân viên không cần suy nghĩ
```

**E. Inventory Transfer (Chuyển kho nội bộ)**

**1. Di chuyển hàng giữa các vị trí**

```
Tình huống: Sắp xếp lại kho
┌──────────────────────────────────────────┐
│ CHUYỂN KHO NỘI BỘ                        │
├──────────────────────────────────────────┤
│ Sản phẩm: Váy cưới A (Size M)            │
│ Số lượng: [5] cái                        │
│                                          │
│ Từ vị trí:                               │
│ Khu A > Kệ A1 > Ngăn 2 (Còn 10 cái)      │
│                                          │
│ Đến vị trí:                              │
│ Khu E > Mannequin 1 (Trưng bày)          │
│                                          │
│ Lý do: [▼ Trưng bày]                     │
│                                          │
│ [Xác nhận chuyển]                        │
└──────────────────────────────────────────┘

Sau khi chuyển:
• Khu A > Kệ A1 > Ngăn 2: 10 - 5 = 5 cái
• Khu E > Mannequin 1: 0 + 5 = 5 cái
• Tổng tồn kho: Không đổi (10 cái)

→ Theo dõi chính xác vị trí mọi lúc
```

**F. Báo cáo và phân tích vị trí kho**

**1. Báo cáo tồn kho theo vị trí**

```
┌──────────────────────────────────────────┐
│ BÁO CÁO TỒN KHO THEO VỊ TRÍ              │
├──────────────────────────────────────────┤
│ KHU A: Váy cưới cách tân                 │
│ ├─ Kệ A1: 45 sản phẩm (75% đầy)          │
│ │  ├─ Ngăn 1: 15 SP (Size S)            │
│ │  ├─ Ngăn 2: 18 SP (Size M)            │
│ │  └─ Ngăn 3: 12 SP (Size L)            │
│ ├─ Kệ A2: 30 sản phẩm (60% đầy)          │
│ └─ Kệ A3: 10 sản phẩm (20% đầy) ⚠️       │
│     → Có thể gộp vào kệ khác             │
│                                          │
│ KHU B: Váy cưới truyền thống             │
│ ├─ Kệ B1: 25 sản phẩm (50% đầy)          │
│ └─ Kệ B2: 35 sản phẩm (70% đầy)          │
│                                          │
│ KHU C: Váy cưới công chúa                │
│ └─ Kệ C1: 50 sản phẩm (100% đầy) 🔴      │
│     → Cần thêm kệ hoặc chuyển bớt        │
│                                          │
│ KHU D: Phụ kiện                          │
│ ├─ Kệ D1: 40 sản phẩm (80% đầy)          │
│ ├─ Kệ D2: 30 sản phẩm (60% đầy)          │
│ └─ Kệ D3: 25 sản phẩm (50% đầy)          │
│                                          │
│ TỔNG: 290 sản phẩm / 400 chỗ (72.5%)     │
│                                          │
│ [Xuất Excel] [In báo cáo]                │
└──────────────────────────────────────────┘
```

**2. Phân tích hiệu suất vị trí**

```
┌──────────────────────────────────────────┐
│ PHÂN TÍCH HIỆU SUẤT KHO                  │
├──────────────────────────────────────────┤
│ Thời gian lấy hàng trung bình:           │
│ • Khu A: 2 phút/đơn ✓ (Tốt)              │
│ • Khu B: 3 phút/đơn ✓ (OK)               │
│ • Khu C: 5 phút/đơn ⚠️ (Chậm)            │
│   → Nguyên nhân: Xa, nhiều tầng          │
│   → Giải pháp: Chuyển SP bán chạy ra gần │
│ • Khu D: 2.5 phút/đơn ✓ (Tốt)            │
│                                          │
│ Vị trí được truy cập nhiều nhất:         │
│ 1. Khu A > Kệ A1 > Ngăn 2: 150 lần/tuần │
│ 2. Khu D > Kệ D1 > Ngăn 1: 120 lần/tuần │
│ 3. Khu A > Kệ A2 > Ngăn 1: 100 lần/tuần │
│                                          │
│ Vị trí ít sử dụng:                       │
│ 1. Khu C > Kệ C3: 5 lần/tuần            │
│    → Có thể dùng cho sản phẩm ít bán     │
│                                          │
│ ĐỀ XUẤT TỐI ƯU:                          │
│ • Chuyển SP bán chạy từ Khu C về Khu A   │
│ • Gộp Kệ A3 vào Kệ A2 (tiết kiệm không gian)│
│ • Thêm kệ mới cho Khu C (đã đầy 100%)    │
└──────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Tìm hàng nhanh (< 2 phút/sản phẩm)
- ✅ Không tốn thời gian nhớ vị trí
- ✅ Tối ưu quãng đường di chuyển
- ✅ Tận dụng tối đa không gian kho
- ✅ Dễ dàng đào tạo nhân viên mới

---

## **🎯 4. GIẢI PHÁP CHO VẤN ĐỀ VỀ KHÁCH HÀNG**

### **4.1 Vấn đề: Không có CRM**

**Pain Point hiện tại:**
- Shop không lưu trữ thông tin khách hàng một cách hệ thống
- Thông tin chỉ nằm trong tin nhắn Facebook hoặc Excel rời rạc
- Khi khách quay lại mua lần sau, nhân viên không nhớ được khách là ai

**Giải pháp đề xuất:**

**A. Customer Database (Cơ sở dữ liệu khách hàng tập trung)**

**🔧 Odoo Module:** `base`, `sale`, `crm` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Contact management (Customer/Supplier)
- ✅ Customer tags & categories
- ✅ Custom fields
- ✅ Contact notes & chatter
- ✅ Purchase history
- ✅ Customer portal

**1. Customer Profile đầy đủ**

```
Hồ sơ khách hàng:
┌──────────────────────────────────────────┐
│ 👤 NGUYỄN THỊ B                          │
├──────────────────────────────────────────┤
│ THÔNG TIN CƠ BẢN:                        │
│ • SĐT: 0901234567 ⭐ (Verified)          │
│ • Email: nguyenthib@gmail.com            │
│ • Ngày sinh: 15/05/1995 (31 tuổi)        │
│ • Giới tính: Nữ                          │
│                                          │
│ ĐỊA CHỈ:                                 │
│ • Nhà riêng: 123 Nguyễn Huệ, Q1, TPHCM   │
│ • Nơi làm việc: Công ty ABC, Q3          │
│                                          │
│ PHÂN LOẠI:                               │
│ • Tags: [VIP] [Khách quen] [Cô dâu 2026] │
│ • Nguồn: Facebook                        │
│ • Nhân viên phụ trách: NV Bán A          │
│                                          │
│ THÔNG TIN ĐẶC BIỆT:                      │
│ • Size thường mua: M                     │
│ • Màu yêu thích: Trắng, Hồng pastel      │
│ • Ngân sách: 5-7 triệu VNĐ               │
│ • Ngày cưới dự kiến: 20/10/2026          │
│ • Ghi chú: Thích phong cách tối giản,    │
│   không thích ren nhiều                  │
│                                          │
│ [Chỉnh sửa] [Gọi điện] [Gửi email] [SMS] │
└──────────────────────────────────────────┘
```

**2. Tags và phân loại khách hàng**

```
Hệ thống tags:
┌──────────────────────────────────────────┐
│ PHÂN LOẠI KHÁCH HÀNG                     │
├──────────────────────────────────────────┤
│ Theo giá trị:                            │
│ • [VIP] - Mua > 20tr                     │
│ • [Khách quen] - Mua >= 3 lần            │
│ • [Khách mới] - Mua lần đầu              │
│                                          │
│ Theo trạng thái:                         │
│ • [Cô dâu 2026] - Sắp cưới năm 2026      │
│ • [Đã cưới] - Đã mua và sử dụng          │
│ • [Đang tìm hiểu] - Chưa quyết định      │
│                                          │
│ Theo nguồn:                              │
│ • [Facebook] - Từ Facebook               │
│ • [Website] - Từ website                 │
│ • [Giới thiệu] - Bạn bè giới thiệu       │
│ • [Walk-in] - Vào cửa hàng trực tiếp     │
│                                          │
│ Theo sở thích:                           │
│ • [Phong cách hiện đại]                  │
│ • [Phong cách truyền thống]              │
│ • [Phong cách công chúa]                 │
│                                          │
│ [Tạo tag mới]                            │
└──────────────────────────────────────────┘

Sử dụng:
→ Lọc khách hàng: "Tất cả VIP + Cô dâu 2026"
→ Gửi email marketing: "Khuyến mãi cho khách quen"
→ Phân công nhân viên: "NV A chăm sóc VIP"
```

**B. Lead Management (Quản lý khách hàng tiềm năng)**

**1. Quy trình từ Lead → Customer**

```
GIAI ĐOẠN 1: LEAD (Khách hàng tiềm năng)
┌──────────────────────────────────────────┐
│ Nguồn: Khách inbox Facebook hỏi giá      │
│                                          │
│ Thông tin:                               │
│ • Tên: Nguyễn Thị C                      │
│ • SĐT: 0912345678                        │
│ • Quan tâm: Váy cưới cách tân            │
│ • Ngân sách: 5-7tr                       │
│                                          │
│ Trạng thái: NEW (Mới)                    │
│ Độ ưu tiên: 🔴 Cao (Cưới sau 2 tháng)   │
│                                          │
│ Hành động tiếp theo:                     │
│ ☐ Gọi điện tư vấn (Hạn: Hôm nay 15:00)   │
│ ☐ Gửi catalog qua email                  │
│ ☐ Hẹn đến cửa hàng thử váy               │
└──────────────────────────────────────────┘
         ↓
GIAI ĐOẠN 2: QUALIFIED (Đã xác nhận)
┌──────────────────────────────────────────┐
│ Đã gọi điện, khách quan tâm              │
│ Đã hẹn đến cửa hàng: 06/04/2026 14:00    │
│                                          │
│ Trạng thái: QUALIFIED                    │
│ Tỷ lệ chốt: 60%                          │
└──────────────────────────────────────────┘
         ↓
GIAI ĐOẠN 3: QUOTATION (Báo giá)
┌──────────────────────────────────────────┐
│ Khách đã đến cửa hàng, thử váy           │
│ Đã tạo báo giá: #QT001 - 6,500,000 VNĐ   │
│                                          │
│ Trạng thái: QUOTATION                    │
│ Tỷ lệ chốt: 80%                          │
└──────────────────────────────────────────┘
         ↓
GIAI ĐOẠN 4: WON (Chốt đơn) ✓
┌──────────────────────────────────────────┐
│ Khách đồng ý mua!                        │
│ Đơn hàng: #SO001 - 6,500,000 VNĐ         │
│                                          │
│ Trạng thái: WON ✓                        │
│ → Chuyển thành CUSTOMER                  │
└──────────────────────────────────────────┘

Hoặc:
GIAI ĐOẠN 4: LOST (Mất khách) ✗
┌──────────────────────────────────────────┐
│ Khách không mua                          │
│                                          │
│ Lý do: [▼ Giá cao]                       │
│   - Giá cao                              │
│   - Mua ở chỗ khác                       │
│   - Hoãn cưới                            │
│   - Không liên lạc được                  │
│   - Khác                                 │
│                                          │
│ Ghi chú: Khách thấy giá cao, sẽ suy nghĩ│
│                                          │
│ Hành động:                               │
│ ☐ Follow-up sau 1 tuần                   │
│ ☐ Gửi voucher giảm giá 10%               │
└──────────────────────────────────────────┘
```

**2. Kanban Board quản lý Lead**

```
┌────────┬────────┬────────┬────────┬────────┬────────┐
│  NEW   │QUALIFIED│QUOTATION│  WON   │  LOST  │        │
│  (10)  │  (8)   │  (5)   │  (3)   │  (2)   │        │
├────────┼────────┼────────┼────────┼────────┼────────┤
│┌──────┐│┌──────┐│┌──────┐│┌──────┐│┌──────┐│        │
││Lead 1││Lead 5 ││Lead 8 ││Lead 13││Lead 15││        │
││Nguyễn││Trần B ││Lê D   ││Phạm F ││Võ H   ││        │
││Thị A  ││6tr    ││7tr    ││6.5tr  ││5tr    ││        │
││5-7tr  ││🔴 Cao ││🟡 TB  ││✓ Chốt ││✗ Giá ││        │
│└──────┘│└──────┘│└──────┘│└──────┘│ cao   ││        │
││       ││       ││       ││       │└──────┘│        │
│┌──────┐│┌──────┐│┌──────┐│┌──────┐│        │        │
││Lead 2││Lead 6 ││Lead 9 ││Lead 14││        │        │
││...    ││...    ││...    ││...    ││        │        │
│└──────┘│└──────┘│└──────┘│└──────┘│        │        │
│        │        │        │        │        │        │
│[+ Thêm]│        │        │        │        │        │
└────────┴────────┴────────┴────────┴────────┴────────┘

→ Kéo thả để chuyển trạng thái
→ Nhìn 1 cái biết tình hình
→ Lọc theo nhân viên, độ ưu tiên, ngày,...
```

**C. Activities & Follow-up (Hoạt động và theo dõi)**

**1. Lên lịch chăm sóc khách hàng**

```
Với mỗi lead/customer:
┌──────────────────────────────────────────┐
│ LỊCH CHĂM SÓC - Nguyễn Thị B             │
├──────────────────────────────────────────┤
│ 🔴 QUÁ HẠN (1)                           │
│ ├─ 03/04: Gọi điện follow-up             │
│ │   Giao cho: NV Bán A                   │
│ │   [Đánh dấu hoàn thành]                │
│                                          │
│ 🟡 HÔM NAY (2)                           │
│ ├─ 04/04 10:00: Gọi điện nhắc hẹn        │
│ │   "Nhắc khách đến cửa hàng 14:00"      │
│ │   [Hoàn thành] [Hoãn]                  │
│ │                                        │
│ └─ 04/04 14:00: Gặp khách tại cửa hàng   │
│     "Tư vấn và cho thử váy"              │
│     [Hoàn thành] [Hoãn]                  │
│                                          │
│ 🟢 TUẦN NÀY (3)                          │
│ ├─ 05/04: Gửi email cảm ơn               │
│ ├─ 06/04: Gọi điện hỏi feedback          │
│ └─ 07/04: Gửi voucher giảm giá           │
│                                          │
│ [Thêm hoạt động mới]                     │
└──────────────────────────────────────────┘
```

**2. Tự động tạo activities**

```
Rule: Khi tạo lead mới
→ Tự động tạo activity: "Gọi điện tư vấn" (Hạn: Trong ngày)

Rule: Khi khách hẹn đến cửa hàng
→ Tự động tạo activity: "Nhắc khách 1 giờ trước"

Rule: Sau khi báo giá
→ Tự động tạo activity: "Follow-up sau 2 ngày"

Rule: Khi khách không mua (Lost)
→ Tự động tạo activity: "Follow-up sau 1 tuần"

→ Không cần nhớ, hệ thống tự động nhắc
```

**D. Communication History (Lịch sử giao tiếp)**

**1. Ghi lại mọi tương tác**

```
Hồ sơ khách hàng - Nguyễn Thị B:
┌──────────────────────────────────────────┐
│ 📞 LỊCH SỬ GIAO TIẾP                     │
├──────────────────────────────────────────┤
│ 01/04/2026 10:00 - Cuộc gọi              │
│ ├─ Người gọi: NV Bán A                   │
│ ├─ Thời lượng: 15 phút                   │
│ └─ Nội dung: Tư vấn về váy cưới cách tân,│
│   khách quan tâm mẫu A và B, ngân sách   │
│   5-7tr, hẹn đến cửa hàng 04/04 14:00    │
│                                          │
│ 01/04/2026 14:30 - Email                 │
│ ├─ Gửi bởi: NV Bán A                     │
│ ├─ Tiêu đề: "Catalog váy cưới 2026"      │
│ └─ Trạng thái: ✓ Đã mở (01/04 15:00)     │
│                                          │
│ 02/04/2026 09:00 - SMS                   │
│ ├─ Gửi bởi: Hệ thống                     │
│ ├─ Nội dung: "Nhắc lịch hẹn 04/04 14:00" │
│ └─ Trạng thái: ✓ Đã gửi                  │
│                                          │
│ 03/04/2026 16:00 - Tin nhắn Facebook     │
│ ├─ Khách hỏi: "Mẫu A còn size M không?"  │
│ └─ NV trả lời: "Dạ còn ạ, em để dành cho│
│   chị luôn nhé!"                         │
│                                          │
│ 04/04/2026 14:00 - Gặp mặt               │
│ ├─ Địa điểm: Cửa hàng                    │
│ ├─ Người tiếp: NV Bán A                  │
│ └─ Nội dung: Khách thử váy A và B, thích │
│   váy A hơn, đồng ý mua, tạo đơn #SO001  │
│                                          │
│ [Thêm ghi chú] [Gọi điện] [Gửi email]    │
└──────────────────────────────────────────┘

→ Nhân viên nào cũng biết lịch sử
→ Không cần hỏi lại khách
→ Chuyên nghiệp, nhất quán
```

**E. Customer Segmentation (Phân khúc khách hàng)**

**🔧 Odoo Module:** `sale`, `crm` (Cần customize)

**💻 Customize Python cho RFM Analysis:**

```python
# Module: crm_rfm_analysis
from odoo import models, fields, api
from datetime import datetime

class ResPartner(models.Model):
    _inherit = 'res.partner'

    rfm_segment = fields.Selection([
        ('champions', 'Champions'),
        ('loyal', 'Loyal'),
        ('potential', 'Potential'),
        ('at_risk', 'At Risk'),
        ('hibernating', 'Hibernating'),
        ('new', 'New')
    ], string='RFM Segment', compute='_compute_rfm_score', store=True)
    
    recency_days = fields.Integer('Recency (Days)', compute='_compute_rfm_score')
    frequency_count = fields.Integer('Frequency', compute='_compute_rfm_score')
    monetary_value = fields.Float('Monetary Value', compute='_compute_rfm_score')

    @api.depends('sale_order_ids.date_order', 'sale_order_ids.amount_total')
    def _compute_rfm_score(self):
        for partner in self:
            orders = self.env['sale.order'].search([
                ('partner_id', '=', partner.id),
                ('state', 'in', ['sale', 'done'])
            ])
            
            if not orders:
                partner.rfm_segment = 'new'
                continue
            
            # Recency, Frequency, Monetary
            last_order = max(orders.mapped('date_order'))
            recency = (datetime.now().date() - last_order.date()).days
            frequency = len(orders)
            monetary = sum(orders.mapped('amount_total'))
            
            partner.recency_days = recency
            partner.frequency_count = frequency
            partner.monetary_value = monetary
            
            # Tính RFM score và phân khúc
            r = 5 if recency < 30 else 3 if recency < 90 else 1
            f = 5 if frequency >= 5 else 3 if frequency >= 2 else 1
            m = 5 if monetary >= 20000000 else 3 if monetary >= 10000000 else 1
            
            if r >= 4 and f >= 4 and m >= 4:
                partner.rfm_segment = 'champions'
            elif f >= 4 and m >= 4:
                partner.rfm_segment = 'loyal'
            elif r >= 4 and f <= 2:
                partner.rfm_segment = 'potential'
            elif r <= 2 and f >= 3:
                partner.rfm_segment = 'at_risk'
            else:
                partner.rfm_segment = 'hibernating'
```

**1. Phân loại tự động theo RFM**

```
RFM Analysis:
┌──────────────────────────────────────────┐
│ R - Recency (Mua gần đây)                │
│ F - Frequency (Tần suất mua)             │
│ M - Monetary (Giá trị mua)               │
├──────────────────────────────────────────┤
│ PHÂN KHÚC:                               │
│                                          │
│ 🏆 CHAMPIONS (Khách hàng vàng)           │
│ • R: Cao | F: Cao | M: Cao              │
│ • Mua gần đây, mua nhiều lần, chi nhiều  │
│ • Số lượng: 15 khách (5%)                │
│ • Hành động: Chăm sóc đặc biệt, ưu đãi VIP│
│                                          │
│ 💎 LOYAL (Khách trung thành)             │
│ • R: TB | F: Cao | M: Cao               │
│ • Mua thường xuyên, chi nhiều            │
│ • Số lượng: 45 khách (15%)               │
│ • Hành động: Tặng quà, voucher           │
│                                          │
│ 🌟 POTENTIAL (Tiềm năng)                 │
│ • R: Cao | F: Thấp | M: Cao             │
│ • Mua gần đây, chi nhiều nhưng mới 1 lần │
│ • Số lượng: 60 khách (20%)               │
│ • Hành động: Khuyến khích mua lần 2      │
│                                          │
│ 💤 AT RISK (Có nguy cơ mất)              │
│ • R: Thấp | F: Cao | M: Cao             │
│ • Lâu không mua, trước đây mua nhiều     │
│ • Số lượng: 30 khách (10%)               │
│ • Hành động: Gọi điện, gửi ưu đãi đặc biệt│
│                                          │
│ 😴 HIBERNATING (Ngủ đông)                │
│ • R: Thấp | F: Thấp | M: Thấp           │
│ • Lâu không mua, mua ít                  │
│ • Số lượng: 90 khách (30%)               │
│ • Hành động: Email marketing, khảo sát   │
│                                          │
│ 🆕 NEW (Khách mới)                       │
│ • Mua lần đầu                            │
│ • Số lượng: 60 khách (20%)               │
│ • Hành động: Chào mừng, voucher lần 2    │
└──────────────────────────────────────────┘

→ Tự động phân loại
→ Chiến lược marketing phù hợp từng nhóm
```

**Lợi ích:**
- ✅ Lưu trữ đầy đủ thông tin khách hàng
- ✅ Không quên khách hàng nào
- ✅ Tăng tỷ lệ chốt đơn (theo dõi sát sao)
- ✅ Chuyên nghiệp, tạo ấn tượng tốt

---

### **4.2 Vấn đề: Không có lịch sử mua hàng**

**Pain Point hiện tại:**
- Shop không có dữ liệu về lịch sử mua hàng của khách
- Không biết khách đã từng mua sản phẩm nào, size gì, màu gì
- Không thể cá nhân hóa trải nghiệm mua sắm

**Giải pháp đề xuất:**

**A. Purchase History (Lịch sử mua hàng chi tiết)**

**🔧 Odoo Module:** `sale`, `sale_management` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Full purchase history per customer
- ✅ Order details with products, quantities, prices
- ✅ Order timeline & status
- ✅ Reorder functionality
- ✅ Customer portal (khách tự xem lịch sử)

**1. Xem toàn bộ lịch sử đơn hàng**

```
Hồ sơ khách hàng - Nguyễn Thị B:
┌──────────────────────────────────────────┐
│ 🛍️ LỊCH SỬ MUA HÀNG                     │
├──────────────────────────────────────────┤
│ TỔNG QUAN:                               │
│ • Tổng đơn hàng: 5 đơn                   │
│ • Tổng chi tiêu: 32,500,000 VNĐ          │
│ • Giá trị TB/đơn: 6,500,000 VNĐ          │
│ • Lần mua đầu: 15/01/2024                │
│ • Lần mua gần nhất: 20/03/2026           │
├──────────────────────────────────────────┤
│ CHI TIẾT ĐơN HÀNG:                       │
│                                          │
│ 📦 #SO005 - 20/03/2026                   │
│ ├─ Váy dạ hội đỏ - Size M                │
│ ├─ Tổng tiền: 8,500,000 VNĐ              │
│ └─ Trạng thái: ✓ Hoàn thành              │
│                                          │
│ 📦 #SO004 - 10/02/2026                   │
│ ├─ Áo dài cưới trắng - Size M            │
│ ├─ Phụ kiện: Khăn voan, hoa cài          │
│ ├─ Tổng tiền: 7,000,000 VNĐ              │
│ └─ Trạng thái: ✓ Hoàn thành              │
│                                          │
│ 📦 #SO003 - 05/12/2025                   │
│ ├─ Váy cưới công chúa - Size M           │
│ ├─ Tổng tiền: 9,000,000 VNĐ              │
│ └─ Trạng thái: ✓ Hoàn thành              │
│                                          │
│ 📦 #SO002 - 20/08/2025                   │
│ ├─ Váy cưới cách tân hồng - Size M       │
│ ├─ Tổng tiền: 6,000,000 VNĐ              │
│ └─ Trạng thái: ✓ Hoàn thành              │
│                                          │
│ 📦 #SO001 - 15/01/2024                   │
│ ├─ Váy cưới trắng đơn giản - Size M      │
│ ├─ Tổng tiền: 2,000,000 VNĐ (Thuê)       │
│ └─ Trạng thái: ✓ Hoàn thành              │
│                                          │
│ [Xem chi tiết] [Mua lại] [In hóa đơn]    │
└──────────────────────────────────────────┘
```

**2. Phân tích sở thích khách hàng**

```
INSIGHT KHÁCH HÀNG - Nguyễn Thị B:
┌──────────────────────────────────────────┐
│ 📊 PHÂN TÍCH SỞ THÍCH                    │
├──────────────────────────────────────────┤
│ SIZE THƯỜNG MUA:                         │
│ • Size M: 5/5 đơn (100%) ⭐              │
│ → Gợi ý: Luôn có sẵn size M cho khách   │
│                                          │
│ MÀU SẮC YÊU THÍCH:                       │
│ • Trắng: 3 lần                           │
│ • Hồng pastel: 2 lần                     │
│ • Đỏ: 1 lần                              │
│ → Gợi ý: Ưu tiên giới thiệu màu trắng/hồng│
│                                          │
│ PHONG CÁCH:                              │
│ • Cách tân: 2 lần                        │
│ • Công chúa: 1 lần                       │
│ • Đơn giản: 1 lần                        │
│ • Dạ hội: 1 lần                          │
│ → Gợi ý: Khách thích đa dạng phong cách  │
│                                          │
│ NGÂN SÁCH:                               │
│ • Trung bình: 6,500,000 VNĐ/đơn          │
│ • Cao nhất: 9,000,000 VNĐ                │
│ • Thấp nhất: 2,000,000 VNĐ (Thuê)        │
│ → Gợi ý: Giới thiệu sản phẩm 6-9 triệu   │
│                                          │
│ THỜI GIAN MUA:                           │
│ • Mua thường xuyên nhất: Q1 (3 lần)      │
│ • Khoảng cách TB giữa các lần: 4 tháng   │
│ → Gợi ý: Follow-up sau 3-4 tháng         │
└──────────────────────────────────────────┘
```

**B. Product Recommendations (Gợi ý sản phẩm thông minh)**

**1. Gợi ý dựa trên lịch sử mua**

```
Khi khách Nguyễn Thị B inbox:
┌──────────────────────────────────────────┐
│ 💡 GỢI Ý CHO KHÁCH HÀNG                  │
├──────────────────────────────────────────┤
│ Dựa trên lịch sử mua hàng:               │
│                                          │
│ ✨ SẢN PHẨM PHÙ HỢP:                     │
│                                          │
│ 1️⃣ Váy cưới cách tân trắng - Size M     │
│    • Giá: 6,800,000 VNĐ                  │
│    • Lý do: Khách thích cách tân + trắng │
│    • Có sẵn kho: ✓                       │
│    [Gửi ảnh cho khách]                   │
│                                          │
│ 2️⃣ Váy dạ hội hồng pastel - Size M      │
│    • Giá: 7,200,000 VNĐ                  │
│    • Lý do: Khách thích màu hồng pastel  │
│    • Có sẵn kho: ✓                       │
│    [Gửi ảnh cho khách]                   │
│                                          │
│ 3️⃣ Áo dài cưới hồng phấn - Size M       │
│    • Giá: 6,500,000 VNĐ                  │
│    • Lý do: Phù hợp ngân sách + sở thích │
│    • Có sẵn kho: ✓                       │
│    [Gửi ảnh cho khách]                   │
│                                          │
│ ❌ KHÔNG NÊN GIỚI THIỆU:                 │
│ • Váy màu đen (Khách chưa mua bao giờ)   │
│ • Size S/L (Khách luôn mua M)            │
│ • Giá > 9tr (Vượt ngân sách thường)      │
└──────────────────────────────────────────┘
```

**2. Cross-sell và Up-sell thông minh**

```
Khi khách đang xem váy cưới:
┌──────────────────────────────────────────┐
│ 🎁 KHÁCH HÀNG THƯỜNG MUA THÊM            │
├──────────────────────────────────────────┤
│ Dựa trên khách hàng tương tự:            │
│                                          │
│ 📌 PHỤ KIỆN ĐI KÈM:                      │
│ • Khăn voan cưới - 500,000 VNĐ           │
│   (85% khách mua váy cưới mua thêm)      │
│                                          │
│ • Hoa cài tóc - 300,000 VNĐ              │
│   (70% khách mua váy cưới mua thêm)      │
│                                          │
│ • Găng tay ren - 200,000 VNĐ             │
│   (60% khách mua váy cưới mua thêm)      │
│                                          │
│ 💎 NÂNG CẤP:                             │
│ • Váy cưới cao cấp hơn +2,000,000 VNĐ    │
│   "Chất liệu ren Pháp, đính pha lê"      │
│                                          │
│ 🎉 COMBO ƯU ĐÃI:                         │
│ • Váy cưới + Áo dài = Giảm 1,000,000 VNĐ │
│ • Váy + 3 phụ kiện = Tặng makeup         │
│                                          │
│ [Thêm vào đơn hàng]                      │
└──────────────────────────────────────────┘
```

**C. Repeat Purchase Tracking (Theo dõi mua lại)**

**1. Nhắc khách mua lại**

```
Automation Rules:
┌──────────────────────────────────────────┐
│ 🔔 TỰ ĐỘNG NHẮC MUA LẠI                  │
├──────────────────────────────────────────┤
│ Rule 1: Khách mua váy cưới (thuê)        │
│ → Sau 6 tháng: Gửi email "Váy cưới mua"  │
│   "Chị đã thuê váy của shop, có muốn     │
│    sở hữu váy cưới riêng không?"         │
│                                          │
│ Rule 2: Khách mua váy dạ hội             │
│ → Sau 3 tháng: "Sự kiện mới, váy mới"    │
│   "Có sự kiện nào sắp tới không chị?"    │
│                                          │
│ Rule 3: Khách mua phụ kiện               │
│ → Sau 1 tháng: "Bộ sưu tập phụ kiện mới" │
│                                          │
│ Rule 4: Khách VIP không mua > 6 tháng    │
│ → Gửi voucher 15% "We miss you!"         │
│                                          │
│ → Tự động, không cần nhớ                 │
└──────────────────────────────────────────┘
```

**2. Chương trình khách hàng thân thiết**

```
LOYALTY PROGRAM:
┌──────────────────────────────────────────┐
│ 🏆 CHƯƠNG TRÌNH KHÁCH HÀNG THÂN THIẾT    │
├──────────────────────────────────────────┤
│ Nguyễn Thị B - Hạng VÀNG 💛              │
│                                          │
│ ĐIỂM TÍCH LŨY:                           │
│ • Điểm hiện tại: 3,250 điểm              │
│ • Tích lũy từ: 32,500,000 VNĐ            │
│   (1,000 VNĐ = 1 điểm)                   │
│                                          │
│ ƯU ĐÃI HẠNG VÀNG:                        │
│ ✓ Giảm 10% mọi đơn hàng                  │
│ ✓ Miễn phí ship                          │
│ ✓ Ưu tiên đặt hàng trước                 │
│ ✓ Tặng quà sinh nhật                     │
│ ✓ Mời tham gia sự kiện VIP               │
│                                          │
│ THĂNG HẠNG:                              │
│ • Còn 7,500,000 VNĐ → Hạng BẠCH KIM 💎   │
│   (Tổng 40tr)                            │
│                                          │
│ ĐỔI ĐIỂM:                                │
│ • 1,000 điểm = Voucher 1,000,000 VNĐ     │
│ • 500 điểm = Miễn phí makeup             │
│ • 300 điểm = Phụ kiện miễn phí           │
│                                          │
│ [Đổi điểm] [Xem ưu đãi] [Lịch sử điểm]   │
└──────────────────────────────────────────┘
```

**D. Customer Lifetime Value (CLV) Analysis**

**1. Dự đoán giá trị khách hàng**

```
PHÂN TÍCH GIÁ TRỊ KHÁCH HÀNG:
┌──────────────────────────────────────────┐
│ 💰 CUSTOMER LIFETIME VALUE               │
├──────────────────────────────────────────┤
│ Nguyễn Thị B:                            │
│                                          │
│ ĐÃ CHI TIÊU:                             │
│ • Tổng: 32,500,000 VNĐ (2 năm)           │
│ • Trung bình: 16,250,000 VNĐ/năm         │
│                                          │
│ DỰ ĐOÁN:                                 │
│ • CLV dự kiến (5 năm): 81,250,000 VNĐ    │
│ • Xác suất mua lại: 85% (Rất cao)        │
│ • Thời gian mua lại dự kiến: 2-3 tháng   │
│                                          │
│ PHÂN LOẠI:                               │
│ • Nhóm: HIGH VALUE CUSTOMER 🏆           │
│ • Top: 5% khách hàng giá trị nhất        │
│                                          │
│ KHUYẾN NGHỊ:                             │
│ ✓ Chăm sóc đặc biệt, ưu tiên cao nhất    │
│ ✓ Gọi điện định kỳ hỏi thăm              │
│ ✓ Tặng quà sinh nhật, ngày kỷ niệm       │
│ ✓ Mời tham gia sự kiện VIP               │
│ ✓ Giới thiệu sản phẩm mới đầu tiên       │
└──────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Hiểu rõ sở thích và hành vi mua của khách
- ✅ Tư vấn chính xác, phù hợp với từng khách
- ✅ Tăng giá trị đơn hàng (cross-sell, up-sell)
- ✅ Tăng tỷ lệ khách quay lại mua (repeat rate)
- ✅ Xây dựng lòng trung thành khách hàng

---

### **4.3 Vấn đề: Khách hàng phải chờ lâu**

**Pain Point hiện tại:**
- Do quy trình xử lý đơn hàng thủ công, khách phải chờ lâu
- Nhân viên phải kiểm tra kho, xác nhận sản phẩm thủ công
- Trong giờ cao điểm, thời gian phản hồi kéo dài
- Trải nghiệm khách hàng kém

**Giải pháp đề xuất:**

**A. Quick Response System (Hệ thống phản hồi nhanh)**

**🔧 Odoo Module:** `website_sale`, `stock`, `sale` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Real-time stock check trên website
- ✅ Instant quotation generation
- ✅ Product search & filtering
- ✅ Add to cart & checkout

**1. Kiểm tra tồn kho tức thời**

```
Khi khách hỏi: "Váy A còn size M không?"

QUY TRÌNH CŨ (AS-IS):
┌──────────────────────────────────────────┐
│ 1. NV nhận tin nhắn                      │
│ 2. Mở file Excel tìm sản phẩm (2 phút)   │
│ 3. Gọi điện cho kho hỏi (3 phút)         │
│ 4. NV kho vào kho tìm (5 phút)           │
│ 5. NV kho gọi lại báo (1 phút)           │
│ 6. NV trả lời khách (1 phút)             │
│                                          │
│ ⏱️ TỔNG: 12 phút                         │
│ ❌ Khách đã mất kiên nhẫn                │
└──────────────────────────────────────────┘

QUY TRÌNH MỚI (TO-BE):
┌──────────────────────────────────────────┐
│ 1. NV nhận tin nhắn                      │
│ 2. Tìm kiếm "Váy A" trong hệ thống       │
│    → Kết quả hiện ngay:                  │
│    ✓ Váy A - Size M: Còn 3 cái           │
│    ✓ Vị trí: Kệ A2, Tầng 1               │
│    ✓ Giá: 6,500,000 VNĐ                  │
│ 3. NV trả lời khách ngay                 │
│                                          │
│ ⏱️ TỔNG: 30 giây                         │
│ ✓ Khách hài lòng                         │
└──────────────────────────────────────────┘
```

**2. Chatbot tự động trả lời 24/7**

```
CHATBOT TỰ ĐỘNG:
┌──────────────────────────────────────────┐
│ 🤖 CHATBOT - Trợ lý ảo của shop          │
├──────────────────────────────────────────┤
│ Khách: "Váy cưới cách tân giá bao nhiêu?"│
│                                          │
│ Bot: "Chào chị! Shop có nhiều mẫu váy    │
│      cưới cách tân với giá từ 5-10 triệu │
│      VNĐ. Chị muốn xem mẫu nào ạ?"       │
│                                          │
│      [Xem tất cả] [5-7tr] [7-10tr]       │
│                                          │
│ Khách: [Click "5-7tr"]                   │
│                                          │
│ Bot: "Dạ, đây là 8 mẫu váy cưới cách tân │
│      từ 5-7 triệu VNĐ:"                  │
│                                          │
│      📷 Váy A - 6,500,000 VNĐ (Còn hàng) │
│      📷 Váy B - 6,800,000 VNĐ (Còn hàng) │
│      📷 Váy C - 5,900,000 VNĐ (Hết hàng) │
│      ...                                 │
│                                          │
│      [Xem chi tiết] [Đặt hàng ngay]      │
│                                          │
│ Khách: "Váy A còn size M không?"         │
│                                          │
│ Bot: "Dạ váy A còn size M ạ (Còn 3 cái). │
│      Chị muốn đặt hàng không?"           │
│                                          │
│      [Đặt hàng] [Xem size khác]          │
│      [Chat với nhân viên]                │
│                                          │
│ → Trả lời tức thời 24/7                  │
│ → Chuyển cho NV nếu câu hỏi phức tạp     │
└──────────────────────────────────────────┘
```

**3. Quick Quote (Báo giá nhanh)**

```
Tính năng báo giá tự động:
┌──────────────────────────────────────────┐
│ 💵 BÁO GIÁ NHANH                         │
├──────────────────────────────────────────┤
│ Khách chọn sản phẩm:                     │
│ ☑️ Váy cưới A - Size M                   │
│ ☑️ Khăn voan                             │
│ ☑️ Hoa cài tóc                           │
│                                          │
│ Hệ thống tự động tính:                   │
│ ┌──────────────────────────────────┐    │
│ │ Váy cưới A        6,500,000 VNĐ  │    │
│ │ Khăn voan           500,000 VNĐ  │    │
│ │ Hoa cài tóc         300,000 VNĐ  │    │
│ │ ─────────────────────────────────│    │
│ │ Tạm tính:         7,300,000 VNĐ  │    │
│ │ Giảm giá (VIP):    -730,000 VNĐ  │    │
│ │ ─────────────────────────────────│    │
│ │ TỔNG CỘNG:        6,570,000 VNĐ  │    │
│ └──────────────────────────────────┘    │
│                                          │
│ [Gửi báo giá cho khách] [Tạo đơn hàng]   │
│                                          │
│ ⏱️ Thời gian: 10 giây                    │
│ (So với 10-15 phút tính thủ công)        │
└──────────────────────────────────────────┘
```

**B. Self-Service Portal (Cổng tự phục vụ)**

**1. Customer Portal - Khách tự tra cứu**

```
WEBSITE/APP KHÁCH HÀNG:
┌──────────────────────────────────────────┐
│ 👤 Xin chào, Nguyễn Thị B                │
├──────────────────────────────────────────┤
│ 🔍 TÌM KIẾM SẢN PHẨM                     │
│ [Tìm kiếm...] 🔍                         │
│                                          │
│ Lọc:                                     │
│ • Loại: [▼ Váy cưới]                     │
│ • Giá: [5tr] ─────●──── [10tr]          │
│ • Size: [☑️ M] [ ] L [ ] XL              │
│ • Màu: [☑️ Trắng] [☑️ Hồng]              │
│ • Còn hàng: [☑️]                         │
│                                          │
│ [Tìm kiếm]                               │
│                                          │
│ ─────────────────────────────────────────│
│ KẾT QUẢ: 12 sản phẩm                     │
│                                          │
│ 📷 Váy cưới A - 6,500,000 VNĐ            │
│    Size M ✓ | Trắng | Còn 3 cái          │
│    ⭐⭐⭐⭐⭐ (25 đánh giá)                │
│    [Xem] [Đặt hàng]                      │
│                                          │
│ 📷 Váy cưới B - 6,800,000 VNĐ            │
│    Size M ✓ | Hồng | Còn 5 cái           │
│    ⭐⭐⭐⭐ (18 đánh giá)                 │
│    [Xem] [Đặt hàng]                      │
│                                          │
│ → Khách tự tìm, không cần hỏi NV         │
└──────────────────────────────────────────┘
```

**2. Order Tracking - Theo dõi đơn hàng**

```
Khách tự theo dõi đơn hàng:
┌──────────────────────────────────────────┐
│ 📦 THEO DÕI ĐƠN HÀNG #SO001              │
├──────────────────────────────────────────┤
│ Trạng thái: Đang chuẩn bị hàng 📦        │
│                                          │
│ TIẾN TRÌNH:                              │
│ ✓ Đã đặt hàng      04/04 10:00           │
│ ✓ Đã xác nhận      04/04 10:05           │
│ ✓ Đang chuẩn bị    04/04 10:30           │
│ ⏳ Đang giao hàng   Dự kiến 04/04 15:00  │
│ ⏳ Hoàn thành       Dự kiến 04/04 16:00  │
│                                          │
│ CHI TIẾT:                                │
│ • Sản phẩm: Váy cưới A - Size M          │
│ • Tổng tiền: 6,500,000 VNĐ               │
│ • Địa chỉ: 123 Nguyễn Huệ, Q1, TPHCM     │
│ • Shipper: Nguyễn Văn X - 0909123456     │
│                                          │
│ [Gọi shipper] [Hủy đơn] [Liên hệ shop]   │
│                                          │
│ → Khách biết rõ tiến độ, không cần hỏi   │
└──────────────────────────────────────────┘
```

**C. Omnichannel Integration (Tích hợp đa kênh)**

**1. Thống nhất thông tin trên mọi kênh**

```
OMNICHANNEL:
┌──────────────────────────────────────────┐
│ 📱 KHÁCH TƯƠNG TÁC QUA NHIỀU KÊNH        │
├──────────────────────────────────────────┤
│ Nguyễn Thị B:                            │
│                                          │
│ 10:00 - Facebook: "Váy A còn không?"     │
│ → Bot trả lời: "Còn ạ, size M còn 3 cái" │
│                                          │
│ 10:30 - Website: Xem chi tiết Váy A      │
│ → Hệ thống nhận diện: "Chị đã hỏi trên   │
│   Facebook, váy này còn size M ạ"        │
│                                          │
│ 11:00 - Điện thoại: Gọi shop hỏi giá     │
│ → NV thấy lịch sử: "Dạ, chị đã xem váy A │
│   trên web, giá 6,5tr, chị muốn đặt không?"│
│                                          │
│ 14:00 - Đến cửa hàng: Thử váy            │
│ → NV thấy hồ sơ: "Chào chị B, váy A size │
│   M em đã chuẩn bị sẵn cho chị rồi ạ"    │
│                                          │
│ → Mọi kênh đều biết lịch sử khách        │
│ → Khách không phải lặp lại thông tin     │
│ → Trải nghiệm liền mạch, chuyên nghiệp   │
└──────────────────────────────────────────┘
```

**D. Express Checkout (Thanh toán nhanh)**

**1. One-click ordering**

```
THANH TOÁN NHANH:
┌──────────────────────────────────────────┐
│ ⚡ THANH TOÁN 1 CLICK                    │
├──────────────────────────────────────────┤
│ Khách hàng quen (đã có thông tin):       │
│                                          │
│ Sản phẩm: Váy cưới A - Size M            │
│ Giá: 6,500,000 VNĐ                       │
│                                          │
│ Giao đến:                                │
│ 📍 123 Nguyễn Huệ, Q1, TPHCM             │
│    (Địa chỉ mặc định)                    │
│    [Đổi địa chỉ]                         │
│                                          │
│ Thanh toán:                              │
│ 💳 Thẻ Visa ****1234 (Đã lưu)            │
│    [Đổi phương thức]                     │
│                                          │
│ ┌──────────────────────────────────┐    │
│ │ [⚡ ĐẶT HÀNG NGAY]                │    │
│ └──────────────────────────────────┘    │
│                                          │
│ ⏱️ Thời gian: 5 giây                     │
│ (So với 5-10 phút điền form thủ công)    │
└──────────────────────────────────────────┘
```

**2. Multiple payment options**

```
PHƯƠNG THỨC THANH TOÁN ĐA DẠNG:
┌──────────────────────────────────────────┐
│ 💰 CHỌN CÁCH THANH TOÁN                  │
├──────────────────────────────────────────┤
│ ⚡ THANH TOÁN NHANH:                     │
│ • 💳 Thẻ tín dụng/ghi nợ                 │
│ • 📱 Ví điện tử (MoMo, ZaloPay, VNPay)   │
│ • 🏦 Chuyển khoản ngân hàng              │
│ • 📲 QR Code (Quét là xong)              │
│                                          │
│ 🕐 THANH TOÁN SAU:                       │
│ • 💵 COD (Thanh toán khi nhận hàng)      │
│ • 📅 Trả góp 0% (3-6-12 tháng)           │
│ • 💳 Đặt cọc trước (30-50%)              │
│                                          │
│ → Khách chọn cách thuận tiện nhất        │
│ → Thanh toán nhanh, không chờ đợi        │
└──────────────────────────────────────────┘
```

**E. Real-time Notifications (Thông báo tức thời)**

**1. Thông báo cho khách hàng**

```
HỆ THỐNG THÔNG BÁO TỰ ĐỘNG:
┌──────────────────────────────────────────┐
│ 🔔 THÔNG BÁO CHO KHÁCH                   │
├──────────────────────────────────────────┤
│ Khi đặt hàng thành công:                 │
│ → SMS + Email ngay lập tức:              │
│   "Đơn hàng #SO001 đã được xác nhận.     │
│    Dự kiến giao: 04/04 15:00"            │
│                                          │
│ Khi đang chuẩn bị hàng:                  │
│ → Thông báo: "Đơn hàng đang được đóng gói"│
│                                          │
│ Khi bắt đầu giao:                        │
│ → Thông báo: "Shipper đang trên đường    │
│    đến. SĐT: 0909123456"                 │
│                                          │
│ Trước khi giao 30 phút:                  │
│ → SMS: "Đơn hàng sẽ đến trong 30 phút,   │
│    vui lòng chuẩn bị nhận hàng"          │
│                                          │
│ Khi giao thành công:                     │
│ → Thông báo: "Đơn hàng đã giao thành công│
│    Cảm ơn chị đã mua hàng! ⭐"           │
│                                          │
│ → Khách luôn biết tình trạng đơn hàng    │
│ → Không cần gọi điện hỏi                 │
└──────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Giảm 90% thời gian phản hồi khách hàng (12 phút → 30 giây)
- ✅ Khách có thể tự tra cứu 24/7, không cần chờ NV
- ✅ Trải nghiệm mượt mà, liền mạch trên mọi kênh
- ✅ Tăng tỷ lệ chuyển đổi (khách không bỏ đi vì chờ lâu)
- ✅ Giảm tải cho nhân viên, tập trung vào tư vấn chuyên sâu

---

## **🎯 5. GIẢI PHÁP CHO VẤN ĐỀ VỀ BÁO CÁO & PHÂN TÍCH**

### **5.1 Vấn đề: Báo cáo thủ công**

**Pain Point hiện tại:**
- Cuối mỗi ngày, nhân viên phải mở Excel và tự tổng hợp doanh thu
- Nhân viên quên cập nhật hoặc tính sai số liệu
- Báo cáo doanh thu không chính xác
- Tốn thời gian, dễ sai sót

**Giải pháp đề xuất:**

**A. Automated Reporting (Báo cáo tự động)**

**🔧 Odoo Module:** `sale`, `account`, `stock`, `base` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Pre-built reports (Sales, Inventory, Accounting, HR)
- ✅ Scheduled actions cho auto-send reports
- ✅ Export to Excel/PDF
- ✅ Email reports automatically
- ✅ Custom report builder (Odoo Studio)

**1. Báo cáo tự động hàng ngày**

```
HỆ THỐNG TỰ ĐỘNG TẠO BÁO CÁO:
┌──────────────────────────────────────────┐
│ 📊 BÁO CÁO DOANH THU NGÀY 04/04/2026     │
├──────────────────────────────────────────┤
│ TỔNG QUAN:                               │
│ • Tổng doanh thu: 45,600,000 VNĐ         │
│   (↑ 15% so với hôm qua)                 │
│ • Số đơn hàng: 12 đơn                    │
│   (↑ 3 đơn so với hôm qua)               │
│ • Giá trị TB/đơn: 3,800,000 VNĐ          │
│   (↑ 8% so với hôm qua)                  │
│                                          │
│ THEO KÊNH:                               │
│ • Cửa hàng: 28,500,000 VNĐ (62%)         │
│ • Facebook: 12,100,000 VNĐ (27%)         │
│ • Website: 5,000,000 VNĐ (11%)           │
│                                          │
│ TOP SẢN PHẨM BÁN CHẠY:                   │
│ 1. Váy cưới A - 4 cái - 26,000,000 VNĐ   │
│ 2. Váy dạ hội B - 2 cái - 15,000,000 VNĐ │
│ 3. Áo dài C - 3 cái - 4,600,000 VNĐ      │
│                                          │
│ NHÂN VIÊN XUẤT SẮC:                      │
│ 🏆 NV Bán A - 5 đơn - 22,500,000 VNĐ     │
│ 🥈 NV Bán B - 4 đơn - 15,600,000 VNĐ     │
│ 🥉 NV Bán C - 3 đơn - 7,500,000 VNĐ      │
│                                          │
│ [Xuất Excel] [Xuất PDF] [Gửi email]      │
└──────────────────────────────────────────┘

→ Tự động tạo lúc 23:59 mỗi ngày
→ Tự động gửi email cho quản lý
→ Không cần nhân viên làm gì
```

**2. Scheduled Reports (Báo cáo định kỳ)**

```
LỊCH BÁO CÁO TỰ ĐỘNG:
┌──────────────────────────────────────────┐
│ 📅 LỊCH BÁO CÁO                          │
├──────────────────────────────────────────┤
│ HÀNG NGÀY (23:59):                       │
│ ✓ Báo cáo doanh thu ngày                 │
│ ✓ Báo cáo đơn hàng                       │
│ ✓ Báo cáo tồn kho                        │
│ → Gửi cho: Quản lý, Kế toán             │
│                                          │
│ HÀNG TUẦN (Chủ nhật 18:00):              │
│ ✓ Báo cáo doanh thu tuần                 │
│ ✓ Báo cáo hiệu suất nhân viên            │
│ ✓ Báo cáo sản phẩm bán chạy              │
│ → Gửi cho: Quản lý                       │
│                                          │
│ HÀNG THÁNG (Ngày 1 hàng tháng):          │
│ ✓ Báo cáo tài chính tháng                │
│ ✓ Báo cáo lợi nhuận                      │
│ ✓ Báo cáo khách hàng mới/cũ              │
│ ✓ Báo cáo tồn kho cuối tháng             │
│ → Gửi cho: Quản lý, Kế toán, Chủ shop   │
│                                          │
│ HÀNG QUÝ (Ngày 1 quý mới):               │
│ ✓ Báo cáo tổng quan kinh doanh           │
│ ✓ Phân tích xu hướng                     │
│ ✓ Đề xuất chiến lược                     │
│ → Gửi cho: Chủ shop, Ban giám đốc       │
│                                          │
│ [Thêm báo cáo] [Chỉnh sửa lịch]          │
└──────────────────────────────────────────┘
```

**3. Custom Reports (Báo cáo tùy chỉnh)**

```
TẠO BÁO CÁO TÙY CHỈNH:
┌──────────────────────────────────────────┐
│ 🔧 TẠO BÁO CÁO MỚI                       │
├──────────────────────────────────────────┤
│ Tên báo cáo: [Doanh thu theo sản phẩm]   │
│                                          │
│ Thời gian:                               │
│ • Từ: [01/01/2026] Đến: [31/03/2026]     │
│                                          │
│ Chỉ số cần xem:                          │
│ ☑️ Doanh thu                             │
│ ☑️ Số lượng bán                          │
│ ☑️ Lợi nhuận                             │
│ ☐ Tồn kho                                │
│                                          │
│ Nhóm theo:                               │
│ • [▼ Sản phẩm]                           │
│   (Sản phẩm, Loại SP, Nhân viên,...)    │
│                                          │
│ Lọc:                                     │
│ • Loại SP: [▼ Váy cưới]                  │
│ • Giá: [5tr] ─────●──── [10tr]          │
│                                          │
│ Hiển thị:                                │
│ • [▼ Biểu đồ cột]                        │
│   (Bảng, Biểu đồ cột, Biểu đồ tròn,...)│
│                                          │
│ [Xem trước] [Lưu] [Xuất file]            │
└──────────────────────────────────────────┘

→ Tạo báo cáo theo nhu cầu
→ Không cần biết Excel
```

**B. Export & Integration (Xuất dữ liệu & Tích hợp)**

**1. Xuất báo cáo đa định dạng**

```
XUẤT BÁO CÁO:
┌──────────────────────────────────────────┐
│ 📥 XUẤT BÁO CÁO                          │
├──────────────────────────────────────────┤
│ Định dạng:                               │
│ • 📊 Excel (.xlsx) - Để phân tích thêm   │
│ • 📄 PDF - Để in hoặc ký                 │
│ • 📧 Email - Gửi trực tiếp               │
│ • 🔗 Link chia sẻ - Xem online           │
│ • 📱 Google Sheets - Cộng tác            │
│                                          │
│ Tùy chọn:                                │
│ ☑️ Bao gồm biểu đồ                       │
│ ☑️ Bao gồm chi tiết đơn hàng             │
│ ☐ Bao gồm ảnh sản phẩm                   │
│                                          │
│ [Xuất ngay] [Lên lịch gửi định kỳ]       │
└──────────────────────────────────────────┘
```

**2. Tích hợp với phần mềm kế toán**

```
TÍCH HỢP KẾ TOÁN:
┌──────────────────────────────────────────┐
│ 🔗 ĐỒNG BỘ DỮ LIỆU KẾ TOÁN              │
├──────────────────────────────────────────┤
│ Tích hợp với:                            │
│ • MISA                                   │
│ • Fast Accounting                        │
│ • Bravo                                  │
│ • Excel (Tùy chỉnh)                      │
│                                          │
│ Tự động đồng bộ:                         │
│ ✓ Hóa đơn bán hàng                       │
│ ✓ Phiếu thu/chi                          │
│ ✓ Công nợ khách hàng                     │
│ ✓ Báo cáo doanh thu                      │
│                                          │
│ Tần suất đồng bộ:                        │
│ • [▼ Realtime] (Ngay lập tức)            │
│   (Realtime, Mỗi giờ, Mỗi ngày,...)     │
│                                          │
│ → Kế toán không cần nhập lại             │
│ → Dữ liệu luôn khớp                      │
└──────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Tiết kiệm 100% thời gian làm báo cáo thủ công
- ✅ Báo cáo chính xác 100%, không sai sót
- ✅ Báo cáo đúng giờ, không bao giờ quên
- ✅ Quản lý nắm được tình hình kinh doanh ngay lập tức

---

### **5.2 Vấn đề: Không có dashboard real-time**

**Pain Point hiện tại:**
- Chủ shop không thể xem ngay tình hình kinh doanh trong ngày
- Không biết doanh thu, số đơn hàng, sản phẩm bán chạy
- Không ra quyết định kịp thời

**Giải pháp đề xuất:**

**A. Real-time Dashboard (Bảng điều khiển thời gian thực)**

**🔧 Odoo Module:** `board`, `sale`, `stock`, `account` (Có sẵn - Không cần customize)

**Tính năng có sẵn trong Odoo:**
- ✅ Customizable dashboards
- ✅ Real-time KPI widgets
- ✅ Charts & graphs (line, bar, pie, pivot)
- ✅ Drill-down reports
- ✅ Mobile-responsive dashboards

**1. Dashboard tổng quan**

```
DASHBOARD TỔNG QUAN:
┌──────────────────────────────────────────────────────────────┐
│ 📊 BẢNG ĐIỀU KHIỂN - 04/04/2026 15:30                        │
├──────────────────────────────────────────────────────────────┤
│ DOANH THU HÔM NAY:                                           │
│ ┌────────────────────────────────────────────────────┐      │
│ │  💰 45,600,000 VNĐ    ↑ 15% vs hôm qua            │      │
│ │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░ 76% mục tiêu (60tr)        │      │
│ └────────────────────────────────────────────────────┘      │
│                                                              │
│ CHỈ SỐ CHÍNH:                                                │
│ ┌─────────────┬─────────────┬─────────────┬─────────────┐  │
│ │ 📦 ĐƠN HÀNG │ 👥 KHÁCH    │ 💵 GIÁ TB   │ 📈 LỢI NHUẬN│  │
│ │    12 đơn   │   10 khách  │  3.8tr/đơn  │   15.2tr    │  │
│ │   ↑ 3 đơn   │   ↑ 2 khách │   ↑ 8%      │   ↑ 12%     │  │
│ └─────────────┴─────────────┴─────────────┴─────────────┘  │
│                                                              │
│ DOANH THU THEO GIỜ:                                          │
│ ┌────────────────────────────────────────────────────┐      │
│ │ 10tr│                                        ●      │      │
│ │  8tr│                              ●    ●           │      │
│ │  6tr│                    ●    ●                    │      │
│ │  4tr│          ●    ●                              │      │
│ │  2tr│    ●                                         │      │
│ │  0  └────┴────┴────┴────┴────┴────┴────┴────      │      │
│ │     9h  10h  11h  12h  13h  14h  15h  16h          │      │
│ └────────────────────────────────────────────────────┘      │
│                                                              │
│ TOP SẢN PHẨM BÁN CHẠY HÔM NAY:                               │
│ ┌────────────────────────────────────────────────────┐      │
│ │ 1. 👗 Váy cưới A       4 cái    26,000,000 VNĐ     │      │
│ │ 2. 👗 Váy dạ hội B     2 cái    15,000,000 VNĐ     │      │
│ │ 3. 👘 Áo dài C         3 cái     4,600,000 VNĐ     │      │
│ └────────────────────────────────────────────────────┘      │
│                                                              │
│ CẢNH BÁO:                                                    │
│ ┌────────────────────────────────────────────────────┐      │
│ │ ⚠️ Váy cưới A sắp hết hàng (Còn 2 cái)             │      │
│ │ ⚠️ 3 đơn hàng chưa xử lý                           │      │
│ │ ✓ Tồn kho ổn định                                  │      │
│ └────────────────────────────────────────────────────┘      │
│                                                              │
│ [Xem chi tiết] [Xuất báo cáo] [Cài đặt]                      │
└──────────────────────────────────────────────────────────────┘

→ Cập nhật mỗi 30 giây
→ Xem được trên máy tính, điện thoại, tablet
→ Chủ shop biết ngay tình hình kinh doanh
```

**2. Dashboard theo vai trò**

```
DASHBOARD THEO VAI TRÒ:

┌─────────────────────────────────────────┐
│ CHỦ SHOP - Dashboard                    │
├─────────────────────────────────────────┤
│ • Doanh thu, lợi nhuận                  │
│ • Hiệu suất nhân viên                   │
│ • Tình hình tồn kho                     │
│ • Khách hàng mới/cũ                     │
│ • So sánh với tháng trước               │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ QUẢN LÝ BÁN HÀNG - Dashboard            │
├─────────────────────────────────────────┤
│ • Số đơn hàng trong ngày                │
│ • Đơn hàng đang xử lý                   │
│ • Hiệu suất từng nhân viên              │
│ • Khách hàng cần follow-up              │
│ • Lead mới cần xử lý                    │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ NHÂN VIÊN BÁN HÀNG - Dashboard          │
├─────────────────────────────────────────┤
│ • Đơn hàng của tôi                      │
│ • Mục tiêu cá nhân (KPI)                │
│ • Khách hàng cần chăm sóc hôm nay       │
│ • Hoa hồng dự kiến                      │
│ • Xếp hạng so với đồng nghiệp           │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ NHÂN VIÊN KHO - Dashboard               │
├─────────────────────────────────────────┤
│ • Đơn hàng cần đóng gói                 │
│ • Sản phẩm sắp hết hàng                 │
│ • Lịch nhập hàng                        │
│ • Vị trí sản phẩm trong kho             │
│ • Yêu cầu kiểm kho                      │
└─────────────────────────────────────────┘

→ Mỗi người thấy thông tin phù hợp vai trò
```

**B. Mobile Dashboard (Dashboard trên di động)**

**1. App mobile cho chủ shop**

```
📱 APP MOBILE - CHỦ SHOP:
┌────────────────────────────┐
│ ≡  DASHBOARD    🔔 (3)  👤 │
├────────────────────────────┤
│ Hôm nay - 04/04/2026       │
│                            │
│ 💰 DOANH THU               │
│ ┌────────────────────────┐ │
│ │ 45,600,000 VNĐ         │ │
│ │ ▓▓▓▓▓▓▓▓░░ 76% mục tiêu│ │
│ │ ↑ 15% vs hôm qua       │ │
│ └────────────────────────┘ │
│                            │
│ 📊 CHỈ SỐ                  │
│ ┌──────────┬──────────┐   │
│ │ 📦 12 đơn│👥 10 KH  │   │
│ │ ↑ 3 đơn  │↑ 2 khách │   │
│ └──────────┴──────────┘   │
│ ┌──────────┬──────────┐   │
│ │💵 3.8tr/đơn│📈 15.2tr│   │
│ │ ↑ 8%     │↑ 12%     │   │
│ └──────────┴──────────┘   │
│                            │
│ ⚠️ CẢNH BÁO (2)            │
│ • Váy A sắp hết (2 cái)    │
│ • 3 đơn chưa xử lý         │
│                            │
│ 📈 TOP SẢN PHẨM            │
│ 1. Váy cưới A - 26tr       │
│ 2. Váy dạ hội B - 15tr     │
│ 3. Áo dài C - 4.6tr        │
│                            │
│ [Xem chi tiết →]           │
└────────────────────────────┘

→ Chủ shop xem mọi lúc mọi nơi
→ Nhận thông báo realtime
→ Ra quyết định nhanh
```

**C. KPI Tracking (Theo dõi chỉ tiêu)**

**1. Thiết lập KPI**

```
THIẾT LẬP KPI:
┌──────────────────────────────────────────┐
│ 🎯 THIẾT LẬP MỤC TIÊU                    │
├──────────────────────────────────────────┤
│ MỤC TIÊU THÁNG 4/2026:                   │
│                                          │
│ Doanh thu:                               │
│ • Mục tiêu: [1,500,000,000] VNĐ          │
│ • Hiện tại: 456,000,000 VNĐ (30%)        │
│ • Còn lại: 1,044,000,000 VNĐ             │
│ • Dự kiến: Đạt 95% (Cần tăng tốc)        │
│                                          │
│ Số đơn hàng:                             │
│ • Mục tiêu: [300] đơn                    │
│ • Hiện tại: 98 đơn (33%)                 │
│ • Còn lại: 202 đơn                       │
│ • Dự kiến: Đạt 100% ✓                    │
│                                          │
│ Khách hàng mới:                          │
│ • Mục tiêu: [100] khách                  │
│ • Hiện tại: 45 khách (45%)               │
│ • Còn lại: 55 khách                      │
│ • Dự kiến: Đạt 110% ✓                    │
│                                          │
│ Tỷ lệ chốt đơn:                          │
│ • Mục tiêu: [60]%                        │
│ • Hiện tại: 58%                          │
│ • Chênh lệch: -2%                        │
│                                          │
│ [Lưu] [Phân bổ cho nhân viên]            │
└──────────────────────────────────────────┘
```

**2. Theo dõi KPI realtime**

```
THEO DÕI KPI:
┌──────────────────────────────────────────┐
│ 📊 TIẾN ĐỘ MỤC TIÊU THÁNG 4/2026         │
├──────────────────────────────────────────┤
│ DOANH THU:                               │
│ ▓▓▓▓▓▓░░░░░░░░░░░░░░ 30% (456tr/1,500tr)│
│ 🔴 Chậm tiến độ (Cần đạt 40% vào ngày 12)│
│                                          │
│ SỐ ĐƠN HÀNG:                             │
│ ▓▓▓▓▓▓▓░░░░░░░░░░░░░ 33% (98/300 đơn)   │
│ 🟢 Đúng tiến độ                          │
│                                          │
│ KHÁCH HÀNG MỚI:                          │
│ ▓▓▓▓▓▓▓▓▓░░░░░░░░░░░ 45% (45/100 khách) │
│ 🟢 Vượt tiến độ                          │
│                                          │
│ TỶ LỆ CHỐT ĐƠN:                          │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ 58% (Mục tiêu 60%)  │
│ 🟡 Gần đạt                               │
│                                          │
│ KHUYẾN NGHỊ:                             │
│ • Tăng cường marketing để tăng doanh thu │
│ • Tập trung chốt đơn từ lead hiện có     │
│ • Duy trì chiến lược thu hút khách mới   │
│                                          │
│ [Xem chi tiết] [Điều chỉnh mục tiêu]     │
└──────────────────────────────────────────┘
```

**D. Alerts & Notifications (Cảnh báo & Thông báo)**

**1. Cảnh báo thông minh**

```
HỆ THỐNG CẢNH BÁO:
┌──────────────────────────────────────────┐
│ 🔔 CẢNH BÁO TỰ ĐỘNG                     │
├──────────────────────────────────────────┤
│ DOANH THU:                               │
│ 🔴 Doanh thu hôm nay thấp hơn 30% so với │
│    trung bình → Cần kiểm tra nguyên nhân │
│                                          │
│ 🟢 Doanh thu tuần này cao hơn 20% so với │
│    tuần trước → Chiến lược hiệu quả!     │
│                                          │
│ TỒN KHO:                                 │
│ 🔴 5 sản phẩm sắp hết hàng               │
│    → Cần nhập hàng gấp                   │
│                                          │
│ 🟡 10 sản phẩm tồn kho > 6 tháng         │
│    → Cân nhắc giảm giá thanh lý          │
│                                          │
│ ĐƠN HÀNG:                                │
│ 🔴 3 đơn hàng quá hạn xử lý              │
│    → Cần xử lý ngay                      │
│                                          │
│ 🟡 5 đơn hàng giao chậm                  │
│    → Liên hệ shipper                     │
│                                          │
│ KHÁCH HÀNG:                              │
│ 🟡 15 lead chưa follow-up quá 3 ngày     │
│    → Có thể mất khách                    │
│                                          │
│ 🟢 10 khách VIP có sinh nhật tuần này    │
│    → Gửi lời chúc + voucher              │
│                                          │
│ [Xử lý ngay] [Tắt thông báo]             │
└──────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Chủ shop nắm được tình hình kinh doanh realtime
- ✅ Ra quyết định nhanh dựa trên dữ liệu chính xác
- ✅ Phát hiện vấn đề sớm, xử lý kịp thời
- ✅ Theo dõi KPI, đảm bảo đạt mục tiêu
- ✅ Xem được mọi lúc mọi nơi (mobile app)

---

### **5.3 Vấn đề: Không phân tích được xu hướng**

**Pain Point hiện tại:**
- Shop không có công cụ để phân tích dữ liệu bán hàng theo thời gian
- Không biết sản phẩm nào bán chạy theo tuần/tháng
- Không biết size nào được ưa chuộng, mùa nào bán tốt
- Phân tích nếu có chỉ dựa vào cảm tính, không chính xác

**Giải pháp đề xuất:**

**A. Advanced Analytics (Phân tích nâng cao)**

**1. Sales Trend Analysis (Phân tích xu hướng bán hàng)**

```
PHÂN TÍCH XU HƯỚNG:
┌──────────────────────────────────────────────────────────────┐
│ 📈 PHÂN TÍCH XU HƯỚNG BÁN HÀNG - Q1/2026                     │
├──────────────────────────────────────────────────────────────┤
│ DOANH THU THEO THÁNG:                                        │
│ ┌────────────────────────────────────────────────────┐      │
│ │ 80tr│                                        ●      │      │
│ │ 60tr│                              ●                │      │
│ │ 40tr│                    ●                          │      │
│ │ 20tr│          ●                                    │      │
│ │  0  └────┴────┴────┴────┴────┴────┴────            │      │
│ │     T10  T11  T12  T1   T2   T3   T4               │      │
│ └────────────────────────────────────────────────────┘      │
│                                                              │
│ NHẬN XÉT:                                                    │
│ • Doanh thu tăng đều qua các tháng                           │
│ • Tháng 3 tăng mạnh 35% (Mùa cưới)                           │
│ • Dự đoán: Tháng 4-5 tiếp tục tăng                           │
│                                                              │
│ SẢN PHẨM BÁN CHẠY THEO THỜI GIAN:                            │
│ ┌────────────────────────────────────────────────────┐      │
│ │ Tháng 1: Váy cưới truyền thống (Tết)               │      │
│ │ Tháng 2: Áo dài cưới (Sau Tết)                     │      │
│ │ Tháng 3: Váy cưới cách tân (Mùa cưới bắt đầu)      │      │
│ │ Dự đoán T4: Váy cưới + Phụ kiện (Cao điểm cưới)    │      │
│ └────────────────────────────────────────────────────┘      │
│                                                              │
│ KHUYẾN NGHỊ:                                                 │
│ ✓ Nhập thêm váy cưới cách tân (Bán chạy T3-T5)               │
│ ✓ Chuẩn bị phụ kiện đầy đủ (Khách mua kèm nhiều)             │
│ ✓ Giảm giá áo dài (Qua mùa)                                  │
│                                                              │
│ [Xem chi tiết] [Xuất báo cáo] [Lên kế hoạch]                 │
└──────────────────────────────────────────────────────────────┘
```

**2. Product Performance Analysis (Phân tích hiệu suất sản phẩm)**

```
PHÂN TÍCH SẢN PHẨM:
┌──────────────────────────────────────────┐
│ 📦 PHÂN TÍCH SẢN PHẨM - Q1/2026          │
├──────────────────────────────────────────┤
│ TOP 10 SẢN PHẨM BÁN CHẠY:                │
│                                          │
│ 1. Váy cưới A                            │
│    • Doanh thu: 156,000,000 VNĐ          │
│    • Số lượng: 24 cái                    │
│    • Tăng trưởng: ↑ 45% vs Q4/2025       │
│    • Tỷ lệ chốt: 75% (Rất cao)           │
│    • Size bán chạy: M (60%), L (30%)     │
│    • Màu bán chạy: Trắng (80%)           │
│    💡 Nhập thêm size M màu trắng         │
│                                          │
│ 2. Váy dạ hội B                          │
│    • Doanh thu: 128,000,000 VNĐ          │
│    • Số lượng: 16 cái                    │
│    • Tăng trưởng: ↑ 20% vs Q4/2025       │
│    • Tỷ lệ chốt: 65%                     │
│    • Size bán chạy: S (50%), M (40%)     │
│    • Màu bán chạy: Đỏ (60%), Đen (30%)   │
│    💡 Duy trì tồn kho hiện tại           │
│                                          │
│ ...                                      │
│                                          │
│ SẢN PHẨM BÁN CHẬM (Cần xem xét):         │
│                                          │
│ 1. Váy X - Tồn kho 8 tháng               │
│    💡 Giảm giá 30% để thanh lý           │
│                                          │
│ 2. Áo dài Y - Không bán được trong Q1    │
│    💡 Ngừng nhập, xem xét loại bỏ        │
│                                          │
│ [Xem tất cả] [Xuất báo cáo]              │
└──────────────────────────────────────────┘
```

**3. Customer Behavior Analysis (Phân tích hành vi khách hàng)**

```
PHÂN TÍCH KHÁCH HÀNG:
┌──────────────────────────────────────────┐
│ 👥 PHÂN TÍCH HÀNH VI KHÁCH HÀNG          │
├──────────────────────────────────────────┤
│ PHÂN KHÚC KHÁCH HÀNG:                    │
│                                          │
│ 🏆 VIP (5%): 15 khách                    │
│    • Doanh thu: 487,500,000 VNĐ (40%)    │
│    • TB/khách: 32,500,000 VNĐ            │
│    • Tần suất: 5 lần/năm                 │
│    💡 Chăm sóc đặc biệt, tặng quà VIP    │
│                                          │
│ 💎 KHÁCH QUEN (15%): 45 khách            │
│    • Doanh thu: 364,500,000 VNĐ (30%)    │
│    • TB/khách: 8,100,000 VNĐ             │
│    • Tần suất: 3 lần/năm                 │
│    💡 Gửi voucher, khuyến khích mua thêm │
│                                          │
│ 🆕 KHÁCH MỚI (80%): 240 khách            │
│    • Doanh thu: 365,000,000 VNĐ (30%)    │
│    • TB/khách: 1,520,000 VNĐ             │
│    • Tần suất: 1 lần                     │
│    💡 Chăm sóc để chuyển thành khách quen│
│                                          │
│ HÀNH VI MUA HÀNG:                        │
│                                          │
│ Thời gian mua nhiều nhất:                │
│ • Thứ 7, Chủ nhật: 45%                   │
│ • Thứ 6: 25%                             │
│ • Các ngày khác: 30%                     │
│ 💡 Tăng nhân sự cuối tuần                │
│                                          │
│ Giờ mua nhiều nhất:                      │
│ • 14:00-17:00: 40%                       │
│ • 10:00-12:00: 30%                       │
│ • 18:00-20:00: 20%                       │
│ 💡 Chuẩn bị hàng trước 14:00             │
│                                          │
│ Kênh mua hàng:                           │
│ • Cửa hàng: 60%                          │
│ • Facebook: 30%                          │
│ • Website: 10%                           │
│ 💡 Đầu tư thêm vào Facebook marketing    │
│                                          │
│ [Xem chi tiết] [Xuất báo cáo]            │
└──────────────────────────────────────────┘
```

**B. Predictive Analytics (Phân tích dự đoán)**

**1. Demand Forecasting (Dự báo nhu cầu)**

```
DỰ BÁO NHU CẦU:
┌──────────────────────────────────────────┐
│ 🔮 DỰ BÁO NHU CẦU THÁNG 5/2026           │
├──────────────────────────────────────────┤
│ Dựa trên:                                │
│ • Dữ liệu 12 tháng qua                   │
│ • Xu hướng mùa vụ                        │
│ • Sự kiện đặc biệt (Lễ, Tết,...)         │
│ • Tình hình kinh tế                      │
│                                          │
│ DỰ ĐOÁN DOANH THU:                       │
│ • Dự kiến: 85,000,000 VNĐ                │
│ • Khoảng tin cậy: 80-90tr                │
│ • Tăng trưởng: ↑ 18% vs T5/2025          │
│ • Độ chính xác: 92%                      │
│                                          │
│ SẢN PHẨM SẼ BÁN CHẠY:                    │
│                                          │
│ 1. Váy cưới cách tân                     │
│    • Dự kiến: 30 cái                     │
│    • Cần nhập: 35 cái (Dự phòng)         │
│    • Ưu tiên: Size M, màu trắng/hồng     │
│                                          │
│ 2. Phụ kiện cưới                         │
│    • Dự kiến: 50 bộ                      │
│    • Cần nhập: 60 bộ                     │
│    • Ưu tiên: Khăn voan, hoa cài         │
│                                          │
│ 3. Váy dạ hội                            │
│    • Dự kiến: 15 cái                     │
│    • Cần nhập: 18 cái                    │
│    • Ưu tiên: Size S/M, màu đỏ/đen       │
│                                          │
│ SẢN PHẨM SẼ BÁN CHẬM:                    │
│ • Áo dài (Qua mùa Tết)                   │
│ • Váy cưới truyền thống (Ít người chọn)  │
│ 💡 Không nhập thêm, giảm giá thanh lý    │
│                                          │
│ [Tạo đơn nhập hàng] [Xuất báo cáo]       │
└──────────────────────────────────────────┘
```

**2. Churn Prediction (Dự đoán khách rời bỏ)**

```
DỰ ĐOÁN KHÁCH RỜI BỎ:
┌──────────────────────────────────────────┐
│ ⚠️ KHÁCH HÀNG CÓ NGUY CƠ RỜI BỎ          │
├──────────────────────────────────────────┤
│ Hệ thống phát hiện 12 khách có nguy cơ   │
│ cao không quay lại mua hàng:             │
│                                          │
│ 1. Nguyễn Thị B - VIP                    │
│    • Lần mua cuối: 6 tháng trước         │
│    • Nguy cơ: 85% (Rất cao)              │
│    • Lý do: Lâu không mua, không tương tác│
│    • Giá trị: 32,500,000 VNĐ (Quan trọng)│
│    💡 Hành động:                          │
│       ☐ Gọi điện hỏi thăm                │
│       ☐ Gửi voucher 20% (Đặc biệt)       │
│       ☐ Mời tham gia sự kiện VIP         │
│    [Thực hiện ngay]                      │
│                                          │
│ 2. Trần Thị C - Khách quen               │
│    • Lần mua cuối: 4 tháng trước         │
│    • Nguy cơ: 65% (Cao)                  │
│    • Lý do: Tần suất mua giảm            │
│    • Giá trị: 15,000,000 VNĐ             │
│    💡 Hành động:                          │
│       ☐ Gửi email khảo sát               │
│       ☐ Gửi voucher 15%                  │
│    [Thực hiện ngay]                      │
│                                          │
│ ...                                      │
│                                          │
│ TỔNG GIÁ TRỊ CÓ THỂ MẤT: 180,000,000 VNĐ │
│                                          │
│ [Xem tất cả] [Gửi email hàng loạt]       │
└──────────────────────────────────────────┘
```

**C. Comparative Analysis (Phân tích so sánh)**

**1. So sánh theo thời gian**

```
SO SÁNH THEO THỜI GIAN:
┌──────────────────────────────────────────┐
│ 📊 SO SÁNH HIỆU SUẤT                     │
├──────────────────────────────────────────┤
│ THÁNG 4/2026 vs THÁNG 3/2026:            │
│                                          │
│ Doanh thu:                               │
│ • T4: 45,600,000 VNĐ (4 ngày)            │
│ • T3: 78,500,000 VNĐ (31 ngày)           │
│ • TB/ngày T4: 11,400,000 VNĐ             │
│ • TB/ngày T3: 2,532,000 VNĐ              │
│ • Tăng trưởng: ↑ 350% 🚀                 │
│ 💡 Tháng 4 bắt đầu rất tốt!              │
│                                          │
│ Số đơn hàng:                             │
│ • T4: 12 đơn (4 ngày)                    │
│ • T3: 52 đơn (31 ngày)                   │
│ • TB/ngày T4: 3 đơn                      │
│ • TB/ngày T3: 1.7 đơn                    │
│ • Tăng trưởng: ↑ 76%                     │
│                                          │
│ Giá trị TB/đơn:                          │
│ • T4: 3,800,000 VNĐ                      │
│ • T3: 1,509,000 VNĐ                      │
│ • Tăng trưởng: ↑ 152% 🚀                 │
│ 💡 Khách mua sản phẩm giá cao hơn        │
│                                          │
│ THÁNG 4/2026 vs THÁNG 4/2025:            │
│                                          │
│ Doanh thu:                               │
│ • T4/2026: 45,600,000 VNĐ (4 ngày)       │
│ • T4/2025: 28,000,000 VNĐ (4 ngày)       │
│ • Tăng trưởng: ↑ 63% 🎉                  │
│ 💡 Tăng trưởng tốt so với năm ngoái      │
│                                          │
│ [Xem chi tiết] [Xuất báo cáo]            │
└──────────────────────────────────────────┘
```

**2. Benchmarking (So sánh với thị trường)**

```
SO SÁNH VỚI THỊ TRƯỜNG:
┌──────────────────────────────────────────┐
│ 📈 BENCHMARKING - Q1/2026                │
├──────────────────────────────────────────┤
│ So với trung bình ngành váy cưới:        │
│                                          │
│ Tăng trưởng doanh thu:                   │
│ • Shop: ↑ 35%                            │
│ • Ngành: ↑ 20%                           │
│ • Đánh giá: ✓ Vượt trội                  │
│                                          │
│ Tỷ lệ chốt đơn:                          │
│ • Shop: 58%                              │
│ • Ngành: 45%                             │
│ • Đánh giá: ✓ Tốt hơn                    │
│                                          │
│ Giá trị TB/đơn:                          │
│ • Shop: 6,500,000 VNĐ                    │
│ • Ngành: 5,800,000 VNĐ                   │
│ • Đánh giá: ✓ Cao hơn                    │
│                                          │
│ Tỷ lệ khách quay lại:                    │
│ • Shop: 25%                              │
│ • Ngành: 35%                             │
│ • Đánh giá: ⚠️ Cần cải thiện             │
│ 💡 Tăng cường chăm sóc khách hàng        │
│                                          │
│ Thời gian xử lý đơn:                     │
│ • Shop: 2 giờ                            │
│ • Ngành: 4 giờ                           │
│ • Đánh giá: ✓ Nhanh hơn                  │
│                                          │
│ [Xem chi tiết] [Xuất báo cáo]            │
└──────────────────────────────────────────┘
```

**D. AI-Powered Insights (Thông tin thông minh từ AI)**

**1. Tự động phát hiện insight**

```
AI INSIGHTS:
┌──────────────────────────────────────────┐
│ 🤖 THÔNG TIN THÔNG MINH TỪ AI            │
├──────────────────────────────────────────┤
│ Hệ thống AI phát hiện 5 insight quan trọng:│
│                                          │
│ 💡 INSIGHT 1: Cơ hội tăng doanh thu      │
│    "Khách mua váy cưới có 70% khả năng   │
│     mua thêm phụ kiện nếu được gợi ý     │
│     ngay sau khi chọn váy"               │
│    → Khuyến nghị: Train NV gợi ý phụ kiện│
│    → Tiềm năng: +15,000,000 VNĐ/tháng    │
│                                          │
│ 💡 INSIGHT 2: Xu hướng mới                │
│    "Váy cưới màu hồng pastel tăng 120%   │
│     trong 2 tháng qua, đang là xu hướng" │
│    → Khuyến nghị: Nhập thêm váy hồng     │
│    → Tiềm năng: +20,000,000 VNĐ/tháng    │
│                                          │
│ 💡 INSIGHT 3: Tối ưu giá                  │
│    "Sản phẩm trong khoảng 6-7tr có tỷ lệ │
│     chốt cao nhất (75%), nên tập trung   │
│     vào phân khúc này"                   │
│    → Khuyến nghị: Tăng sản phẩm 6-7tr    │
│    → Tiềm năng: +10% tỷ lệ chốt          │
│                                          │
│ 💡 INSIGHT 4: Rủi ro tồn kho              │
│    "5 sản phẩm có nguy cơ tồn kho lâu    │
│     (>6 tháng), nên giảm giá sớm"        │
│    → Khuyến nghị: Flash sale 30% off     │
│    → Tiết kiệm: 8,000,000 VNĐ vốn        │
│                                          │
│ 💡 INSIGHT 5: Cơ hội marketing            │
│    "Khách hàng VIP có sinh nhật trong    │
│     tháng này, gửi voucher có thể tăng   │
│     80% khả năng mua lại"                │
│    → Khuyến nghị: Gửi voucher 15%        │
│    → Tiềm năng: +12,000,000 VNĐ          │
│                                          │
│ [Áp dụng tất cả] [Xem thêm insight]      │
└──────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Hiểu rõ xu hướng thị trường, hành vi khách hàng
- ✅ Dự đoán nhu cầu chính xác, nhập hàng đúng lúc
- ✅ Phát hiện cơ hội kinh doanh mới
- ✅ Tối ưu hóa tồn kho, giảm rủi ro
- ✅ Ra quyết định dựa trên dữ liệu, không cảm tính
- ✅ AI tự động phát hiện insight, tiết kiệm thời gian phân tích

---

## **🎯 6. GIẢI PHÁP CHO VẤN ĐỀ VỀ THANH TOÁN**

### **6.1 Vấn đề: Đối soát thanh toán thủ công**

**Pain Point hiện tại:**
- Cuối ngày phải đối chiếu tiền mặt, chuyển khoản, COD với đơn hàng trên Excel thủ công
- Tốn thời gian, dễ sai sót, nhầm lẫn hoặc bỏ sót giao dịch
- Không biết đơn nào đã thanh toán, đơn nào chưa

**Giải pháp đề xuất:**

**A. Hệ thống quản lý thanh toán tự động**

**Odoo Module:** `account` (Accounting), `account_payment` (Payment Management)

**Tính năng:**
- Tự động ghi nhận thanh toán khi tạo đơn hàng
- Liên kết thanh toán với đơn hàng, cập nhật trạng thái tự động
- Dashboard theo dõi thanh toán theo thời gian thực

**Ví dụ giao diện:**

```
┌─────────────────────────────────────────┐
│ QUẢN LÝ THANH TOÁN                      │
├─────────────────────────────────────────┤
│ Hôm nay: 15/01/2024                     │
│                                         │
│ 💰 Tổng thu: 45,000,000 VNĐ             │
│   • Tiền mặt: 15,000,000 (5 đơn)        │
│   • Chuyển khoản: 20,000,000 (8 đơn)    │
│   • COD: 10,000,000 (4 đơn)             │
│                                         │
│ ⏳ Chờ thanh toán: 12,000,000 VNĐ (3 đơn)│
│ ✅ Đã thanh toán: 17 đơn                │
│ ❌ Quá hạn: 2 đơn (cảnh báo)            │
│                                         │
│ [Xem chi tiết] [Đối soát] [Báo cáo]     │
└─────────────────────────────────────────┘
```

**B. Đối soát tự động cuối ngày**

**Customize Python:**
```python
# Module: custom_payment_reconciliation
def auto_reconcile_daily_payments():
    """Tự động đối soát thanh toán cuối ngày"""
    today = fields.Date.today()
    
    # Lấy tất cả thanh toán trong ngày
    payments = self.env['account.payment'].search([
        ('date', '=', today),
        ('state', '=', 'posted')
    ])
    
    # Tính tổng theo phương thức
    cash_total = sum(p.amount for p in payments if p.payment_method_code == 'cash')
    bank_total = sum(p.amount for p in payments if p.payment_method_code == 'bank')
    cod_total = sum(p.amount for p in payments if p.payment_method_code == 'cod')
    
    # Tạo báo cáo đối soát
    reconciliation = self.env['payment.reconciliation'].create({
        'date': today,
        'cash_amount': cash_total,
        'bank_amount': bank_total,
        'cod_amount': cod_total,
        'total_amount': cash_total + bank_total + cod_total,
        'state': 'draft'
    })
    
    return reconciliation
```

**Lợi ích:**
- ✅ Tiết kiệm 90% thời gian đối soát (từ 30 phút → 3 phút)
- ✅ Độ chính xác 100%, không bỏ sót giao dịch
- ✅ Cảnh báo tự động khi có sai lệch
- ✅ Báo cáo chi tiết theo từng phương thức thanh toán

---

### **6.2 Vấn đề: Không tích hợp cổng thanh toán**

**Pain Point hiện tại:**
- Khách chuyển khoản xong phải chụp ảnh gửi qua Zalo/Facebook
- Nhân viên phải kiểm tra thủ công từng ảnh, đối chiếu với số tiền đơn hàng
- Mất thời gian, dễ nhầm lẫn

**Giải pháp đề xuất:**

**A. Tích hợp cổng thanh toán online**

**Odoo Module:** `payment` (Payment Acquirer)

**Cổng thanh toán hỗ trợ:**
- VNPay
- MoMo
- ZaloPay
- Banking (chuyển khoản ngân hàng)

**Customize Python - Tích hợp VNPay:**
```python
# Module: payment_vnpay
from odoo import models, fields, api
import hashlib
import urllib.parse

class PaymentAcquirerVNPay(models.Model):
    _inherit = 'payment.acquirer'
    
    provider = fields.Selection(
        selection_add=[('vnpay', 'VNPay')],
        ondelete={'vnpay': 'set default'}
    )
    vnpay_tmn_code = fields.Char('VNPay TMN Code')
    vnpay_hash_secret = fields.Char('VNPay Hash Secret')
    
    def vnpay_get_form_action_url(self):
        """Tạo URL thanh toán VNPay"""
        return 'https://sandbox.vnpayment.vn/paymentv2/vpcpay.html'
    
    def vnpay_form_generate_values(self, values):
        """Tạo form data cho VNPay"""
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        
        vnpay_data = {
            'vnp_Version': '2.1.0',
            'vnp_Command': 'pay',
            'vnp_TmnCode': self.vnpay_tmn_code,
            'vnp_Amount': int(values['amount'] * 100),  # VNPay tính theo đồng
            'vnp_CurrCode': 'VND',
            'vnp_TxnRef': values['reference'],
            'vnp_OrderInfo': f"Thanh toan don hang {values['reference']}",
            'vnp_OrderType': 'billpayment',
            'vnp_Locale': 'vn',
            'vnp_ReturnUrl': f"{base_url}/payment/vnpay/return",
            'vnp_IpAddr': '127.0.0.1',
        }
        
        # Tạo secure hash
        vnpay_data['vnp_SecureHash'] = self._vnpay_generate_signature(vnpay_data)
        
        return vnpay_data
```

**Quy trình thanh toán:**

```
1. Khách chọn "Thanh toán online"
   ↓
2. Chọn cổng thanh toán (VNPay/MoMo/ZaloPay)
   ↓
3. Hệ thống tạo link thanh toán → Gửi cho khách
   ↓
4. Khách thanh toán trên app/web của cổng thanh toán
   ↓
5. Cổng thanh toán gửi kết quả về hệ thống
   ↓
6. Hệ thống tự động cập nhật trạng thái đơn hàng
   ↓
7. Gửi thông báo cho khách và nhân viên
```

**B. Quét mã QR thanh toán**

**Customize Python:**
```python
# Module: payment_qr_code
import qrcode
from io import BytesIO
import base64

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    qr_code_image = fields.Binary('QR Code', compute='_compute_qr_code')
    
    def _compute_qr_code(self):
        """Tạo mã QR cho thanh toán chuyển khoản"""
        for order in self:
            if order.state in ['sale', 'sent']:
                # Tạo nội dung QR theo chuẩn VietQR
                bank_info = self.env.company.bank_ids[0]
                qr_content = f"Bank:{bank_info.bank_id.name}|Account:{bank_info.acc_number}|Amount:{order.amount_total}|Message:{order.name}"
                
                # Tạo QR code
                qr = qrcode.QRCode(version=1, box_size=10, border=5)
                qr.add_data(qr_content)
                qr.make(fit=True)
                
                img = qr.make_image(fill_color="black", back_color="white")
                buffer = BytesIO()
                img.save(buffer, format='PNG')
                order.qr_code_image = base64.b64encode(buffer.getvalue())
```

**Hiển thị QR Code:**

```
┌─────────────────────────────────────────┐
│ THANH TOÁN ĐỠN HÀNG #SO001              │
├─────────────────────────────────────────┤
│ Tổng tiền: 5,000,000 VNĐ                │
│                                         │
│ Quét mã QR để thanh toán:               │
│                                         │
│        ┌─────────────┐                  │
│        │  ▄▄▄▄▄▄▄▄▄  │                  │
│        │  █ ▄▄▄ █ ▀█ │                  │
│        │  █ ███ █ ▄▄ │                  │
│        │  █▄▄▄▄▄█ ▀ █ │                  │
│        │  ▄▄ ▄ ▄ ▄▄▄▄ │                  │
│        │  ▀▄█▀▀▀█▄▀▀  │                  │
│        │  ▄▄▄▄▄▄▄ █▀  │                  │
│        └─────────────┘                  │
│                                         │
│ Hoặc chuyển khoản thủ công:             │
│ • Ngân hàng: Vietcombank                │
│ • Số TK: 1234567890                     │
│ • Nội dung: SO001                       │
│                                         │
│ [Tôi đã thanh toán] [Hủy]               │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Khách thanh toán nhanh chóng, tiện lợi
- ✅ Tự động cập nhật trạng thái, không cần kiểm tra thủ công
- ✅ Giảm 95% thời gian xác nhận thanh toán
- ✅ Tăng tỷ lệ chốt đơn (thanh toán dễ dàng hơn)

---

### **6.3 Vấn đề: Khó đối chiếu COD**

**Pain Point hiện tại:**
- Phải đợi đơn vị vận chuyển gửi file đối soát (3-7 ngày)
- Khó kiểm tra ngay đơn nào đã thu tiền, đơn nào chưa
- Dễ bị thiếu sót, mất tiền

**Giải pháp đề xuất:**

**A. Tích hợp API đơn vị vận chuyển**

**Odoo Module:** `delivery` (Delivery Methods)

**Customize Python - Tích hợp GHN (Giao Hàng Nhanh):**
```python
# Module: delivery_ghn
import requests

class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'
    
    delivery_type = fields.Selection(
        selection_add=[('ghn', 'Giao Hàng Nhanh')],
        ondelete={'ghn': 'set default'}
    )
    ghn_token = fields.Char('GHN API Token')
    ghn_shop_id = fields.Char('GHN Shop ID')
    
    def ghn_create_order(self, picking):
        """Tạo đơn hàng trên GHN"""
        url = "https://dev-online-gateway.ghn.vn/shiip/public-api/v2/shipping-order/create"
        
        headers = {
            'Token': self.ghn_token,
            'ShopId': self.ghn_shop_id,
            'Content-Type': 'application/json'
        }
        
        data = {
            'to_name': picking.partner_id.name,
            'to_phone': picking.partner_id.phone,
            'to_address': picking.partner_id.street,
            'cod_amount': int(picking.sale_id.amount_total) if picking.sale_id.payment_term_id.name == 'COD' else 0,
            'content': f"Don hang {picking.sale_id.name}",
            'weight': int(picking.weight * 1000),  # Gram
            'service_type_id': 2,  # Giao hàng tiêu chuẩn
        }
        
        response = requests.post(url, json=data, headers=headers)
        result = response.json()
        
        if result['code'] == 200:
            picking.carrier_tracking_ref = result['data']['order_code']
            return True
        return False
    
    def ghn_get_cod_reconciliation(self, date_from, date_to):
        """Lấy đối soát COD từ GHN"""
        url = "https://dev-online-gateway.ghn.vn/shiip/public-api/v2/a5/gen-token"
        
        headers = {
            'Token': self.ghn_token,
            'Content-Type': 'application/json'
        }
        
        data = {
            'from_date': date_from.strftime('%Y-%m-%d'),
            'to_date': date_to.strftime('%Y-%m-%d'),
        }
        
        response = requests.post(url, json=data, headers=headers)
        return response.json()
```

**B. Dashboard theo dõi COD realtime**

```
┌─────────────────────────────────────────┐
│ ĐỐI SOÁT COD                            │
├─────────────────────────────────────────┤
│ Kỳ đối soát: 01/01 - 07/01/2024        │
│                                         │
│ 📦 Tổng đơn COD: 45 đơn                 │
│ 💰 Tổng tiền COD: 125,000,000 VNĐ       │
│                                         │
│ Trạng thái:                             │
│ ✅ Đã giao & thu tiền: 38 đơn (95M)     │
│ 🚚 Đang giao: 5 đơn (20M)               │
│ ❌ Hoàn: 2 đơn (10M)                    │
│                                         │
│ Đối soát với GHN:                       │
│ • Tiền GHN báo: 95,000,000 VNĐ          │
│ • Tiền hệ thống: 95,000,000 VNĐ         │
│ • Chênh lệch: 0 VNĐ ✓                   │
│                                         │
│ Tiền về tài khoản:                      │
│ • Dự kiến: 15/01/2024                   │
│ • Số tiền: 95,000,000 VNĐ               │
│                                         │
│ [Xuất báo cáo] [Đối soát chi tiết]      │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Theo dõi COD realtime, không cần đợi file đối soát
- ✅ Tự động đối chiếu với đơn vị vận chuyển
- ✅ Cảnh báo khi có chênh lệch
- ✅ Giảm 90% thời gian đối soát COD

---

### **6.4 Vấn đề: Không theo dõi công nợ**

**Pain Point hiện tại:**
- Không biết đơn nào đã thanh toán đầy đủ, đơn nào còn nợ
- Dễ xảy ra tranh chấp với khách hàng
- Mất tiền do không theo dõi được

**Giải pháp đề xuất:**

**A. Hệ thống quản lý công nợ tự động**

**Odoo Module:** `account_followup` (Payment Follow-up)

**Tính năng:**
- Tự động theo dõi công nợ theo từng khách hàng
- Cảnh báo khi đơn hàng quá hạn thanh toán
- Gửi email/SMS nhắc nhở tự động

**Dashboard công nợ:**

```
┌─────────────────────────────────────────┐
│ QUẢN LÝ CÔNG NỢ                         │
├─────────────────────────────────────────┤
│ Tổng công nợ: 25,000,000 VNĐ           │
│                                         │
│ Theo độ tuổi công nợ:                   │
│ • 0-7 ngày: 15,000,000 (10 đơn) 🟢      │
│ • 8-15 ngày: 8,000,000 (5 đơn) 🟡       │
│ • >15 ngày: 2,000,000 (2 đơn) 🔴        │
│                                         │
│ Top khách hàng có công nợ:              │
│ 1. Nguyễn Văn A - 5,000,000 (2 đơn)     │
│    • SO001: 3,000,000 (Quá hạn 3 ngày)  │
│    • SO005: 2,000,000 (Còn 2 ngày)      │
│    [Nhắc nhở] [Xem chi tiết]            │
│                                         │
│ 2. Trần Thị B - 3,000,000 (1 đơn)       │
│    • SO010: 3,000,000 (Quá hạn 10 ngày) │
│    [Nhắc nhở] [Xem chi tiết]            │
│                                         │
│ [Gửi nhắc nhở hàng loạt] [Báo cáo]      │
└─────────────────────────────────────────┘
```

**B. Tự động gửi nhắc nhở thanh toán**

**Customize Python:**
```python
# Module: custom_payment_reminder
class AccountMove(models.Model):
    _inherit = 'account.move'
    
    def _cron_send_payment_reminder(self):
        """Gửi nhắc nhở thanh toán tự động"""
        # Tìm hóa đơn quá hạn chưa thanh toán
        overdue_invoices = self.search([
            ('state', '=', 'posted'),
            ('payment_state', '!=', 'paid'),
            ('invoice_date_due', '<', fields.Date.today())
        ])
        
        for invoice in overdue_invoices:
            days_overdue = (fields.Date.today() - invoice.invoice_date_due).days
            
            # Gửi nhắc nhở theo độ tuổi công nợ
            if days_overdue == 3:  # Quá hạn 3 ngày - nhắc nhở lần 1
                self._send_reminder_email(invoice, 'gentle')
            elif days_overdue == 7:  # Quá hạn 7 ngày - nhắc nhở lần 2
                self._send_reminder_email(invoice, 'firm')
            elif days_overdue == 15:  # Quá hạn 15 ngày - cảnh báo nghiêm túc
                self._send_reminder_email(invoice, 'final')
    
    def _send_reminder_email(self, invoice, reminder_type):
        """Gửi email nhắc nhở"""
        template_mapping = {
            'gentle': 'custom_payment_reminder.email_template_gentle_reminder',
            'firm': 'custom_payment_reminder.email_template_firm_reminder',
            'final': 'custom_payment_reminder.email_template_final_reminder',
        }
        
        template = self.env.ref(template_mapping[reminder_type])
        template.send_mail(invoice.id, force_send=True)
```

**Email nhắc nhở mẫu:**

```
Kính gửi Quý khách [Tên khách hàng],

Chúng tôi nhận thấy đơn hàng #SO001 của Quý khách 
đã quá hạn thanh toán 3 ngày.

Thông tin đơn hàng:
• Mã đơn: SO001
• Ngày đặt: 01/01/2024
• Hạn thanh toán: 05/01/2024
• Số tiền: 5,000,000 VNĐ

Vui lòng thanh toán trong 2 ngày tới để tránh ảnh 
hưởng đến các đơn hàng tiếp theo.

Thông tin thanh toán:
• Ngân hàng: Vietcombank
• Số TK: 1234567890
• Nội dung: SO001

Trân trọng,
[Tên shop]
```

**Lợi ích:**
- ✅ Kiểm soát chặt chẽ công nợ, không bị mất tiền
- ✅ Tự động nhắc nhở, không cần nhớ
- ✅ Giảm 80% công nợ quá hạn
- ✅ Cải thiện dòng tiền của doanh nghiệp

---

## **🎯 7. GIẢI PHÁP CHO VẤN ĐỀ VỀ ĐƠN HÀNG**

### **7.1 Vấn đề: Không có hệ thống quản lý trạng thái**

**Pain Point hiện tại:**
- Không biết đơn hàng đang ở bước nào
- Nhân viên phải nhớ hoặc hỏi lại để biết đơn đang ở đâu
- Khó theo dõi, dễ bỏ sót

**Giải pháp đề xuất:**

**A. Workflow quản lý trạng thái đơn hàng tự động**

**Odoo Module:** `sale` (Sales Management)

**Các trạng thái đơn hàng:**

```
1. Báo giá (Quotation)
   ↓
2. Chờ xác nhận (Quotation Sent)
   ↓
3. Đã xác nhận (Sales Order)
   ↓
4. Đang chuẩn bị hàng (Preparing)
   ↓
5. Đang đóng gói (Packing)
   ↓
6. Sẵn sàng giao hàng (Ready to Ship)
   ↓
7. Đang giao hàng (In Transit)
   ↓
8. Đã giao hàng (Delivered)
   ↓
9. Hoàn tất (Done)
```

**Dashboard theo dõi đơn hàng:**

```
┌─────────────────────────────────────────┐
│ QUẢN LÝ ĐƠN HÀNG                        │
├─────────────────────────────────────────┤
│ Tổng đơn hôm nay: 25 đơn                │
│                                         │
│ Theo trạng thái:                        │
│ 📝 Chờ xác nhận: 5 đơn                  │
│ ✅ Đã xác nhận: 8 đơn                   │
│ 📦 Đang chuẩn bị: 6 đơn                 │
│ 🚚 Đang giao: 4 đơn                     │
│ ✓ Hoàn tất: 2 đơn                       │
│                                         │
│ Cảnh báo:                               │
│ ⚠️ 2 đơn quá thời gian chuẩn bị         │
│ ⚠️ 1 đơn chờ xác nhận >2h               │
│                                         │
│ [Xem tất cả] [Lọc] [Báo cáo]            │
└─────────────────────────────────────────┘
```

**B. Timeline theo dõi chi tiết từng đơn**

**Customize Python:**
```python
# Module: sale_order_timeline
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    timeline_ids = fields.One2many('sale.order.timeline', 'order_id', 'Timeline')
    
    def action_confirm(self):
        """Ghi log khi xác nhận đơn"""
        res = super().action_confirm()
        self._create_timeline_entry('confirmed', 'Đơn hàng đã được xác nhận')
        return res
    
    def _create_timeline_entry(self, event_type, description):
        """Tạo timeline entry"""
        self.env['sale.order.timeline'].create({
            'order_id': self.id,
            'event_type': event_type,
            'description': description,
            'user_id': self.env.user.id,
            'timestamp': fields.Datetime.now()
        })

class SaleOrderTimeline(models.Model):
    _name = 'sale.order.timeline'
    _description = 'Sale Order Timeline'
    _order = 'timestamp desc'
    
    order_id = fields.Many2one('sale.order', 'Order')
    event_type = fields.Selection([
        ('created', 'Tạo đơn'),
        ('confirmed', 'Xác nhận'),
        ('preparing', 'Chuẩn bị hàng'),
        ('packed', 'Đóng gói'),
        ('shipped', 'Giao hàng'),
        ('delivered', 'Đã giao'),
        ('cancelled', 'Hủy'),
    ], 'Event Type')
    description = fields.Text('Description')
    user_id = fields.Many2one('res.users', 'User')
    timestamp = fields.Datetime('Timestamp')
```

**Hiển thị timeline:**

```
┌─────────────────────────────────────────┐
│ ĐƠN HÀNG #SO001                         │
├─────────────────────────────────────────┤
│ Khách hàng: Nguyễn Văn A                │
│ Tổng tiền: 5,000,000 VNĐ                │
│ Trạng thái: 🚚 Đang giao hàng           │
│                                         │
│ TIMELINE:                               │
│ ┌───────────────────────────────────┐   │
│ │ ✓ 10:00 - 15/01/2024              │   │
│ │   Đơn hàng được tạo               │   │
│ │   Bởi: Nhân viên A                │   │
│ ├───────────────────────────────────┤   │
│ │ ✓ 10:15 - 15/01/2024              │   │
│ │   Đơn hàng đã xác nhận            │   │
│ │   Bởi: Nhân viên A                │   │
│ ├───────────────────────────────────┤   │
│ │ ✓ 11:00 - 15/01/2024              │   │
│ │   Bắt đầu chuẩn bị hàng           │   │
│ │   Bởi: Nhân viên kho B            │   │
│ ├───────────────────────────────────┤   │
│ │ ✓ 11:30 - 15/01/2024              │   │
│ │   Đóng gói hoàn tất               │   │
│ │   Bởi: Nhân viên kho B            │   │
│ ├───────────────────────────────────┤   │
│ │ 🚚 12:00 - 15/01/2024 (Hiện tại)  │   │
│ │   Đang giao hàng                  │   │
│ │   Mã vận đơn: GHN123456           │   │
│ │   [Theo dõi vận đơn]              │   │
│ └───────────────────────────────────┘   │
│                                         │
│ [Cập nhật trạng thái] [In đơn]          │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Theo dõi chính xác 100% trạng thái đơn hàng
- ✅ Không bỏ sót, không quên đơn
- ✅ Khách hàng có thể tự tra cứu trạng thái
- ✅ Cải thiện trải nghiệm khách hàng

---

### **7.2 Vấn đề: Không có mã đơn hàng tự động**

**Pain Point hiện tại:**
- Đánh số thủ công hoặc không có mã
- Dễ nhầm lẫn, trùng lặp
- Khó tra cứu đơn hàng

**Giải pháp đề xuất:**

**A. Hệ thống sinh mã đơn hàng tự động**

**Odoo Module:** `sale` có sẵn sequence

**Customize Python - Tùy chỉnh format mã:**
```python
# Module: custom_sale_order_sequence
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.model
    def create(self, vals):
        """Tạo mã đơn hàng tự động theo format tùy chỉnh"""
        if vals.get('name', 'New') == 'New':
            # Format: SO-YYMMDD-XXX
            # VD: SO-240115-001
            today = fields.Date.today()
            prefix = f"SO-{today.strftime('%y%m%d')}"
            
            # Đếm số đơn trong ngày
            count = self.search_count([
                ('name', 'like', prefix),
                ('date_order', '=', today)
            ])
            
            vals['name'] = f"{prefix}-{str(count + 1).zfill(3)}"
        
        return super().create(vals)
```

**Ví dụ mã đơn hàng:**
- `SO-240115-001` - Đơn hàng ngày 15/01/2024, số thứ tự 001
- `SO-240115-002` - Đơn hàng ngày 15/01/2024, số thứ tự 002
- `SO-240116-001` - Đơn hàng ngày 16/01/2024, số thứ tự 001

**B. Tìm kiếm đơn hàng thông minh**

```
┌─────────────────────────────────────────┐
│ TÌM KIẾM ĐƠN HÀNG                       │
├─────────────────────────────────────────┤
│ Tìm kiếm: [SO-240115]                   │
│                                         │
│ Kết quả (3 đơn):                        │
│                                         │
│ 1. SO-240115-001                        │
│    • Khách: Nguyễn Văn A                │
│    • Giá trị: 5,000,000 VNĐ             │
│    • Trạng thái: Đã giao                │
│    [Xem chi tiết]                       │
│                                         │
│ 2. SO-240115-002                        │
│    • Khách: Trần Thị B                  │
│    • Giá trị: 3,000,000 VNĐ             │
│    • Trạng thái: Đang giao              │
│    [Xem chi tiết]                       │
│                                         │
│ 3. SO-240115-003                        │
│    • Khách: Lê Văn C                    │
│    • Giá trị: 7,000,000 VNĐ             │
│    • Trạng thái: Đang chuẩn bị          │
│    [Xem chi tiết]                       │
│                                         │
│ [Lọc nâng cao] [Xuất Excel]             │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Không bao giờ trùng mã đơn hàng
- ✅ Dễ dàng tra cứu và quản lý
- ✅ Mã có ý nghĩa, biết ngay ngày tạo đơn
- ✅ Chuyên nghiệp hơn với khách hàng

---

### **7.3 Vấn đề: Khó tìm kiếm đơn hàng cũ**

**Pain Point hiện tại:**
- Phải mở Excel và tìm từng dòng theo tên khách hoặc ngày mua
- Rất mất thời gian
- Dễ bỏ sót thông tin

**Giải pháp đề xuất:**

**A. Tìm kiếm đa tiêu chí**

**Odoo Module:** `sale` có sẵn search view

**Customize Python - Tìm kiếm nâng cao:**
```python
# Module: advanced_sale_search
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        """Tùy chỉnh tìm kiếm"""
        # Thêm tìm kiếm theo số điện thoại khách hàng
        if args:
            for i, arg in enumerate(args):
                if arg[0] == 'partner_phone':
                    partner_ids = self.env['res.partner'].search([
                        ('phone', 'ilike', arg[2])
                    ]).ids
                    args[i] = ('partner_id', 'in', partner_ids)
        
        return super()._search(args, offset, limit, order, count, access_rights_uid)
```

**Giao diện tìm kiếm:**

```
┌─────────────────────────────────────────┐
│ TÌM KIẾM ĐƠN HÀNG NÂNG CAO              │
├─────────────────────────────────────────┤
│ Mã đơn hàng: [_________]                │
│ Tên khách hàng: [_________]             │
│ Số điện thoại: [_________]              │
│                                         │
│ Ngày đặt hàng:                          │
│ Từ: [15/01/2024] Đến: [15/01/2024]     │
│                                         │
│ Trạng thái: [▼ Tất cả]                  │
│ Khoảng giá: Từ [_____] Đến [_____]     │
│                                         │
│ Sản phẩm: [_________]                   │
│ Nhân viên phụ trách: [▼ Tất cả]        │
│                                         │
│ [Tìm kiếm] [Xóa bộ lọc]                 │
└─────────────────────────────────────────┘
```

**B. Lịch sử mua hàng của khách**

```
┌─────────────────────────────────────────┐
│ KHÁCH HÀNG: Nguyễn Văn A                │
├─────────────────────────────────────────┤
│ SĐT: 0901234567                         │
│ Tổng đơn: 5 đơn                         │
│ Tổng giá trị: 25,000,000 VNĐ           │
│                                         │
│ LỊCH SỬ MUA HÀNG:                       │
│ ┌───────────────────────────────────┐   │
│ │ SO-240115-001 - 15/01/2024        │   │
│ │ • Váy cưới cách tân A             │   │
│ │ • Giá: 5,000,000 VNĐ              │   │
│ │ • Trạng thái: Hoàn tất            │   │
│ │ [Xem chi tiết]                    │   │
│ ├───────────────────────────────────┤   │
│ │ SO-231220-045 - 20/12/2023        │   │
│ │ • Váy dạ hội B                    │   │
│ │ • Giá: 4,000,000 VNĐ              │   │
│ │ • Trạng thái: Hoàn tất            │   │
│ │ [Xem chi tiết]                    │   │
│ ├───────────────────────────────────┤   │
│ │ SO-231115-023 - 15/11/2023        │   │
│ │ • Phụ kiện cưới                   │   │
│ │ • Giá: 1,500,000 VNĐ              │   │
│ │ • Trạng thái: Hoàn tất            │   │
│ │ [Xem chi tiết]                    │   │
│ └───────────────────────────────────┘   │
│                                         │
│ [Tạo đơn mới] [Gửi ưu đãi]             │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Tìm đơn hàng trong 5 giây thay vì 5 phút
- ✅ Xem ngay lịch sử mua hàng của khách
- ✅ Phục vụ khách hàng tốt hơn
- ✅ Tăng khả năng bán hàng (biết khách đã mua gì)

---

### **7.4 Vấn đề: Không có lịch sử thay đổi**

**Pain Point hiện tại:**
- Không biết ai đã sửa, sửa cái gì, sửa lúc nào
- Dễ xảy ra tranh cãi giữa các nhân viên
- Mất kiểm soát

**Giải pháp đề xuất:**

**A. Audit Log - Ghi nhận mọi thay đổi**

**Odoo Module:** `auditlog` (Audit Log)

**Customize Python:**
```python
# Module: sale_order_audit
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _track_fields = ['partner_id', 'amount_total', 'state']
    
    def write(self, vals):
        """Ghi log mọi thay đổi"""
        for order in self:
            # Lưu giá trị cũ
            old_values = {
                'partner_id': order.partner_id.name if order.partner_id else '',
                'amount_total': order.amount_total,
                'state': order.state,
            }
            
            # Thực hiện thay đổi
            res = super(SaleOrder, order).write(vals)
            
            # Ghi log các thay đổi
            for field in vals:
                if field in self._track_fields:
                    new_value = vals[field]
                    old_value = old_values.get(field)
                    
                    if new_value != old_value:
                        self.env['sale.order.log'].create({
                            'order_id': order.id,
                            'field_name': field,
                            'old_value': str(old_value),
                            'new_value': str(new_value),
                            'user_id': self.env.user.id,
                            'timestamp': fields.Datetime.now()
                        })
            
            return res

class SaleOrderLog(models.Model):
    _name = 'sale.order.log'
    _description = 'Sale Order Change Log'
    _order = 'timestamp desc'
    
    order_id = fields.Many2one('sale.order', 'Order')
    field_name = fields.Char('Field')
    old_value = fields.Text('Old Value')
    new_value = fields.Text('New Value')
    user_id = fields.Many2one('res.users', 'Changed By')
    timestamp = fields.Datetime('Timestamp')
```

**Hiển thị lịch sử thay đổi:**

```
┌─────────────────────────────────────────┐
│ LỊCH SỬ THAY ĐỔI - ĐƠN HÀNG #SO001     │
├─────────────────────────────────────────┤
│ 15/01/2024 14:30 - Nhân viên A          │
│ • Thay đổi: Trạng thái                  │
│ • Từ: "Chờ xác nhận"                    │
│ • Thành: "Đã xác nhận"                  │
│                                         │
│ 15/01/2024 14:25 - Nhân viên A          │
│ • Thay đổi: Tổng tiền                   │
│ • Từ: "5,500,000 VNĐ"                   │
│ • Thành: "5,000,000 VNĐ"                │
│ • Lý do: Áp dụng mã giảm giá            │
│                                         │
│ 15/01/2024 14:20 - Nhân viên A          │
│ • Thay đổi: Khách hàng                  │
│ • Từ: "Nguyễn Văn B"                    │
│ • Thành: "Nguyễn Văn A"                 │
│ • Lý do: Sửa nhầm tên khách             │
│                                         │
│ 15/01/2024 14:00 - Nhân viên A          │
│ • Tạo đơn hàng                          │
│                                         │
│ [Xuất báo cáo] [Hoàn tác thay đổi]      │
└─────────────────────────────────────────┘
```

**B. So sánh phiên bản (Version Control)**

```
┌─────────────────────────────────────────┐
│ SO SÁNH PHIÊN BẢN                       │
├─────────────────────────────────────────┤
│ Phiên bản 1 (14:00)  |  Phiên bản 2 (14:30)│
│                                         │
│ Khách hàng:                             │
│ Nguyễn Văn B         |  Nguyễn Văn A    │
│                      |  ← Đã thay đổi   │
│                                         │
│ Sản phẩm:                               │
│ • Váy cưới A         |  • Váy cưới A    │
│ • Phụ kiện B         |  • Phụ kiện B    │
│                      |  • Khăn voan C   │
│                      |  ← Đã thêm       │
│                                         │
│ Tổng tiền:                              │
│ 5,000,000 VNĐ        |  5,500,000 VNĐ   │
│                      |  ← Đã thay đổi   │
│                                         │
│ [Hoàn tác về v1] [Xuất so sánh]         │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Truy vết được mọi thay đổi
- ✅ Không tranh cãi, có bằng chứng rõ ràng
- ✅ Phát hiện sai sót và khắc phục nhanh
- ✅ Tăng trách nhiệm của nhân viên

---

### **7.5 Vấn đề: Không có quy trình hủy/hoàn đơn**

**Pain Point hiện tại:**
- Xử lý thủ công, không thống nhất
- Mỗi lần xử lý khác nhau, dễ gây nhầm lẫn
- Không theo dõi được lý do hủy/hoàn

**Giải pháp đề xuất:**

**A. Quy trình hủy đơn chuẩn hóa**

**Odoo Module:** `sale` (có sẵn cancel order)

**Customize Python - Thêm lý do hủy:**
```python
# Module: sale_order_cancellation
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    cancellation_reason = fields.Selection([
        ('customer_request', 'Khách yêu cầu hủy'),
        ('out_of_stock', 'Hết hàng'),
        ('wrong_info', 'Thông tin sai'),
        ('payment_issue', 'Vấn đề thanh toán'),
        ('other', 'Lý do khác'),
    ], 'Cancellation Reason')
    cancellation_note = fields.Text('Cancellation Note')
    
    def action_cancel_with_reason(self):
        """Hủy đơn với lý do"""
        return {
            'name': 'Hủy đơn hàng',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order.cancel.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_order_id': self.id}
        }

class SaleOrderCancelWizard(models.TransientModel):
    _name = 'sale.order.cancel.wizard'
    _description = 'Sale Order Cancellation Wizard'
    
    order_id = fields.Many2one('sale.order', 'Order')
    reason = fields.Selection([
        ('customer_request', 'Khách yêu cầu hủy'),
        ('out_of_stock', 'Hết hàng'),
        ('wrong_info', 'Thông tin sai'),
        ('payment_issue', 'Vấn đề thanh toán'),
        ('other', 'Lý do khác'),
    ], 'Reason', required=True)
    note = fields.Text('Note')
    refund = fields.Boolean('Hoàn tiền cho khách', default=False)
    
    def action_confirm_cancel(self):
        """Xác nhận hủy đơn"""
        self.order_id.write({
            'cancellation_reason': self.reason,
            'cancellation_note': self.note,
        })
        
        # Hủy đơn hàng
        self.order_id.action_cancel()
        
        # Nếu cần hoàn tiền
        if self.refund and self.order_id.invoice_ids:
            # Tạo credit note (hóa đơn hoàn tiền)
            for invoice in self.order_id.invoice_ids:
                invoice.action_create_credit_note()
        
        # Gửi thông báo cho khách
        self.order_id._send_cancellation_email()
        
        return {'type': 'ir.actions.act_window_close'}
```

**Giao diện hủy đơn:**

```
┌─────────────────────────────────────────┐
│ HỦY ĐƠN HÀNG #SO001                     │
├─────────────────────────────────────────┤
│ Khách hàng: Nguyễn Văn A                │
│ Tổng tiền: 5,000,000 VNĐ                │
│ Trạng thái: Đã xác nhận                 │
│                                         │
│ Lý do hủy*:                             │
│ ( ) Khách yêu cầu hủy                   │
│ (•) Hết hàng                            │
│ ( ) Thông tin sai                       │
│ ( ) Vấn đề thanh toán                   │
│ ( ) Lý do khác                          │
│                                         │
│ Ghi chú:                                │
│ ┌─────────────────────────────────┐     │
│ │ Sản phẩm size M đã hết hàng,    │     │
│ │ khách không muốn đổi size khác  │     │
│ └─────────────────────────────────┘     │
│                                         │
│ [✓] Hoàn tiền cho khách                 │
│     (Nếu đã thanh toán)                 │
│                                         │
│ [✓] Gửi email thông báo cho khách       │
│                                         │
│ ⚠️ Lưu ý: Hành động này không thể hoàn tác│
│                                         │
│ [Hủy] [Xác nhận hủy đơn]                │
└─────────────────────────────────────────┘
```

**B. Quy trình hoàn hàng**

**Odoo Module:** `stock` (có sẵn return picking)

**Customize Python:**
```python
# Module: sale_order_return
class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    return_reason = fields.Selection([
        ('defective', 'Sản phẩm lỗi'),
        ('wrong_item', 'Giao nhầm hàng'),
        ('not_as_described', 'Không đúng mô tả'),
        ('change_mind', 'Khách đổi ý'),
        ('other', 'Lý do khác'),
    ], 'Return Reason')
    return_note = fields.Text('Return Note')
    
    def action_return_with_reason(self):
        """Hoàn hàng với lý do"""
        return {
            'name': 'Hoàn hàng',
            'type': 'ir.actions.act_window',
            'res_model': 'stock.return.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_picking_id': self.id}
        }
```

**Giao diện hoàn hàng:**

```
┌─────────────────────────────────────────┐
│ HOÀN HÀNG - ĐƠN #SO001                  │
├─────────────────────────────────────────┤
│ Khách hàng: Nguyễn Văn A                │
│ Ngày giao: 15/01/2024                   │
│                                         │
│ Sản phẩm hoàn:                          │
│ [✓] Váy cưới cách tân A - Size M        │
│     Số lượng: [1]                       │
│ [ ] Phụ kiện B                          │
│                                         │
│ Lý do hoàn*:                            │
│ (•) Sản phẩm lỗi                        │
│ ( ) Giao nhầm hàng                      │
│ ( ) Không đúng mô tả                    │
│ ( ) Khách đổi ý                         │
│ ( ) Lý do khác                          │
│                                         │
│ Mô tả chi tiết:                         │
│ ┌─────────────────────────────────┐     │
│ │ Váy bị rách ở phần tay áo       │     │
│ └─────────────────────────────────┘     │
│                                         │
│ Hình ảnh minh chứng:                    │
│ [📷 Tải ảnh lên]                        │
│                                         │
│ Xử lý:                                  │
│ (•) Hoàn tiền: 5,000,000 VNĐ            │
│ ( ) Đổi sản phẩm khác                   │
│ ( ) Sửa chữa miễn phí                   │
│                                         │
│ [Hủy] [Xác nhận hoàn hàng]              │
└─────────────────────────────────────────┘
```

**C. Báo cáo hủy/hoàn đơn**

```
┌─────────────────────────────────────────┐
│ BÁO CÁO HỦY/HOÀN ĐƠN                    │
├─────────────────────────────────────────┤
│ Tháng 01/2024                           │
│                                         │
│ Tổng đơn hủy: 15 đơn (5% tổng đơn)     │
│ Tổng giá trị: 45,000,000 VNĐ           │
│                                         │
│ Lý do hủy:                              │
│ • Khách yêu cầu: 8 đơn (53%)            │
│ • Hết hàng: 4 đơn (27%)                 │
│ • Vấn đề thanh toán: 2 đơn (13%)        │
│ • Khác: 1 đơn (7%)                      │
│                                         │
│ Tổng đơn hoàn: 5 đơn (1.7% tổng đơn)   │
│ Tổng giá trị: 15,000,000 VNĐ           │
│                                         │
│ Lý do hoàn:                             │
│ • Sản phẩm lỗi: 3 đơn (60%)             │
│ • Không đúng mô tả: 1 đơn (20%)         │
│ • Khách đổi ý: 1 đơn (20%)              │
│                                         │
│ 💡 Insight:                             │
│ • Tỷ lệ hủy do hết hàng cao → Cần       │
│   cải thiện quản lý tồn kho             │
│ • Sản phẩm lỗi chiếm 60% hoàn hàng →    │
│   Cần kiểm tra chất lượng kỹ hơn        │
│                                         │
│ [Xuất báo cáo] [Xem chi tiết]           │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Quy trình chuẩn hóa, xử lý nhất quán
- ✅ Theo dõi được lý do hủy/hoàn
- ✅ Phân tích để cải thiện quy trình
- ✅ Tăng sự hài lòng của khách hàng

---

## **🎯 8. GIẢI PHÁP CHO VẤN ĐỀ VỀ SẢN PHẨM**

### **8.1 Vấn đề: Không quản lý biến thể sản phẩm**

**Pain Point hiện tại:**
- Mỗi biến thể (size S, M, L, màu trắng, hồng...) được ghi riêng lẻ trong Excel
- Khó biết tổng tồn kho của một mẫu váy có bao nhiêu
- Khó quản lý giá, hình ảnh cho từng biến thể

**Giải pháp đề xuất:**

**A. Hệ thống quản lý biến thể sản phẩm (Product Variants)**

**Odoo Module:** `product` (Product Variants)

**Cấu trúc:**
```
Sản phẩm chính: Váy cưới cách tân A
├── Thuộc tính 1: Size
│   ├── S
│   ├── M
│   ├── L
│   └── XL
├── Thuộc tính 2: Màu sắc
│   ├── Trắng
│   ├── Hồng
│   └── Kem
└── Tạo ra 12 biến thể (4 size × 3 màu)
```

**Customize Python:**
```python
# Module: product_variant_management
class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    def create_variants_with_stock(self, attribute_values):
        """Tạo biến thể với tồn kho riêng"""
        # Tạo biến thể
        self.attribute_line_ids = [(0, 0, {
            'attribute_id': attr['attribute_id'],
            'value_ids': [(6, 0, attr['value_ids'])]
        }) for attr in attribute_values]
        
        # Tạo tồn kho cho từng biến thể
        for variant in self.product_variant_ids:
            self.env['stock.quant'].create({
                'product_id': variant.id,
                'location_id': self.env.ref('stock.stock_location_stock').id,
                'quantity': 0,  # Sẽ cập nhật khi nhập hàng
            })
        
        return self.product_variant_ids

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    def name_get(self):
        """Hiển thị tên biến thể đầy đủ"""
        result = []
        for product in self:
            # VD: Váy cưới cách tân A (Size M, Màu Trắng)
            name = product.product_tmpl_id.name
            if product.product_template_attribute_value_ids:
                attrs = ', '.join(product.product_template_attribute_value_ids.mapped('name'))
                name = f"{name} ({attrs})"
            result.append((product.id, name))
        return result
```

**Giao diện quản lý biến thể:**

```
┌─────────────────────────────────────────┐
│ SẢN PHẨM: Váy cưới cách tân A           │
├─────────────────────────────────────────┤
│ Mã SP: VDC-001                          │
│ Giá cơ bản: 5,000,000 VNĐ              │
│                                         │
│ THUỘC TÍNH:                             │
│ • Size: S, M, L, XL                     │
│ • Màu sắc: Trắng, Hồng, Kem             │
│                                         │
│ BIẾN THỂ (12 biến thể):                 │
│ ┌───────────────────────────────────┐   │
│ │ Size │ Màu   │ Tồn kho │ Giá     │   │
│ ├──────┼───────┼─────────┼─────────┤   │
│ │ S    │ Trắng │ 5       │ 5,000K  │   │
│ │ S    │ Hồng  │ 3       │ 5,200K  │   │
│ │ S    │ Kem   │ 2       │ 5,000K  │   │
│ │ M    │ Trắng │ 8       │ 5,000K  │   │
│ │ M    │ Hồng  │ 6       │ 5,200K  │   │
│ │ M    │ Kem   │ 4       │ 5,000K  │   │
│ │ L    │ Trắng │ 4       │ 5,000K  │   │
│ │ L    │ Hồng  │ 2       │ 5,200K  │   │
│ │ L    │ Kem   │ 1       │ 5,000K  │   │
│ │ XL   │ Trắng │ 2       │ 5,500K  │   │
│ │ XL   │ Hồng  │ 1       │ 5,700K  │   │
│ │ XL   │ Kem   │ 0       │ 5,500K  │   │
│ └──────┴───────┴─────────┴─────────┘   │
│                                         │
│ Tổng tồn kho: 38 sản phẩm               │
│                                         │
│ [Cập nhật giá hàng loạt] [Nhập kho]     │
└─────────────────────────────────────────┘
```

**B. Ma trận tồn kho theo biến thể**

```
┌─────────────────────────────────────────┐
│ MA TRẬN TỒN KHO - Váy cưới cách tân A   │
├─────────────────────────────────────────┤
│        │ Trắng │ Hồng │ Kem  │ Tổng    │
│ ───────┼───────┼──────┼──────┼─────────│
│ S      │   5   │  3   │  2   │   10    │
│ M      │   8   │  6   │  4   │   18    │
│ L      │   4   │  2   │  1   │    7    │
│ XL     │   2   │  1   │  0   │    3    │
│ ───────┼───────┼──────┼──────┼─────────│
│ Tổng   │  19   │ 12   │  7   │   38    │
│                                         │
│ 💡 Insight:                             │
│ • Size M bán chạy nhất (47% tồn kho)    │
│ • Màu Trắng được ưa chuộng nhất (50%)   │
│ • Size XL màu Kem đã hết hàng ⚠️        │
│                                         │
│ [Xuất Excel] [Nhập hàng theo ma trận]   │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Quản lý tồn kho chính xác từng biến thể
- ✅ Dễ dàng xem tổng quan và chi tiết
- ✅ Giá linh hoạt theo từng biến thể
- ✅ Báo cáo bán hàng theo thuộc tính

---

### **8.2 Vấn đề: Không có hình ảnh trong hệ thống**

**Pain Point hiện tại:**
- Hình ảnh lưu rời rạc trên máy tính hoặc điện thoại
- Khi cần gửi cho khách, phải tìm kiếm rất lâu
- Không có hình ảnh cho từng biến thể

**Giải pháp đề xuất:**

**A. Thư viện hình ảnh sản phẩm**

**Odoo Module:** `product` (có sẵn image field)

**Customize Python - Nhiều hình ảnh:**
```python
# Module: product_multi_image
class ProductImage(models.Model):
    _name = 'product.image'
    _description = 'Product Image'
    _order = 'sequence, id'
    
    name = fields.Char('Name')
    sequence = fields.Integer('Sequence', default=10)
    image = fields.Binary('Image', required=True)
    product_tmpl_id = fields.Many2one('product.template', 'Product Template')
    product_variant_id = fields.Many2one('product.product', 'Product Variant')

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    image_ids = fields.One2many('product.image', 'product_tmpl_id', 'Images')
    image_count = fields.Integer('Image Count', compute='_compute_image_count')
    
    def _compute_image_count(self):
        for product in self:
            product.image_count = len(product.image_ids)
```

**Giao diện quản lý hình ảnh:**

```
┌─────────────────────────────────────────┐
│ HÌNH ẢNH SẢN PHẨM                       │
│ Váy cưới cách tân A                     │
├─────────────────────────────────────────┤
│ Hình chính:                             │
│ ┌─────────────────────┐                 │
│ │                     │                 │
│ │   [Hình váy chính]  │                 │
│ │                     │                 │
│ └─────────────────────┘                 │
│                                         │
│ Thư viện ảnh (8 ảnh):                   │
│ ┌───┬───┬───┬───┐                       │
│ │[1]│[2]│[3]│[4]│                       │
│ └───┴───┴───┴───┘                       │
│ ┌───┬───┬───┬───┐                       │
│ │[5]│[6]│[7]│[8]│                       │
│ └───┴───┴───┴───┘                       │
│                                         │
│ [+ Thêm ảnh] [Sắp xếp] [Xóa]            │
│                                         │
│ Hình theo biến thể:                     │
│ • Size S - Màu Trắng: 3 ảnh             │
│ • Size S - Màu Hồng: 3 ảnh              │
│ • Size M - Màu Trắng: 3 ảnh             │
│ ...                                     │
│                                         │
│ [Gửi ảnh cho khách] [Tải xuống tất cả]  │
└─────────────────────────────────────────┘
```

**B. Gửi hình ảnh cho khách tự động**

**Customize Python:**
```python
# Module: product_image_share
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def action_send_product_images(self):
        """Gửi hình ảnh sản phẩm cho khách"""
        # Lấy tất cả sản phẩm trong đơn
        products = self.order_line.mapped('product_id')
        
        # Tạo email với hình ảnh
        attachments = []
        for product in products:
            for image in product.product_tmpl_id.image_ids:
                attachments.append({
                    'name': f"{product.name}_{image.sequence}.jpg",
                    'datas': image.image,
                    'mimetype': 'image/jpeg'
                })
        
        # Gửi email
        template = self.env.ref('product_image_share.email_template_product_images')
        template.with_context(attachments=attachments).send_mail(self.id)
        
        return True
```

**Email gửi khách:**

```
Kính gửi Quý khách Nguyễn Văn A,

Cảm ơn Quý khách đã quan tâm đến sản phẩm của chúng tôi.

Đính kèm là hình ảnh chi tiết của sản phẩm trong đơn hàng #SO001:

📷 Váy cưới cách tân A (Size M, Màu Trắng)
   • Ảnh 1: Mặt trước
   • Ảnh 2: Mặt sau
   • Ảnh 3: Chi tiết tay áo
   • Ảnh 4: Chi tiết thân váy

Nếu cần thêm thông tin, vui lòng liên hệ:
📞 Hotline: 0901234567
💬 Zalo: 0901234567

Trân trọng,
[Tên shop]
```

**Lợi ích:**
- ✅ Hình ảnh được quản lý tập trung
- ✅ Tìm kiếm và gửi cho khách nhanh chóng
- ✅ Hình ảnh theo từng biến thể
- ✅ Tăng tỷ lệ chốt đơn (khách thấy rõ sản phẩm)

---

### **8.3 Vấn đề: Không quản lý giá theo thời gian**

**Pain Point hiện tại:**
- Giá cố định, khó áp dụng khuyến mãi
- Khi giảm giá phải sửa thủ công từng dòng trong Excel
- Không theo dõi được lịch sử giá

**Giải pháp đề xuất:**

**A. Hệ thống quản lý giá linh hoạt (Pricelist)**

**Odoo Module:** `product` (Pricelist)

**Customize Python:**
```python
# Module: advanced_pricelist
class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'
    
    def create_seasonal_pricelist(self, season_name, discount_percent, date_start, date_end):
        """Tạo bảng giá theo mùa"""
        pricelist = self.create({
            'name': f"Khuyến mãi {season_name}",
            'active': True,
            'discount_policy': 'with_discount',
        })
        
        # Tạo rule giảm giá cho tất cả sản phẩm
        self.env['product.pricelist.item'].create({
            'pricelist_id': pricelist.id,
            'applied_on': '3_global',  # Áp dụng cho tất cả
            'compute_price': 'percentage',
            'percent_price': discount_percent,
            'date_start': date_start,
            'date_end': date_end,
        })
        
        return pricelist
```

**Giao diện quản lý giá:**

```
┌─────────────────────────────────────────┐
│ QUẢN LÝ GIÁ - Váy cưới cách tân A       │
├─────────────────────────────────────────┤
│ Giá gốc: 5,000,000 VNĐ                  │
│                                         │
│ BẢNG GIÁ HIỆN TẠI:                      │
│ ┌───────────────────────────────────┐   │
│ │ Bảng giá      │ Giá bán │ Còn lại│   │
│ ├───────────────┼─────────┼────────┤   │
│ │ Giá thường    │ 5,000K  │ -      │   │
│ │ Giá VIP       │ 4,500K  │ 10%    │   │
│ │ Flash Sale    │ 3,500K  │ 30%    │   │
│ │ (15-20/01)    │         │        │   │
│ └───────────────┴─────────┴────────┘   │
│                                         │
│ LỊCH SỬ GIÁ:                            │
│ • 01/01/2024: 5,000,000 VNĐ (Giá gốc)  │
│ • 10/12/2023: 4,800,000 VNĐ (Giảm 4%)  │
│ • 01/11/2023: 5,200,000 VNĐ (Tăng 4%)  │
│ • 01/10/2023: 5,000,000 VNĐ (Giá gốc)  │
│                                         │
│ [Tạo khuyến mãi] [Xem biểu đồ giá]      │
└─────────────────────────────────────────┘
```

**B. Tạo chương trình khuyến mãi tự động**

```
┌─────────────────────────────────────────┐
│ TẠO CHƯƠNG TRÌNH KHUYẾN MÃI             │
├─────────────────────────────────────────┤
│ Tên chương trình*:                      │
│ [Flash Sale Tết 2024]                   │
│                                         │
│ Thời gian:                              │
│ Từ: [15/01/2024 00:00]                  │
│ Đến: [20/01/2024 23:59]                 │
│                                         │
│ Áp dụng cho:                            │
│ (•) Tất cả sản phẩm                     │
│ ( ) Danh mục cụ thể: [▼ Váy cưới]      │
│ ( ) Sản phẩm cụ thể                     │
│                                         │
│ Loại giảm giá:                          │
│ (•) Phần trăm: [30] %                   │
│ ( ) Số tiền cố định: [_______] VNĐ     │
│                                         │
│ Điều kiện (tùy chọn):                   │
│ [ ] Giá trị đơn tối thiểu: [_____] VNĐ  │
│ [ ] Số lượng tối thiểu: [___] sản phẩm  │
│ [ ] Chỉ áp dụng cho khách VIP           │
│                                         │
│ [✓] Tự động kích hoạt khi đến thời gian │
│ [✓] Gửi thông báo cho khách hàng        │
│                                         │
│ [Hủy] [Lưu nháp] [Tạo & Kích hoạt]      │
└─────────────────────────────────────────┘
```

**C. Giá theo số lượng (Bulk Pricing)**

```
┌─────────────────────────────────────────┐
│ GIÁ THEO SỐ LƯỢNG                       │
│ Váy cưới cách tân A                     │
├─────────────────────────────────────────┤
│ Mua 1 sản phẩm: 5,000,000 VNĐ/sp       │
│ Mua 2-5 sản phẩm: 4,800,000 VNĐ/sp (-4%)│
│ Mua 6-10 sản phẩm: 4,500,000 VNĐ/sp (-10%)│
│ Mua >10 sản phẩm: 4,200,000 VNĐ/sp (-16%)│
│                                         │
│ Ví dụ:                                  │
│ • Mua 1 sp: 5,000,000 VNĐ               │
│ • Mua 3 sp: 14,400,000 VNĐ (tiết kiệm 600K)│
│ • Mua 10 sp: 45,000,000 VNĐ (tiết kiệm 5M)│
│                                         │
│ [Áp dụng] [Chỉnh sửa]                   │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Linh hoạt trong chiến lược giá
- ✅ Dễ dàng tạo khuyến mãi, flash sale
- ✅ Theo dõi lịch sử giá, phân tích hiệu quả
- ✅ Tăng doanh thu (giá theo số lượng, VIP)

---

### **8.4 Vấn đề: Không phân loại sản phẩm rõ ràng**

**Pain Point hiện tại:**
- Không có danh mục chuẩn
- Khó tìm kiếm, báo cáo
- Không biết sản phẩm nào thuộc nhóm nào

**Giải pháp đề xuất:**

**A. Hệ thống phân loại sản phẩm đa cấp**

**Odoo Module:** `product` (Product Category)

**Cấu trúc danh mục:**

```
Tất cả sản phẩm
├── Váy cưới
│   ├── Váy cưới truyền thống
│   ├── Váy cưới cách tân
│   ├── Váy cưới hiện đại
│   └── Váy cưới dạ hội
├── Váy dạ hội
│   ├── Váy dạ hội dài
│   └── Váy dạ hội ngắn
├── Phụ kiện
│   ├── Khăn voan
│   ├── Vương miện
│   ├── Hoa cầm tay
│   └── Giày cưới
└── Trang phục phù dâu
    ├── Váy phù dâu
    └── Áo dài phù dâu
```

**Customize Python:**
```python
# Module: product_category_enhanced
class ProductCategory(models.Model):
    _inherit = 'product.category'
    
    image = fields.Binary('Category Image')
    description = fields.Text('Description')
    product_count = fields.Integer('Product Count', compute='_compute_product_count')
    
    def _compute_product_count(self):
        """Đếm số sản phẩm trong danh mục"""
        for category in self:
            category.product_count = self.env['product.template'].search_count([
                ('categ_id', 'child_of', category.id)
            ])
```

**Giao diện danh mục:**

```
┌─────────────────────────────────────────┐
│ DANH MỤC SẢN PHẨM                       │
├─────────────────────────────────────────┤
│ 📁 Tất cả sản phẩm (125 sp)             │
│ ├─ 👗 Váy cưới (85 sp)                  │
│ │  ├─ Váy cưới truyền thống (20 sp)     │
│ │  ├─ Váy cưới cách tân (35 sp)         │
│ │  ├─ Váy cưới hiện đại (20 sp)         │
│ │  └─ Váy cưới dạ hội (10 sp)           │
│ ├─ 👗 Váy dạ hội (25 sp)                │
│ │  ├─ Váy dạ hội dài (15 sp)            │
│ │  └─ Váy dạ hội ngắn (10 sp)           │
│ ├─ 💍 Phụ kiện (12 sp)                  │
│ │  ├─ Khăn voan (3 sp)                  │
│ │  ├─ Vương miện (4 sp)                 │
│ │  ├─ Hoa cầm tay (3 sp)                │
│ │  └─ Giày cưới (2 sp)                  │
│ └─ 👰 Trang phục phù dâu (3 sp)         │
│    ├─ Váy phù dâu (2 sp)                │
│    └─ Áo dài phù dâu (1 sp)             │
│                                         │
│ [+ Thêm danh mục] [Sắp xếp] [Báo cáo]   │
└─────────────────────────────────────────┘
```

**B. Tìm kiếm theo danh mục**

```
┌─────────────────────────────────────────┐
│ TÌM KIẾM SẢN PHẨM                       │
├─────────────────────────────────────────┤
│ Danh mục: [▼ Váy cưới cách tân]         │
│ Từ khóa: [_________________]            │
│ Giá: Từ [_____] Đến [_____] VNĐ         │
│ Tồn kho: [▼ Còn hàng]                   │
│                                         │
│ Kết quả (35 sản phẩm):                  │
│ ┌───────────────────────────────────┐   │
│ │ [Ảnh] Váy cưới cách tân A         │   │
│ │       • Giá: 5,000,000 VNĐ        │   │
│ │       • Tồn: 38 sp                │   │
│ │       [Xem] [Sửa] [Xóa]           │   │
│ ├───────────────────────────────────┤   │
│ │ [Ảnh] Váy cưới cách tân B         │   │
│ │       • Giá: 6,000,000 VNĐ        │   │
│ │       • Tồn: 25 sp                │   │
│ │       [Xem] [Sửa] [Xóa]           │   │
│ └───────────────────────────────────┘   │
│                                         │
│ [Xuất Excel] [In catalog]               │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Tìm kiếm sản phẩm nhanh chóng
- ✅ Báo cáo theo danh mục dễ dàng
- ✅ Quản lý có hệ thống, chuyên nghiệp
- ✅ Dễ dàng mở rộng khi có sản phẩm mới

---

### **8.5 Vấn đề: Không có mã SKU chuẩn**

**Pain Point hiện tại:**
- Đặt tên tùy ý, không thống nhất
- Cùng một sản phẩm có thể có nhiều tên khác nhau
- Gây trùng lặp và khó quản lý

**Giải pháp đề xuất:**

**A. Hệ thống sinh mã SKU tự động**

**Odoo Module:** `product` (có sẵn default_code)

**Customize Python:**
```python
# Module: product_sku_generator
class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    @api.model
    def create(self, vals):
        """Tự động sinh mã SKU khi tạo sản phẩm"""
        if not vals.get('default_code'):
            # Format: CATEGORY-YEAR-SEQUENCE
            # VD: VDC-24-001 (Váy cưới cách tân - 2024 - 001)
            category = self.env['product.category'].browse(vals.get('categ_id'))
            year = fields.Date.today().strftime('%y')
            
            # Lấy mã danh mục (3 ký tự đầu)
            category_code = category.name[:3].upper() if category else 'PRD'
            
            # Đếm số sản phẩm trong danh mục
            count = self.search_count([('categ_id', '=', vals.get('categ_id'))])
            
            vals['default_code'] = f"{category_code}-{year}-{str(count + 1).zfill(3)}"
        
        return super().create(vals)
```

**Quy tắc đặt mã SKU:**

```
Format: [CATEGORY]-[YEAR]-[SEQUENCE]

Ví dụ:
• VDC-24-001: Váy cưới cách tân - 2024 - Số 001
• VDD-24-015: Váy dạ hội - 2024 - Số 015
• PKH-24-003: Phụ kiện - 2024 - Số 003

Với biến thể:
• VDC-24-001-S-W: Size S, Màu Trắng (White)
• VDC-24-001-M-P: Size M, Màu Hồng (Pink)
• VDC-24-001-L-C: Size L, Màu Kem (Cream)
```

**Giao diện sinh mã SKU:**

```
┌─────────────────────────────────────────┐
│ TẠO SẢN PHẨM MỚI                        │
├─────────────────────────────────────────┤
│ Tên sản phẩm*:                          │
│ [Váy cưới cách tân A]                   │
│                                         │
│ Danh mục*:                              │
│ [▼ Váy cưới cách tân]                   │
│                                         │
│ Mã SKU:                                 │
│ [VDC-24-036] 🔄 Tự động sinh            │
│ [ ] Nhập thủ công                       │
│                                         │
│ 💡 Mã SKU được tạo tự động theo quy tắc:│
│    [Danh mục]-[Năm]-[Số thứ tự]         │
│                                         │
│ Giá bán*: [5,000,000] VNĐ              │
│ ...                                     │
│                                         │
│ [Hủy] [Lưu]                             │
└─────────────────────────────────────────┘
```

**B. Kiểm tra trùng lặp SKU**

**Customize Python:**
```python
# Module: product_sku_validator
class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    @api.constrains('default_code')
    def _check_sku_unique(self):
        """Kiểm tra SKU không trùng lặp"""
        for product in self:
            if product.default_code:
                duplicate = self.search([
                    ('default_code', '=', product.default_code),
                    ('id', '!=', product.id)
                ])
                if duplicate:
                    raise ValidationError(
                        f"Mã SKU '{product.default_code}' đã tồn tại cho sản phẩm '{duplicate.name}'"
                    )
```

**Lợi ích:**
- ✅ Mã SKU chuẩn, không trùng lặp
- ✅ Dễ dàng tra cứu và quản lý
- ✅ Tích hợp với barcode, quét mã nhanh
- ✅ Chuyên nghiệp, dễ mở rộng

---

## **🎯 9. GIẢI PHÁP CHO VẤN ĐỀ VỀ NHÂN VIÊN**

### **9.1 Vấn đề: Không phân quyền rõ ràng**

**Pain Point hiện tại:**
- File Excel được chia sẻ chung, ai cũng có thể mở và sửa
- Không kiểm soát được ai làm gì
- Dễ xảy ra sai sót hoặc xóa nhầm dữ liệu

**Giải pháp đề xuất:**

**A. Hệ thống phân quyền chi tiết (Role-Based Access Control)**

**Odoo Module:** `base` (Users & Access Rights)

**Các vai trò chuẩn:**

```
1. Admin (Quản trị viên)
   ✓ Toàn quyền trên hệ thống
   ✓ Quản lý người dùng, phân quyền
   ✓ Xem tất cả báo cáo, dữ liệu

2. Manager (Quản lý)
   ✓ Xem tất cả đơn hàng, khách hàng
   ✓ Duyệt đơn hàng, hủy đơn
   ✓ Xem báo cáo doanh thu, tồn kho
   ✗ Không sửa cấu hình hệ thống

3. Sales (Nhân viên bán hàng)
   ✓ Tạo đơn hàng, báo giá
   ✓ Xem khách hàng
   ✓ Xem tồn kho
   ✗ Không xem giá nhập, lợi nhuận
   ✗ Không hủy đơn đã duyệt

4. Warehouse (Nhân viên kho)
   ✓ Nhập/xuất kho
   ✓ Kiểm kho
   ✓ Đóng gói đơn hàng
   ✗ Không xem thông tin khách hàng
   ✗ Không tạo đơn hàng

5. Accountant (Kế toán)
   ✓ Xem tất cả hóa đơn, thanh toán
   ✓ Đối soát công nợ
   ✓ Xuất báo cáo tài chính
   ✗ Không tạo/sửa đơn hàng
```

**Customize Python:**
```python
# Module: custom_access_rights
class ResUsers(models.Model):
    _inherit = 'res.users'
    
    def create_user_with_role(self, name, email, role):
        """Tạo người dùng với vai trò cụ thể"""
        # Mapping role với groups
        role_groups = {
            'admin': ['base.group_system'],
            'manager': ['sales_team.group_sale_manager', 'stock.group_stock_manager'],
            'sales': ['sales_team.group_sale_salesman'],
            'warehouse': ['stock.group_stock_user'],
            'accountant': ['account.group_account_user'],
        }
        
        # Tạo user
        user = self.create({
            'name': name,
            'login': email,
            'email': email,
            'groups_id': [(6, 0, [self.env.ref(g).id for g in role_groups.get(role, [])])]
        })
        
        return user
```

**Giao diện phân quyền:**

```
┌─────────────────────────────────────────┐
│ QUẢN LÝ NGƯỜI DÙNG                      │
├─────────────────────────────────────────┤
│ Tổng: 8 người dùng                      │
│                                         │
│ ┌───────────────────────────────────┐   │
│ │ Nguyễn Văn A - Admin              │   │
│ │ • Email: admin@shop.com           │   │
│ │ • Vai trò: Quản trị viên          │   │
│ │ • Quyền: Toàn quyền               │   │
│ │ [Sửa] [Khóa]                      │   │
│ ├───────────────────────────────────┤   │
│ │ Trần Thị B - Manager              │   │
│ │ • Email: manager@shop.com         │   │
│ │ • Vai trò: Quản lý                │   │
│ │ • Quyền: Xem báo cáo, duyệt đơn   │   │
│ │ [Sửa] [Khóa]                      │   │
│ ├───────────────────────────────────┤   │
│ │ Lê Văn C - Sales                  │   │
│ │ • Email: sales1@shop.com          │   │
│ │ • Vai trò: Nhân viên bán hàng     │   │
│ │ • Quyền: Tạo đơn, xem khách       │   │
│ │ [Sửa] [Khóa]                      │   │
│ └───────────────────────────────────┘   │
│                                         │
│ [+ Thêm người dùng] [Xuất danh sách]    │
└─────────────────────────────────────────┘
```

**B. Phân quyền chi tiết theo từng chức năng**

```
┌─────────────────────────────────────────┐
│ PHÂN QUYỀN CHI TIẾT - Nhân viên bán hàng│
├─────────────────────────────────────────┤
│ Đơn hàng:                               │
│ [✓] Tạo đơn hàng mới                    │
│ [✓] Xem đơn hàng của mình               │
│ [✓] Sửa đơn hàng (chưa duyệt)          │
│ [ ] Xem đơn hàng của người khác         │
│ [ ] Hủy đơn hàng (đã duyệt)             │
│ [ ] Xóa đơn hàng                        │
│                                         │
│ Khách hàng:                             │
│ [✓] Tạo khách hàng mới                  │
│ [✓] Xem thông tin khách hàng            │
│ [✓] Sửa thông tin khách hàng            │
│ [ ] Xóa khách hàng                      │
│                                         │
│ Sản phẩm:                               │
│ [✓] Xem danh sách sản phẩm              │
│ [✓] Xem giá bán                         │
│ [✓] Xem tồn kho                         │
│ [ ] Xem giá nhập                        │
│ [ ] Thêm/sửa/xóa sản phẩm               │
│                                         │
│ Báo cáo:                                │
│ [✓] Xem doanh số cá nhân                │
│ [ ] Xem doanh số toàn shop              │
│ [ ] Xem báo cáo lợi nhuận               │
│                                         │
│ [Lưu] [Hủy]                             │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Kiểm soát chặt chẽ ai làm gì
- ✅ Bảo mật dữ liệu nhạy cảm
- ✅ Giảm rủi ro sai sót, xóa nhầm
- ✅ Tăng trách nhiệm của nhân viên

---

### **9.2 Vấn đề: Không theo dõi hiệu suất**

**Pain Point hiện tại:**
- Không có dữ liệu về doanh số từng nhân viên
- Không biết số đơn hàng xử lý, tỷ lệ chốt đơn
- Khó đánh giá hiệu suất và thưởng phạt

**Giải pháp đề xuất:**

**A. Dashboard hiệu suất nhân viên**

**Odoo Module:** `sale`, `hr` (Human Resources)

**Customize Python:**
```python
# Module: sales_performance_dashboard
class SalesPerson(models.Model):
    _name = 'sales.person.performance'
    _description = 'Sales Person Performance'
    
    def get_performance_data(self, user_id, date_from, date_to):
        """Lấy dữ liệu hiệu suất nhân viên"""
        orders = self.env['sale.order'].search([
            ('user_id', '=', user_id),
            ('date_order', '>=', date_from),
            ('date_order', '<=', date_to),
        ])
        
        # Tính các chỉ số
        total_orders = len(orders)
        total_revenue = sum(orders.mapped('amount_total'))
        confirmed_orders = orders.filtered(lambda o: o.state in ['sale', 'done'])
        conversion_rate = len(confirmed_orders) / total_orders * 100 if total_orders > 0 else 0
        
        # Sản phẩm bán chạy
        products = {}
        for order in confirmed_orders:
            for line in order.order_line:
                if line.product_id.id not in products:
                    products[line.product_id.id] = {
                        'name': line.product_id.name,
                        'qty': 0,
                        'revenue': 0
                    }
                products[line.product_id.id]['qty'] += line.product_uom_qty
                products[line.product_id.id]['revenue'] += line.price_subtotal
        
        return {
            'total_orders': total_orders,
            'confirmed_orders': len(confirmed_orders),
            'total_revenue': total_revenue,
            'conversion_rate': conversion_rate,
            'avg_order_value': total_revenue / len(confirmed_orders) if confirmed_orders else 0,
            'top_products': sorted(products.values(), key=lambda x: x['revenue'], reverse=True)[:5]
        }
```

**Dashboard hiệu suất:**

```
┌─────────────────────────────────────────┐
│ HIỆU SUẤT NHÂN VIÊN - Lê Văn C          │
├─────────────────────────────────────────┤
│ Tháng 01/2024                           │
│                                         │
│ 📊 TỔNG QUAN:                           │
│ • Tổng đơn: 45 đơn                      │
│ • Đơn thành công: 38 đơn (84%)          │
│ • Doanh thu: 125,000,000 VNĐ           │
│ • Giá trị TB/đơn: 3,289,474 VNĐ         │
│                                         │
│ 🎯 SO SÁNH VỚI MỤC TIÊU:                │
│ Doanh thu: [████████░░] 83% (100M/120M)│
│ Số đơn: [██████████] 100% (38/38)      │
│                                         │
│ 📈 XU HƯỚNG:                            │
│ • Tuần 1: 8 đơn - 25M                   │
│ • Tuần 2: 12 đơn - 35M ↑                │
│ • Tuần 3: 10 đơn - 32M                  │
│ • Tuần 4: 8 đơn - 33M ↑                 │
│                                         │
│ 🏆 TOP SẢN PHẨM BÁN CHẠY:               │
│ 1. Váy cưới cách tân A - 12 sp (35M)    │
│ 2. Váy dạ hội B - 8 sp (28M)            │
│ 3. Phụ kiện C - 15 sp (18M)             │
│                                         │
│ 💰 HOA HỒNG DỰ KIẾN: 6,250,000 VNĐ      │
│ (5% doanh thu)                          │
│                                         │
│ [Xem chi tiết] [So sánh với team]       │
└─────────────────────────────────────────┘
```

**B. Bảng xếp hạng nhân viên**

```
┌─────────────────────────────────────────┐
│ BẢNG XẾP HẠNG NHÂN VIÊN - Tháng 01/2024│
├─────────────────────────────────────────┤
│ Theo doanh thu:                         │
│ 🥇 1. Nguyễn Văn D - 150M (45 đơn)      │
│ 🥈 2. Trần Thị E - 135M (42 đơn)        │
│ 🥉 3. Lê Văn C - 125M (38 đơn)          │
│    4. Phạm Văn F - 110M (35 đơn)        │
│    5. Hoàng Thị G - 95M (28 đơn)        │
│                                         │
│ Theo số đơn:                            │
│ 🥇 1. Nguyễn Văn D - 45 đơn             │
│ 🥈 2. Trần Thị E - 42 đơn               │
│ 🥉 3. Lê Văn C - 38 đơn                 │
│                                         │
│ Theo tỷ lệ chốt đơn:                    │
│ 🥇 1. Trần Thị E - 95%                  │
│ 🥈 2. Nguyễn Văn D - 90%                │
│ 🥉 3. Lê Văn C - 84%                    │
│                                         │
│ [Xem chi tiết] [Xuất báo cáo]           │
└─────────────────────────────────────────┘
```

**C. Báo cáo KPI tự động**

```
┌─────────────────────────────────────────┐
│ BÁO CÁO KPI - Lê Văn C                  │
├─────────────────────────────────────────┤
│ Tháng 01/2024                           │
│                                         │
│ KPI 1: Doanh thu                        │
│ • Mục tiêu: 120,000,000 VNĐ            │
│ • Thực tế: 125,000,000 VNĐ             │
│ • Đạt: 104% ✅                          │
│                                         │
│ KPI 2: Số đơn hàng                      │
│ • Mục tiêu: 40 đơn                      │
│ • Thực tế: 38 đơn                       │
│ • Đạt: 95% ⚠️                           │
│                                         │
│ KPI 3: Tỷ lệ chốt đơn                   │
│ • Mục tiêu: 85%                         │
│ • Thực tế: 84%                          │
│ • Đạt: 99% ⚠️                           │
│                                         │
│ KPI 4: Giá trị TB/đơn                   │
│ • Mục tiêu: 3,000,000 VNĐ              │
│ • Thực tế: 3,289,474 VNĐ               │
│ • Đạt: 110% ✅                          │
│                                         │
│ TỔNG KẾT:                               │
│ • Đạt: 2/4 KPI                          │
│ • Đánh giá: Tốt                         │
│ • Thưởng: 2,000,000 VNĐ                │
│                                         │
│ [Xuất PDF] [Gửi email]                  │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Đánh giá hiệu suất khách quan, chính xác
- ✅ Động viên nhân viên làm việc tốt hơn
- ✅ Phát hiện nhân viên cần hỗ trợ
- ✅ Công bằng trong thưởng phạt

---

### **9.3 Vấn đề: Không có hệ thống đào tạo**

**Pain Point hiện tại:**
- Nhân viên mới phải học quy trình từ nhân viên cũ
- Không có tài liệu hướng dẫn chuẩn
- Dễ xảy ra sai sót khi chưa quen

**Giải pháp đề xuất:**

**A. Tài liệu hướng dẫn tích hợp trong hệ thống**

**Odoo Module:** `website` (Knowledge Base)

**Customize Python:**
```python
# Module: employee_training
class TrainingModule(models.Model):
    _name = 'training.module'
    _description = 'Training Module'
    
    name = fields.Char('Module Name')
    description = fields.Html('Description')
    video_url = fields.Char('Video URL')
    document_ids = fields.Many2many('ir.attachment', 'Documents')
    quiz_ids = fields.One2many('training.quiz', 'module_id', 'Quizzes')
    
class TrainingProgress(models.Model):
    _name = 'training.progress'
    _description = 'Training Progress'
    
    user_id = fields.Many2one('res.users', 'User')
    module_id = fields.Many2one('training.module', 'Module')
    progress = fields.Float('Progress (%)')
    completed = fields.Boolean('Completed')
    quiz_score = fields.Float('Quiz Score')
```

**Giao diện đào tạo:**

```
┌─────────────────────────────────────────┐
│ ĐÀO TẠO NHÂN VIÊN MỚI                   │
├─────────────────────────────────────────┤
│ Chào mừng Lê Văn C!                     │
│                                         │
│ Tiến độ học: [████████░░] 80% (4/5)    │
│                                         │
│ CÁC MODULE ĐÀO TẠO:                     │
│ ┌───────────────────────────────────┐   │
│ │ ✅ Module 1: Giới thiệu hệ thống  │   │
│ │    • Video: 10 phút               │   │
│ │    • Điểm quiz: 9/10              │   │
│ │    [Xem lại]                      │   │
│ ├───────────────────────────────────┤   │
│ │ ✅ Module 2: Tạo đơn hàng         │   │
│ │    • Video: 15 phút               │   │
│ │    • Điểm quiz: 10/10             │   │
│ │    [Xem lại]                      │   │
│ ├───────────────────────────────────┤   │
│ │ ✅ Module 3: Quản lý khách hàng   │   │
│ │    • Video: 12 phút               │   │
│ │    • Điểm quiz: 8/10              │   │
│ │    [Xem lại]                      │   │
│ ├───────────────────────────────────┤   │
│ │ ✅ Module 4: Xử lý thanh toán     │   │
│ │    • Video: 18 phút               │   │
│ │    • Điểm quiz: 9/10              │   │
│ │    [Xem lại]                      │   │
│ ├───────────────────────────────────┤   │
│ │ ⏳ Module 5: Báo cáo & Phân tích  │   │
│ │    • Video: 20 phút               │   │
│ │    • Chưa hoàn thành              │   │
│ │    [Bắt đầu học]                  │   │
│ └───────────────────────────────────┘   │
│                                         │
│ [Tiếp tục học] [Xem chứng chỉ]          │
└─────────────────────────────────────────┘
```

**B. Video hướng dẫn từng bước**

```
┌─────────────────────────────────────────┐
│ VIDEO: Cách tạo đơn hàng                │
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────┐     │
│ │                                 │     │
│ │    [Video player]               │     │
│ │    ▶ 00:05 / 15:00              │     │
│ │                                 │     │
│ └─────────────────────────────────┘     │
│                                         │
│ NỘI DUNG:                               │
│ 1. Đăng nhập hệ thống (00:00-01:00)     │
│ 2. Tìm kiếm khách hàng (01:00-03:00)    │
│ 3. Chọn sản phẩm (03:00-06:00)          │
│ 4. Nhập thông tin đơn (06:00-10:00)     │
│ 5. Xác nhận và in đơn (10:00-15:00)     │
│                                         │
│ TÀI LIỆU ĐÍNH KÈM:                      │
│ 📄 Hướng dẫn tạo đơn hàng.pdf           │
│ 📄 Checklist kiểm tra đơn hàng.pdf      │
│                                         │
│ [Tải tài liệu] [Làm bài quiz]           │
└─────────────────────────────────────────┘
```

**C. Trợ giúp ngữ cảnh (Contextual Help)**

```
Khi nhân viên đang tạo đơn hàng:

┌─────────────────────────────────────────┐
│ TẠO ĐƠN HÀNG                            │
├─────────────────────────────────────────┤
│ Khách hàng*: [_________] 💡             │
│                                         │
│ ┌─────────────────────────────────┐     │
│ │ 💡 MẸO:                         │     │
│ │ • Gõ tên hoặc SĐT để tìm khách  │     │
│ │ • Nhấn Enter để tạo khách mới   │     │
│ │ • Click vào khách để xem lịch sử│     │
│ │                                 │     │
│ │ [Xem video hướng dẫn]           │     │
│ └─────────────────────────────────┘     │
│                                         │
│ Sản phẩm*: [_________]                  │
│ ...                                     │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Nhân viên mới làm quen nhanh (3 ngày thay vì 2 tuần)
- ✅ Chất lượng đồng nhất, không phụ thuộc người dạy
- ✅ Giảm sai sót do chưa quen
- ✅ Nhân viên tự học, không tốn thời gian đào tạo

---

### **9.4 Vấn đề: Không có audit log**

**Pain Point hiện tại:**
- Khi có sai sót xảy ra, không biết ai đã thao tác
- Không biết thao tác gì, vào lúc nào
- Khó tìm nguyên nhân và khắc phục

**Giải pháp đề xuất:**

**A. Hệ thống ghi log toàn diện**

**Odoo Module:** `auditlog` (Audit Trail)

**Customize Python:**
```python
# Module: comprehensive_audit_log
class AuditLog(models.Model):
    _name = 'audit.log'
    _description = 'Comprehensive Audit Log'
    _order = 'create_date desc'
    
    user_id = fields.Many2one('res.users', 'User')
    model_name = fields.Char('Model')
    record_id = fields.Integer('Record ID')
    action = fields.Selection([
        ('create', 'Create'),
        ('write', 'Update'),
        ('unlink', 'Delete'),
        ('read', 'Read'),
    ], 'Action')
    old_values = fields.Text('Old Values')
    new_values = fields.Text('New Values')
    ip_address = fields.Char('IP Address')
    user_agent = fields.Char('User Agent')
    create_date = fields.Datetime('Timestamp', default=fields.Datetime.now)

# Hook vào tất cả models
class BaseModel(models.AbstractModel):
    _inherit = 'base'
    
    @api.model
    def create(self, vals):
        """Log khi tạo record"""
        res = super().create(vals)
        self._create_audit_log('create', {}, vals, res.id)
        return res
    
    def write(self, vals):
        """Log khi sửa record"""
        old_vals = {k: self[k] for k in vals.keys() if k in self._fields}
        res = super().write(vals)
        self._create_audit_log('write', old_vals, vals, self.id)
        return res
    
    def unlink(self):
        """Log khi xóa record"""
        for record in self:
            self._create_audit_log('unlink', record.read()[0], {}, record.id)
        return super().unlink()
    
    def _create_audit_log(self, action, old_vals, new_vals, record_id):
        """Tạo audit log"""
        self.env['audit.log'].sudo().create({
            'user_id': self.env.user.id,
            'model_name': self._name,
            'record_id': record_id,
            'action': action,
            'old_values': str(old_vals),
            'new_values': str(new_vals),
            'ip_address': request.httprequest.remote_addr if request else '',
            'user_agent': request.httprequest.user_agent.string if request else '',
        })
```

**Giao diện xem audit log:**

```
┌─────────────────────────────────────────┐
│ NHẬT KÝ HOẠT ĐỘNG HỆ THỐNG              │
├─────────────────────────────────────────┤
│ Lọc: [Tất cả] [Hôm nay] [7 ngày]       │
│ Người dùng: [▼ Tất cả]                  │
│ Hành động: [▼ Tất cả]                   │
│                                         │
│ ┌───────────────────────────────────┐   │
│ │ 15/01/2024 14:30:25               │   │
│ │ 👤 Lê Văn C                       │   │
│ │ 📝 Cập nhật đơn hàng #SO001       │   │
│ │ • Trạng thái: "Chờ xác nhận"     │   │
│ │   → "Đã xác nhận"                 │   │
│ │ • IP: 192.168.1.100               │   │
│ │ [Xem chi tiết] [Hoàn tác]         │   │
│ ├───────────────────────────────────┤   │
│ │ 15/01/2024 14:25:10               │   │
│ │ 👤 Lê Văn C                       │   │
│ │ 📝 Cập nhật đơn hàng #SO001       │   │
│ │ • Tổng tiền: "5,500,000"          │   │
│ │   → "5,000,000"                   │   │
│ │ • IP: 192.168.1.100               │   │
│ │ [Xem chi tiết] [Hoàn tác]         │   │
│ ├───────────────────────────────────┤   │
│ │ 15/01/2024 14:20:45               │   │
│ │ 👤 Lê Văn C                       │   │
│ │ ➕ Tạo đơn hàng #SO001            │   │
│ │ • Khách: Nguyễn Văn A             │   │
│ │ • Giá trị: 5,000,000 VNĐ          │   │
│ │ • IP: 192.168.1.100               │   │
│ │ [Xem chi tiết]                    │   │
│ └───────────────────────────────────┘   │
│                                         │
│ [Xuất báo cáo] [Tìm kiếm nâng cao]      │
└─────────────────────────────────────────┘
```

**B. Cảnh báo hành vi bất thường**

```
┌─────────────────────────────────────────┐
│ ⚠️ CẢNH BÁO BẢO MẬT                     │
├─────────────────────────────────────────┤
│ Phát hiện 3 hành vi bất thường:         │
│                                         │
│ 1. 🔴 Nghiêm trọng                      │
│    Người dùng: Lê Văn C                 │
│    Hành động: Xóa 5 đơn hàng liên tiếp  │
│    Thời gian: 15/01/2024 14:30          │
│    [Xem chi tiết] [Khóa tài khoản]      │
│                                         │
│ 2. 🟡 Cảnh báo                          │
│    Người dùng: Trần Thị B               │
│    Hành động: Đăng nhập từ IP lạ        │
│    IP: 103.xxx.xxx.xxx (Hà Nội)         │
│    Thời gian: 15/01/2024 12:00          │
│    [Xem chi tiết] [Yêu cầu xác thực]    │
│                                         │
│ 3. 🟡 Cảnh báo                          │
│    Người dùng: Phạm Văn F               │
│    Hành động: Truy cập dữ liệu nhạy cảm │
│    Dữ liệu: Báo cáo lợi nhuận           │
│    Thời gian: 15/01/2024 10:00          │
│    [Xem chi tiết] [Báo cáo quản lý]     │
│                                         │
│ [Xem tất cả cảnh báo]                   │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Truy vết được mọi thao tác
- ✅ Phát hiện hành vi bất thường
- ✅ Bảo mật dữ liệu tốt hơn
- ✅ Giải quyết tranh chấp nhanh chóng

---

### **9.5 Vấn đề: Giao việc không rõ ràng**

**Pain Point hiện tại:**
- Phân công công việc qua tin nhắn hoặc gọi điện
- Không có hệ thống theo dõi
- Dễ quên hoặc bỏ sót

**Giải pháp đề xuất:**

**A. Hệ thống quản lý công việc (Task Management)**

**Odoo Module:** `project` (Project Management)

**Customize Python:**
```python
# Module: task_management
class ProjectTask(models.Model):
    _inherit = 'project.task'
    
    related_order_id = fields.Many2one('sale.order', 'Related Order')
    related_picking_id = fields.Many2one('stock.picking', 'Related Delivery')
    auto_created = fields.Boolean('Auto Created')
    
    def create_task_from_order(self, order):
        """Tự động tạo task từ đơn hàng"""
        # Task cho nhân viên kho: Chuẩn bị hàng
        warehouse_task = self.create({
            'name': f"Chuẩn bị hàng cho đơn {order.name}",
            'project_id': self.env.ref('task_management.project_warehouse').id,
            'user_id': order.warehouse_id.user_id.id,
            'related_order_id': order.id,
            'description': f"Đơn hàng: {order.name}\nKhách hàng: {order.partner_id.name}\nSản phẩm: {', '.join(order.order_line.mapped('product_id.name'))}",
            'date_deadline': order.commitment_date,
            'auto_created': True,
        })
        
        return warehouse_task
```

**Giao diện quản lý công việc:**

```
┌─────────────────────────────────────────┐
│ CÔNG VIỆC CỦA TÔI - Nguyễn Văn H (Kho) │
├─────────────────────────────────────────┤
│ Hôm nay: 15/01/2024                     │
│                                         │
│ ⏰ ĐANG LÀM (2):                        │
│ ┌───────────────────────────────────┐   │
│ │ 🔴 Chuẩn bị hàng cho đơn #SO001   │   │
│ │    • Hạn: 15/01 16:00 (còn 2h)    │   │
│ │    • Sản phẩm: Váy cưới A, Phụ kiện│   │
│ │    • Ghi chú: Khách cần gấp       │   │
│ │    [Xem chi tiết] [Hoàn thành]    │   │
│ ├───────────────────────────────────┤   │
│ │ 🟡 Đóng gói đơn #SO005            │   │
│ │    • Hạn: 15/01 18:00 (còn 4h)    │   │
│ │    • Sản phẩm: Váy dạ hội B       │   │
│ │    [Xem chi tiết] [Hoàn thành]    │   │
│ └───────────────────────────────────┘   │
│                                         │
│ 📋 CHỜ LÀM (3):                         │
│ • Kiểm kho khu A (Hạn: 16/01)           │
│ • Nhập hàng từ xưởng (Hạn: 17/01)       │
│ • Sắp xếp lại kho (Hạn: 18/01)          │
│                                         │
│ ✅ ĐÃ HOÀN THÀNH HÔM NAY (5):           │
│ • Chuẩn bị hàng đơn #SO002              │
│ • Đóng gói đơn #SO003                   │
│ • Giao hàng cho shipper                 │
│ ...                                     │
│                                         │
│ [Xem tất cả] [Báo cáo tiến độ]          │
└─────────────────────────────────────────┘
```

**B. Tự động tạo task từ đơn hàng**

```
Khi đơn hàng được xác nhận:
  ↓
Hệ thống tự động tạo các task:

1. Task cho nhân viên kho:
   "Chuẩn bị hàng cho đơn #SO001"
   • Hạn: Theo commitment date
   • Gán cho: Nhân viên kho được chỉ định

2. Task cho nhân viên bán hàng:
   "Theo dõi thanh toán đơn #SO001"
   • Hạn: Theo payment term
   • Gán cho: Nhân viên tạo đơn

3. Task cho kế toán (nếu COD):
   "Đối soát COD đơn #SO001"
   • Hạn: Sau khi giao hàng 3 ngày
   • Gán cho: Kế toán
```

**C. Thông báo và nhắc nhở**

```
┌─────────────────────────────────────────┐
│ 🔔 THÔNG BÁO                            │
├─────────────────────────────────────────┤
│ Bạn có 3 thông báo mới:                 │
│                                         │
│ 1. ⏰ Công việc sắp đến hạn             │
│    "Chuẩn bị hàng cho đơn #SO001"       │
│    Còn 2 giờ nữa đến hạn                │
│    [Xem] [Hoàn thành]                   │
│                                         │
│ 2. ➕ Công việc mới được giao           │
│    "Kiểm kho khu A"                     │
│    Hạn: 16/01/2024                      │
│    [Xem] [Chấp nhận]                    │
│                                         │
│ 3. ✅ Công việc đã được duyệt           │
│    "Đóng gói đơn #SO003"                │
│    Người duyệt: Quản lý B               │
│    [Xem]                                │
│                                         │
│ [Đánh dấu đã đọc tất cả]                │
└─────────────────────────────────────────┘
```

**Lợi ích:**
- ✅ Công việc rõ ràng, không quên
- ✅ Theo dõi tiến độ realtime
- ✅ Tự động hóa phân công công việc
- ✅ Tăng hiệu suất làm việc của team

---

## **📋 TỔNG KẾT GIẢI PHÁP TO-BE**

**Tổng quan chuyển đổi:**

| Khía cạnh | AS-IS (Hiện tại) | TO-BE (Tương lai) | Cải thiện |
|-----------|------------------|-------------------|-----------|
| **Dữ liệu** | Excel thủ công, dễ sai | Database tập trung, tự động | ↑ 95% độ chính xác |
| **Quy trình** | Thủ công, chậm | Tự động hóa, nhanh | ↓ 70% thời gian xử lý |
| **Tồn kho** | Không realtime, xung đột | Realtime, đồng bộ đa kênh | ↑ 100% độ chính xác |
| **Khách hàng** | Không quản lý, quên khách | CRM đầy đủ, chăm sóc tốt | ↑ 50% tỷ lệ quay lại |
| **Báo cáo** | Thủ công, chậm, sai | Tự động, realtime, chính xác | ↓ 100% thời gian làm báo cáo |
| **Phản hồi khách** | 12 phút | 30 giây | ↓ 96% thời gian chờ |
| **Phân tích** | Cảm tính, không chính xác | AI phân tích, dự đoán chính xác | Tăng khả năng ra quyết định |

**ROI dự kiến:**
- ✅ Tăng 40% doanh thu (Xử lý nhanh, không mất khách)
- ✅ Giảm 60% chi phí vận hành (Tự động hóa)
- ✅ Tăng 50% hiệu suất nhân viên (Công cụ tốt hơn)
- ✅ Tăng 70% sự hài lòng khách hàng (Trải nghiệm tốt)
- ✅ Giảm 80% sai sót (Tự động, validation)

**Thời gian triển khai:** 3-6 tháng (Tùy quy mô)

**Đầu tư:** Phụ thuộc vào giải pháp (Cloud ERP, Custom, SaaS,...)

---

*Tài liệu này trình bày chi tiết giải pháp TO-BE cho tất cả 5 nhóm vấn đề đã xác định trong phân tích AS-IS. Mỗi giải pháp đều có ví dụ cụ thể, minh họa rõ ràng và lợi ích đo lường được.*