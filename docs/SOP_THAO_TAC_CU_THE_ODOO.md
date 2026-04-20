# SOP THAO TÁC CỤ THỂ TRÊN ODOO (CẦM TAY CHỈ VIỆC)

Tài liệu này dành cho người vận hành thực tế, hướng dẫn từng bước thao tác trong Odoo.
Ví dụ chi tiết bao gồm: tạo kho sản phẩm, tạo vị trí kho, tạo sản phẩm, nhập tồn đầu kỳ, tạo đơn bán, xuất kho, xuất hóa đơn.

Lưu ý:

- Tên menu có thể khác nhẹ theo phiên bản Odoo hoặc ngôn ngữ giao diện.
- Nếu không thấy menu, vào `Settings -> Activate Developer Mode` và kiểm tra quyền user.

---

## 1) Tạo kho sản phẩm (Warehouse) - Hướng dẫn chi tiết

## Mục tiêu

Tạo một kho mới để quản lý hàng hóa riêng biệt, ví dụ kho showroom hoặc kho online.

## Điều kiện trước khi làm

- User có quyền `Inventory / Administrator` hoặc `Inventory / Manager`.
- Module `Inventory (stock)` đã cài.

## Các bước thao tác

### Bước 1: Vào màn hình kho

- Mở app `Inventory`.
- Vào menu: `Configuration -> Warehouses`.

### Bước 2: Tạo kho mới

- Bấm nút `New`.
- Điền thông tin:
  - `Warehouse Name`: Kho Showroom
  - `Short Name`: KSR
  - `Company`: công ty hiện tại
  - `Address`: chọn địa chỉ kho (nếu quản lý nhiều địa điểm)

### Bước 3: Cấu hình luồng vận hành kho

- Trong phần Operations/Routes (tùy giao diện):
  - Incoming Shipments: chọn `Receive goods directly (1 step)` hoặc `Input -> Stock (2 steps)`
  - Outgoing Shipments: chọn `Deliver goods directly (1 step)` hoặc `Pick -> Pack -> Ship (3 steps)`
- Với shop nhỏ, khuyến nghị bắt đầu `1 step` để dễ vận hành.

### Bước 4: Lưu kho

- Bấm `Save`.

## Kết quả mong đợi

- Danh sách kho xuất hiện `Kho Showroom (KSR)`.
- Hệ thống tự sinh các vị trí nội bộ mặc định của kho mới.

## Cách test nhanh

1. Tạo 1 sản phẩm test.
2. Nhập hàng vào kho `KSR`.
3. Kiểm tra tồn kho theo kho hiển thị đúng.

## Lỗi thường gặp và cách xử lý

- Không thấy menu `Warehouses`: thiếu quyền Inventory Manager.
- Không tạo được kho: chưa bật multi-warehouse trong settings.

---

## 2) Tạo vị trí kho (Location) chi tiết

## Mục tiêu

Tạo cấu trúc vị trí dạng khu/kệ/ngăn để nhân viên kho dễ tìm hàng.

## Bật tính năng trước

- Vào `Inventory -> Configuration -> Settings`.
- Bật `Storage Locations`.
- Bấm `Save`.

## Các bước thao tác

### Bước 1: Tạo location cha (Khu)

- Menu: `Inventory -> Configuration -> Locations`.
- Bấm `New`.
- Điền:
  - `Location Name`: Khu A
  - `Location Type`: Internal Location
  - `Parent Location`: chọn `KSR/Stock`
- `Save`.

### Bước 2: Tạo location con (Kệ)

- Bấm `New`.
- Điền:
  - `Location Name`: Kệ A1
  - `Location Type`: Internal Location
  - `Parent Location`: Khu A
- `Save`.

### Bước 3: Tạo location con (Ngăn)

- Bấm `New`.
- Điền:
  - `Location Name`: Ngăn 01
  - `Location Type`: Internal Location
  - `Parent Location`: Kệ A1
- `Save`.

## Kết quả mong đợi

- Cấu trúc: `KSR/Stock/Khu A/Kệ A1/Ngăn 01`.

## Cách test nhanh

- Vào sản phẩm -> tab tồn kho -> xem số lượng theo location.

---

## 3) Tạo sản phẩm mới (Product) chi tiết

## Mục tiêu

Tạo sản phẩm có SKU rõ ràng, giá bán/giá vốn đầy đủ, dùng được cho bán và kho.

## Các bước thao tác

### Bước 1: Mở màn hình sản phẩm

- Menu: `Inventory -> Products -> Products`.
- Bấm `New`.

### Bước 2: Điền thông tin chính

- `Product Name`: Dam da hoi A
- `Product Type`: Storable Product
- `Sales Price`: 1200000
- `Cost`: 800000
- `Internal Reference (SKU)`: DDH-A-001
- `Product Category`: Dam da hoi

### Bước 3: Thiết lập Attribute/Variant (nhiều size cho 1 sản phẩm)

> Dùng khi 1 mẫu có nhiều size như S, M, L hoặc 36, 37, 38.

#### 3.1. Bật tính năng Variant (chỉ làm 1 lần)

- Vào `Inventory -> Configuration -> Settings`.
- Tìm phần `Products`.
- Bật `Variants` (hoặc `Attributes & Variants`).
- `Save`.

#### 3.2. Tạo Attribute Size

- Vào `Inventory -> Configuration -> Attributes`.
- Bấm `New`.
- Điền:
  - `Attribute Name`: Size
  - `Display Type`: Radio hoặc Pills (tùy giao diện mong muốn)
  - `Variant Creation Mode`: Instantly
- Trong `Attribute Values`, thêm các giá trị:
  - Ví dụ quần áo: `S`, `M`, `L`, `XL`
  - Hoặc giày/đầm: `36`, `37`, `38`, `39`
- `Save`.

#### 3.3. Gán Size vào sản phẩm

- Quay lại sản phẩm đang tạo.
- Tìm tab `Attributes & Variants` (hoặc tab `Variants`).
- Bấm `Add a line`.
- Chọn `Attribute`: Size.
- Chọn các `Values` cần bán (ví dụ S, M, L).
- `Save` sản phẩm.

#### 3.4. Kiểm tra biến thể sinh ra

- Tại sản phẩm template, bấm smart button `Variants`.
- Kiểm tra hệ thống đã tạo các biến thể theo từng size.
- Mỗi biến thể cần có:
  - `Internal Reference (SKU)` riêng (ví dụ `DDH-A-001-S`, `DDH-A-001-M`).
  - Giá riêng nếu có chênh lệch theo size.

### Bước 4: Cấu hình tồn kho và mua hàng

**Mục đích bước này:** nói cho Odoo biết **sản phẩm này lấy hàng từ đâu** (mua ngoài, sản xuất, v.v.) và **khi bán hoặc cần bổ sung tồn thì hệ thống đi theo luồng nào** (có tạo đơn mua tự động hay không). Không cấu hình thì vẫn tạo được sản phẩm và bán được, nhưng **luồng mua hàng / bổ sung tồn** có thể không chạy đúng mong muốn.

#### 4.1. Tab `Inventory` — Routes (tuyến cung ứng)

##### Cách thao tác bật/chọn Routes cho sản phẩm

> Nếu bạn **không thấy** mục Routes trong tab Inventory, làm bước 4.1.A trước.

**4.1.A) Bật tính năng Routes (chỉ làm 1 lần)**

- Vào `Inventory -> Configuration -> Settings`.
- Tìm nhóm `Warehouse` / `Logistics` (tùy giao diện).
- Bật `Multi-Step Routes` (hoặc `Routes`).
- `Save`.

**4.1.B) Chọn Route cho sản phẩm**

- Vào `Inventory -> Products -> Products`.
- Mở sản phẩm cần cấu hình (nếu đang tạo mới thì tạo xong phần chính và `Save` trước để dễ thấy đủ tab).
- Mở tab `Inventory`.
- Tại mục `Routes`, tick theo nhu cầu:
  - Tick **`Buy`** nếu sản phẩm có thể **đặt xưởng/mua** để nhập về kho.
  - Tick **`Replenish on Order (MTO)`** chỉ khi muốn **đơn bán nào cũng kéo theo đặt xưởng theo đơn** (thường không bật mặc định nếu bạn vẫn nhập tồn bán trước).
- `Save`.

- **Route là gì:** quy tắc vận hành kho (bổ sung hàng). Tùy module đã cài, bạn có thể thấy các route như `Buy`, `Manufacture`, `Replenish on Order (MTO)`, `Dropship`, v.v.
- **Buy (Mua):** bật khi hàng **bổ sung từ nhà cung cấp** (ở đây là **xưởng** khai báo như Vendor). Cho phép tạo **RFQ/PO** cho sản phẩm này (thủ công hoặc theo quy tắc bổ sung tồn).
- **MTO — Make To Order / Replenish on Order:** bật khi **mỗi lần bán đều muốn kích hoạt đặt/sản xuất theo đơn**, thường **không** dùng làm mặc định nếu bạn vẫn **nhập một lượng về kho để bán trước** (xem mục 4.1.1).
- **Không bật route bổ sung:** chỉ hợp khi **không** đặt hàng qua Odoo (nhập xuất ghi tay hoàn toàn).

##### 4.1.1. Luồng cửa hàng: nhập lô đầu → bán → hết thì đặt lẻ hoặc đặt theo ngưỡng

Áp dụng khi quy trình như sau:

1. **Đầu kỳ:** nhập một **số lượng** từ xưởng về kho để bán.
2. **Trong khi bán:** nếu **hết hàng** mà khách muốn mua thêm → **đặt xưởng theo đúng số lượng khách cần** (đặt lẻ theo nhu cầu).
3. **Hoặc:** khi tồn **chạm ngưỡng** → hệ thống **cảnh báo gần hết** → nhân viên **đặt xưởng** với số lượng thống nhất (ví dụ đủ bán thêm một đợt).

**Cách map sang Odoo (gợi ý cấu hình):**


| Việc cần làm                           | Gợi ý trong Odoo                                                                                                                                                                                         |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Xưởng là nguồn nhập                    | Tạo **Contact** loại Vendor = xưởng; ở sản phẩm tab **Purchase** thêm dòng Vendor (giá, lead time) — mục 4.2.                                                                                            |
| Nhập lô đầu để bán                     | Tạo **Purchase Order** tới xưởng → **Receive** vào kho (hoặc điều chỉnh tồn nếu dùng quy trình khác).                                                                                                    |
| Bán hàng bình thường                   | **Sales Order** / POS như hiện tại; **Storable Product** để trừ tồn.                                                                                                                                     |
| Đặt lẻ khi hết mà khách order thêm     | Thường xử lý bằng **PO thủ công** (RFQ/PO) tới xưởng với **số lượng = nhu cầu** (theo khách hoặc theo NV bán hàng). Không bắt buộc bật **MTO** trên toàn bộ sản phẩm nếu bạn vẫn ưu tiên **có tồn sẵn**. |
| Ngưỡng “gần hết hàng” + NV đặt theo SL | Dùng **Reorder Rules** (quy tắc bổ sung tồn): đặt **Min** (ngưỡng cảnh báo / kích hoạt bổ sung), **Max** (mức tồn mục tiêu sau khi đặt), kho áp dụng — xem mục 4.3.                                      |
| Route trên sản phẩm                    | Nên bật `**Buy`** để Odoo biết bổ sung qua **mua từ Vendor (xưởng)**. **MTO** chỉ cân nhắc khi muốn **mỗi đơn bán** đều sinh nhu cầu đặt riêng (khác với luồng “nhập trước rồi bán”).                    |


#### 4.2. Tab `Purchase` — Nhà cung cấp và điều kiện mua

**Mục đích:** gắn **nhà cung cấp mặc định** và **giá/thời gian giao** để khi tạo đơn mua, Odoo điền sẵn thông tin, tránh nhập lại từng lần.

- **Add a line** (hoặc `Vendor`):
  - Chọn **Vendor** (nhà cung cấp đã tạo trong `Contacts`).
    - Nếu chưa có Vendor:
      1. Bấm `Search More...` -> `Create`.
      2. Điền tối thiểu: `Name` (tên xưởng/NCC), `Phone` (nếu có), `Email` (nếu có).
      3. Trong tab `Sales & Purchase`, bật/tích vai trò `Vendor` (nếu form có trường này).
      4. `Save` để lưu contact rồi quay lại sản phẩm.
    - Nếu đã có Vendor:
      1. Gõ tên xưởng vào ô `Vendor`.
      2. Chọn đúng contact trong danh sách gợi ý.
      3. Ưu tiên chọn đúng chi nhánh/đơn vị mua nếu có nhiều contact trùng tên.
  - **Price** (Vendor Price): giá mua theo đơn vị tính của dòng (thường là giá/đơn vị mua).
  - **Delivery Lead Time**: số ngày từ lúc xác nhận PO đến khi hàng về kho (dùng cho lịch và tính toán ngày cần đặt).

> Nếu sản phẩm **không mua ngoài** (chỉ sản xuất nội bộ hoặc chỉ bán dịch vụ), có thể **bỏ qua** tab Purchase hoặc không thêm vendor.

#### 4.3. Reorder Rules — ngưỡng gần hết hàng và số lượng đặt lại

**Mục đích:** khi tồn khả dụng (hoặc dự báo) **xuống dưới mức Min**, hệ thống có thể **cảnh báo** và/hoặc **gợi ý đơn mua** (tùy cấu hình lịch chạy replenishment), giúp NV biết cần đặt xưởng bao nhiêu.

- Menu thường dùng: `Inventory -> Operations -> Replenishment` (hoặc mục **Reordering Rules** trong cấu hình Inventory — tùy phiên bản/giao diện).
- Bấm `New` (hoặc tạo từ smart button trên sản phẩm nếu có).
- Chọn **Product** (và **Variant** nếu quản theo size), **Location** (kho bán), điền:
  - **Min Quantity** (Min): ngưỡng “gần hết” — dưới mức này cần bổ sung.
  - **Max Quantity** (Max): sau khi đặt, mong muốn tồn lên khoảng này (Odoo sẽ gợi ý số lượng đặt ≈ Max − hiện tại, tùy quy tắc).
- **Lưu ý:** scheduler / tần suất chạy replenishment ảnh hưởng tới việc PO có **tự sinh** hay chỉ **xuất hiện trong danh sách cần xử lý** — cần thống nhất với quản trị hệ thống.

> Tóm lại: **Buy + Vendor = xưởng** cho phép đặt hàng chuẩn; **Reorder Rules** phục vụ **ngưỡng**; còn **đặt lẻ theo khách khi đã hết** thường kết hợp **PO thủ công** (hoặc quy trình nội bộ ghi rõ SL trên đơn mua).

### Bước 5: Lưu sản phẩm

- Bấm `Save`.

## Kết quả mong đợi

- Sản phẩm xuất hiện trong danh mục và chọn được khi tạo đơn bán.

## Cách test nhanh

- Tạo báo giá, thêm sản phẩm vừa tạo, kiểm tra giá lên đúng.

---

## 3.1) Cách nhập sản phẩm qua file Excel (Import)

## Mục tiêu

Tạo nhanh nhiều sản phẩm cùng lúc bằng file Excel thay vì nhập tay từng sản phẩm.

## Chuẩn bị file Excel mẫu

### Cột tối thiểu nên có

- `Name` (Tên sản phẩm)
- `Internal Reference` (SKU)
- `Product Type` (Storable Product/Consumable/Service)
- `Sales Price` (Giá bán)
- `Cost` (Giá vốn)
- `Product Category`
- `Unit of Measure`
- `Purchase Unit of Measure`

### Ví dụ 1 dòng dữ liệu

- Name: Dam da hoi B
- Internal Reference: DDH-B-001
- Product Type: Storable Product
- Sales Price: 1500000
- Cost: 1000000
- Product Category: Dam da hoi
- Unit of Measure: Units
- Purchase Unit of Measure: Units

## Các bước thao tác import

### Bước 1: Vào màn hình import sản phẩm

1. Vào `Inventory -> Products -> Products`.
2. Chuyển sang list view (danh sách).
3. Bấm nút `Favorites` (hoặc biểu tượng menu) -> `Import records`.

### Bước 2: Tải file lên

1. Bấm `Upload File`.
2. Chọn file `.xlsx` hoặc `.csv`.

### Bước 3: Map cột dữ liệu

1. Ở từng cột bên trái của file, chọn field tương ứng trong Odoo.
2. Mapping khuyến nghị:
  - `Name` -> `Name`
  - `Internal Reference` -> `Internal Reference`
  - `Product Type` -> `Product Type`
  - `Sales Price` -> `Sales Price`
  - `Cost` -> `Cost`
  - `Product Category` -> `Product Category`
  - `Unit of Measure` -> `Unit of Measure`
  - `Purchase Unit of Measure` -> `Purchase Unit of Measure`

### Bước 4: Kiểm tra trước khi import thật

1. Bấm `Test` (hoặc `Validate`) để kiểm tra lỗi.
2. Nếu có lỗi, sửa file rồi upload lại.
3. Khi không còn lỗi, bấm `Import`.

## Lỗi thường gặp khi import và cách sửa

- Lỗi category không tồn tại:
  - Cần tạo trước `Product Category` đúng tên trong hệ thống.
- Lỗi UoM không hợp lệ:
  - Đảm bảo `Unit of Measure` tồn tại và cùng nhóm đơn vị.
- Lỗi SKU trùng:
  - Sửa cột `Internal Reference` để không trùng.
- Lỗi số (giá) sai định dạng:
  - Dùng số thuần, không có ký tự tiền tệ, ví dụ `1500000`.

## Cách test sau import

1. Tìm theo SKU vừa import.
2. Mở 3-5 sản phẩm ngẫu nhiên, kiểm tra:
  - Tên
  - Giá bán/giá vốn
  - Category
  - UoM
3. Tạo thử 1 báo giá và thêm sản phẩm để xác nhận dùng được.

---

## 4) Nhập tồn đầu kỳ cho sản phẩm

## Mục tiêu

Đưa số lượng tồn ban đầu lên hệ thống theo đúng kho và vị trí.

## Cách 1 (dễ dùng): Inventory Adjustment

### Bước thao tác

1. Vào `Inventory -> Operations -> Inventory Adjustments`.
2. Bấm `New`.
3. Chọn:
  - `Location`: KSR/Stock (hoặc location cụ thể)
4. Bấm `Start Inventory`.
5. Thêm dòng sản phẩm:
  - Product: Dam da hoi A
  - Counted Quantity: 20
6. Bấm `Apply`.

## Kết quả mong đợi

- On hand của sản phẩm tăng lên 20 tại location đã chọn.

## Cách test nhanh

- Mở sản phẩm -> `On Hand` -> kiểm tra số lượng.

---

## 5) Tạo đơn bán hàng (Sales Order) chi tiết

## Mục tiêu

Sales tạo báo giá và xác nhận đơn để kho nhận việc tự động.

## Các bước thao tác

### Bước 1: Tạo báo giá

- App `Sales` -> `Orders -> Quotations`.
- Bấm `New`.
- Chọn `Customer`.
- Chọn `Pricelist`.
- Thêm sản phẩm và số lượng.

### Bước 2: Xác nhận đơn

- Bấm `Confirm`.

## Kết quả mong đợi

- Báo giá chuyển thành Sales Order.
- Hệ thống tự tạo Delivery Order bên kho.

## Cách test nhanh

- Bấm smart button `Delivery`.
- Kiểm tra trạng thái:
  - `Ready` nếu đủ hàng.
  - `Waiting` nếu thiếu hàng.

---

## 6) Xuất kho giao hàng (Delivery) chi tiết

## Mục tiêu

Kho xác nhận xuất hàng để trừ tồn thực tế.

## Các bước thao tác

1. Vào `Inventory -> Operations -> Delivery Orders`.
2. Mở phiếu giao hàng từ SO.
3. Kiểm tra số lượng ở cột `Demand`.
4. Điền `Done Quantity` (hoặc dùng nút check toàn bộ nếu giao đủ).
5. Bấm `Validate`.

## Kết quả mong đợi

- Phiếu giao hàng trạng thái `Done`.
- Tồn kho bị trừ đúng.

## Cách test nhanh

- Mở sản phẩm, kiểm tra On Hand giảm đúng số lượng đã giao.

---

## 6.1) Tách rõ theo kệ/quầy: Odoo lấy đúng kệ khi có đơn
Mục tiêu của phần này:
- Khi có đơn (Sales Order) phát sinh Delivery, kho sẽ **reserve/xuất đúng kệ/quầy** chứa hàng thật.
- Khi nhập hàng vào kho, Odoo sẽ **tự chuyển từ kho cha (KMS/Tồn kho) sang kho con (Kệ/quầy)** theo cấu hình Putaway Rules.

### A. Lưu ý quan trọng (để không “hiểu sai” Rule Deliver 3 steps)
- Trong Warehouse set `Pick -> Pack -> Ship (3 steps)`, bước “lấy từ kho” ở mức cấu hình sẽ thường hiển thị nguồn là **kho cha `KMS/Tồn kho`** (lot stock).
- Cái bạn cần để “chia rõ kệ” là phần **reserve/allocate khi Check Availability** của Delivery:
  - Sau khi bấm `Check Availability`, Odoo sẽ chọn đúng **quant theo từng kệ/quầy có hàng** và tạo move lines tương ứng.
- Vì vậy: nếu bạn chỉ nhìn “Rule steps” mà chưa `Check Availability` thì sẽ thấy “kho cha”. Đây là hành vi bình thường.

### B. Bước thiết lập 1 lần (cấu trúc Location + Logistics)
#### B1) Kiểm tra cấu trúc Location đúng chuẩn
1. `Inventory -> Configuration -> Locations`
2. Đảm bảo:
   - `KMS/Tồn kho` là location kiểu `Internal` (hoặc là location cha của các internal).
   - Mỗi `Khu/Kệ` là `Internal` và nằm **là con** của `KMS/Tồn kho`.
3. Nếu kệ/quầy có “Location Type” không phải `Internal` hoặc không thuộc cây `KMS/Tồn kho` thì Odoo sẽ không reserve đúng.

#### B2) Gán Removal Strategy cho từng kệ/quầy (để reserve có thứ tự rõ ràng)
1. Vào `Inventory -> Configuration -> Locations`.
2. Mở từng location là kệ/quầy (ví dụ `KMS/Tồn kho/Khu A/Kệ A1`).
3. Ở tab/section `Logistics` chọn `Removal Strategy` (ví dụ `FIFO`, `LIFO`, hoặc `Closest Location`).
4. Save.

Gợi ý:
- Nếu bạn muốn ưu tiên “lấy gần/nhanh” theo thực tế kho -> chọn `Closest Location`.
- Nếu bạn có chính sách tồn kho -> chọn `FIFO`/`LIFO`.

#### B3) Tạo Putaway Rules (để khi nhập hàng, tự chuyển từ kho cha -> kho con)
Putaway Rules chỉ hoạt động khi hàng được tạo vào hệ thống bằng các luồng có “receiving/stock move” (ví dụ: Receipt, Inbound Transfer). Nó sẽ quyết định hàng **được cất vào location nào con**.

1. Vào `Inventory -> Configuration -> Putaway Rules` (hoặc mở từ màn hình `Location` bấm nút `Putaway Rules`).
2. Bấm `New`.
3. Điền mẫu theo trường hợp của bạn (ví dụ):
   - `When product arrives in` (location_in_id): chọn **`KMS/Tồn kho`** (hoặc Input location bạn đang dùng khi nhập hàng).
   - `Product`: chọn sản phẩm cụ thể (nếu mỗi sản phẩm phải vào đúng kệ riêng).
     - Hoặc `Product Category`: chọn category chung (nếu nhiều sản phẩm cùng một “nhóm kệ”).
   - `Store to sublocation` (location_out_id): chọn vị trí đích là **kệ/quầy con** bạn muốn chứa.
   - `Sublocation`:
     - Chọn `No`/`Last Used` nếu bạn muốn cố định theo rule đơn giản.
     - Chọn `Closest Location` nếu bạn muốn Odoo tự chọn kệ con phù hợp trong nhóm dựa trên hàng hiện có.
4. Save.

Kịch bản hay dùng theo thực tế:
- Nếu bạn muốn “mỗi sản phẩm vào đúng 1 kệ cố định”: tạo **1 rule theo Product** -> `Store to sublocation = kệ đó`.
- Nếu bạn muốn “mỗi nhóm sản phẩm vào nhóm kệ”: tạo rule theo **Product Category** -> trỏ tới các kệ thuộc nhóm.

### C. Nhập hàng vào kho (để tự chuyển từ kho cha sang kệ)
#### C1) Nhập hàng theo luồng Receipt/Inbound Transfer (khuyến nghị)
1. Vào `Inventory -> Operations -> Receipts` (hoặc màn hình nhập hàng tương ứng hệ thống của bạn).
2. Tạo receipt cho các sản phẩm.
3. Khi Validate receipt:
   - Odoo sẽ chạy Putaway Rules (nếu bạn đã cấu hình ở mục B3).
4. Test nhanh sau khi validate:
   - Vào `Inventory -> Operations -> (Receipt)`, mở tab chi tiết `Stock Moves/Move Lines` để kiểm tra `Destination Location` đã rơi về **kệ/quầy con** hay chưa.
   - Hoặc vào `Inventory > On Hand` lọc location theo `KMS/Tồn kho/Khu.../Kệ...`.

#### C2) Nếu bạn đang dùng Physical Inventory để “đặt tồn” theo kệ (Count đầu kỳ / chỉnh sửa tồn)
- `Physical Inventory` (Inventory Adjustments) là bước **cập nhật số lượng theo bạn nhập**, không phải “để hệ thống putaway tự động khi nhận hàng”.
- Vì vậy:
  - Nếu đếm tồn và nhập nhầm vào kho cha `KMS/Tồn kho` thì sẽ vẫn tồn ở kho cha.
  - Khi có đơn, Odoo sẽ reserve từ nơi có quant thật (kho cha) -> nhìn thấy không tách kệ.

Trong trường hợp này, hãy thực hiện bước D (Relocate quants) để đưa quant từ kho cha xuống kệ/quầy.

### D. Nếu vẫn bị “lấy ở kho cha KMS/Tồn kho” khi có đơn: xử lý nhanh
Kiểm tra và sửa theo thứ tự:

#### D1) Kiểm tra quant ở kho cha còn không
1. Vào `Inventory -> Reporting -> Locations` (hoặc màn hình `On Hand`).
2. Lọc `Location = KMS/Tồn kho`.
3. Chọn đúng 1 sản phẩm đang giao thử.
4. Nếu thấy `On Hand` tại `KMS/Tồn kho` > 0 nghĩa là quant đang nằm ở kho cha.

#### D2) Relocate quant từ kho cha xuống kệ/quầy
1. Vào màn hình hiển thị quant của sản phẩm (cách vào thường là tab/entry “On Hand/Quants”).
2. Chọn các dòng quant ở `KMS/Tồn kho`.
3. Bấm nút `Relocate`.
4. Chọn `To Location` = đúng kệ/quầy con (ví dụ `KMS/Tồn kho/Khu A/Kệ A1`).
5. Confirm.

Sau khi relocate:
- Lặp lại test Delivery: tạo/refresh Delivery -> `Check Availability` -> kiểm tra Move Lines để đảm bảo nguồn đã tách theo kệ.

### E. Quy trình khi có đơn (để kho biết đơn ở kệ nào)
Odoo không lưu “kệ của Sales Order” ngay từ lúc tạo SO. Kệ được xác định tại thời điểm **reserve** khi tạo Delivery.
Làm đúng các bước sau:

1. Tạo `Sales Order` -> Confirm.
2. Mở Delivery Order sinh ra từ SO.
3. Bấm `Check Availability` (hoặc action tương đương để allocate/reserve).
4. Vào tab `Operations`:
   - Mở từng `Stock Move`
   - Kiểm tra `Move Lines` để thấy `Source Location`/`Destination Location` đang là các kệ/quầy con.
5. Sau khi đã thấy đúng kệ:
   - Nhân viên pick/pack/ship theo đúng danh sách.
6. Validate Delivery.

Ghi chú vận hành:
- Nếu bạn in/tra cứu danh sách picking trước khi `Check Availability` thì có thể chỉ thấy “kho cha”.
- Luôn `Check Availability` trước khi lấy danh sách/đi nhặt hàng.

### F. Checklist đạt yêu cầu (1 phút test)
- Mỗi sản phẩm đều có quant nằm ở các location kệ/quầy, không còn treo tại kho cha (nếu rule của bạn yêu cầu tách kệ).
- Với 1 Delivery test:
  - Sau `Check Availability`, `Move Lines` của sản phẩm thể hiện `Source Location` tương ứng đúng kệ/quầy.
- Sau khi Validate Delivery, `On Hand` ở kệ/quầy giảm đúng số lượng đã giao.

---

## 7) Tạo hóa đơn và ghi nhận thanh toán

## Mục tiêu

Hoàn tất chuỗi bán hàng: SO -> Delivery -> Invoice -> Payment.

## Các bước thao tác

### Bước 1: Tạo hóa đơn từ SO

1. Vào `Sales -> Orders -> Sales Orders`.
2. Mở SO đã giao hàng.
3. Bấm `Create Invoice`.
4. Chọn kiểu hóa đơn (Regular invoice).
5. Bấm `Create and View Invoice`.

### Bước 2: Post hóa đơn

- Trong hóa đơn, bấm `Confirm`/`Post` (tùy nhãn nút).

### Bước 3: Ghi nhận thanh toán

1. Bấm `Register Payment`.
2. Chọn:
  - Journal: Cash hoặc Bank
  - Amount: đủ hoặc một phần
3. Bấm `Create Payment`.

## Kết quả mong đợi

- Invoice chuyển `Paid` (nếu trả đủ).
- Công nợ cập nhật đúng.

---

## 7.1) Quy trình tự động khi hết hàng nhưng khách vẫn đặt (MTO + Buy)

## Mục tiêu

Khi kho hết hàng nhưng khách vẫn muốn mua:

- Sales vẫn tạo được `Sales Order`.
- Odoo tự sinh nhu cầu mua hàng từ xưởng/nhà cung cấp.
- Sau khi hàng về và nhập kho, Delivery của khách tiếp tục được cấp hàng để giao.

## Khi nào nên dùng

Áp dụng khi doanh nghiệp muốn:

- Hết hàng vẫn nhận đơn khách.
- Mỗi đơn bán thiếu hàng sẽ kéo theo mua đúng theo đơn.
- Giảm thao tác tạo PO thủ công sau khi Sales chốt đơn.

Không phù hợp nếu doanh nghiệp:

- Chủ yếu bán hàng tồn sẵn.
- Không muốn mỗi đơn bán tự sinh nhu cầu mua.
- Muốn bộ phận mua hàng tự quyết định gom đơn rồi mới mua.

## Luồng tổng quan

`Sales Order -> Confirm -> Odoo tạo nhu cầu mua -> RFQ/PO -> Receipt -> Validate -> Delivery được cấp hàng -> Giao khách -> Invoice`

## Điều kiện trước khi làm

- Đã cài `Purchase`, `Inventory`, `Sales`.
- Sản phẩm là `Storable Product`.
- Sản phẩm đã có `Vendor`/xưởng trong tab mua hàng.
- User có quyền thao tác:
  - Sales: tạo và confirm `Sales Order`
  - Purchase: xem/tạo/xác nhận `RFQ/PO`
  - Inventory: validate `Receipt` và `Delivery`

## Bước 1: Cấu hình tự động trên sản phẩm

1. Vào `Inventory -> Products -> Products`.
2. Mở sản phẩm cần cho phép “khách đặt khi hết hàng”.
3. Kiểm tra:
   - `Product Type` = `Storable Product`
4. Mở tab `Inventory`.
5. Ở mục `Routes`, tick:
   - `Buy`
   - `Replenish on Order (MTO)`
6. `Save`.

## Giải thích ngắn về 2 route này

- `Buy`: Odoo biết rằng nếu cần bổ sung hàng thì nguồn là mua từ Vendor/xưởng.
- `MTO`: Odoo biết rằng khi có đơn bán thiếu hàng thì phải tạo nhu cầu mua theo đúng đơn đó.

Nếu chỉ tick `Buy` mà không tick `MTO`:

- Odoo biết sản phẩm có thể mua, nhưng không tự hiểu rằng đơn bán này phải kéo mua ngay theo đơn.

## Bước 2: Khai báo Vendor/xưởng cho sản phẩm

1. Mở cùng sản phẩm đó.
2. Vào tab `Purchase`.
3. Thêm `Vendor`:
   - `Vendor`: tên xưởng/nhà cung cấp
   - `Price`: giá mua
   - `Delivery Lead Time`: số ngày dự kiến giao
4. `Save`.

## Kết quả mong đợi sau bước 1 + 2

- Sản phẩm đã sẵn sàng cho luồng `MTO + Buy`.
- Khi Sales confirm đơn mà kho không đủ hàng, Odoo có thể sinh nhu cầu mua từ Vendor đã khai báo.

## Bước 3: Sales tạo đơn cho khách khi kho đã hết hàng

1. Vào `Sales -> Orders -> Quotations`.
2. Bấm `New`.
3. Chọn:
   - `Customer`
   - sản phẩm
   - số lượng khách đặt
4. Bấm `Confirm`.

## Điều gì xảy ra sau khi Confirm

Odoo sẽ làm các việc sau:

- Tạo `Sales Order`.
- Tạo `Delivery` cho khách.
- Vì sản phẩm đang dùng `MTO + Buy`, hệ thống tạo nhu cầu mua tương ứng.
- Từ nhu cầu đó, Odoo sinh `RFQ/PO` tới Vendor/xưởng.

## Cách kiểm tra Odoo đã tự kéo mua hay chưa

Sau khi confirm `Sales Order`, kiểm tra theo các cách sau:

1. Ngay trên `Sales Order`:
   - kiểm tra smart button liên quan đến `Purchase`, `RFQ`, hoặc `Replenishment` nếu giao diện có hiển thị
2. Hoặc vào `Purchase -> Orders -> Requests for Quotation`
3. Tìm theo:
   - `Source Document`
   - tên `Sales Order`
   - tên khách
   - tên sản phẩm

## Kết quả mong đợi

- Có `RFQ` hoặc `PO` được sinh ra cho đúng sản phẩm đang thiếu.

## Bước 4: Xử lý RFQ/PO do hệ thống tạo ra

1. Vào `Purchase -> Orders -> Requests for Quotation`.
2. Mở RFQ vừa được tạo.
3. Kiểm tra:
   - `Vendor`
   - `Product`
   - `Quantity`
   - `Source Document` có liên quan đến `SO`
4. Nếu mọi thông tin đúng:
   - bấm `Confirm Order`

## Kết quả mong đợi

- RFQ chuyển thành `Purchase Order`.
- PO sẵn sàng để nhận hàng.

## Bước 5: Khi hàng về, nhận hàng bằng Receipt

1. Mở `Purchase Order`.
2. Bấm smart button `Receipt`.
3. Mở phiếu nhập.
4. Kiểm tra:
   - sản phẩm
   - số lượng
   - location đích
5. Bấm `Validate`.

## Điều gì xảy ra sau khi Receipt được Validate

- Hàng vào kho.
- Nếu bạn đã cấu hình `Putaway Rules`, Odoo sẽ đẩy hàng xuống đúng kệ theo rule.
- Delivery đang chờ của khách sẽ có cơ sở để được reserve/cấp hàng.

## Bước 6: Quay lại Delivery để giao khách

1. Vào `Sales Order` hoặc `Inventory -> Operations -> Delivery Orders`.
2. Mở Delivery của đơn khách.
3. Nếu Delivery chưa tự `Ready`, bấm:
   - `Check Availability`
4. Kiểm tra tab `Operations` / `Move Lines`:
   - `Source Location` đã lấy đúng location/kệ
5. Nhập `Done Quantity`.
6. Bấm `Validate`.

## Kết quả mong đợi

- Delivery chuyển `Done`.
- Đơn khách hoàn tất bước giao hàng như một đơn bán bình thường.

## Bước 7: Tạo hóa đơn cho khách

Sau khi Delivery hoàn tất:

1. Quay lại `Sales Order`.
2. Bấm `Create Invoice`.
3. `Post` hóa đơn.
4. `Register Payment` nếu khách thanh toán.

## Cách nhìn để biết đơn nào là “đơn khách đặt vì hết hàng”

Trong thực tế vận hành, bạn có thể nhận biết bằng các dấu hiệu:

- `Sales Order` đã confirm nhưng Delivery ban đầu ở trạng thái `Waiting` / `Not Available`
- Sau đó hệ thống sinh `RFQ/PO`
- `PO` có `Source Document` liên kết về `SO`

Nói dễ hiểu:

- `SO` là đơn khách.
- `PO/RFQ` là đơn mua bù do Odoo tự tạo để đáp ứng đơn khách đó.

## Ví dụ thực tế

Giả sử:

- Sản phẩm `Váy Big Size Dự Tiệc`
- Tồn kho hiện tại = 0
- Khách đặt mua 1 cái

Luồng sẽ là:

1. Sales tạo `Sales Order` cho khách.
2. Bấm `Confirm`.
3. Odoo thấy không có tồn.
4. Vì sản phẩm đã bật `MTO + Buy`, hệ thống tạo `RFQ`.
5. Bộ phận mua hàng confirm `RFQ` thành `PO`.
6. Khi xưởng giao hàng, kho validate `Receipt`.
7. Odoo cấp hàng cho Delivery của khách.
8. Kho giao hàng.
9. Kế toán tạo invoice.

## Những chỗ dễ hiểu sai

- `MTO` không có nghĩa là hàng tự xuất ngay cho khách.
  - Nó chỉ có nghĩa là đơn bán sẽ kéo theo nhu cầu mua/sản xuất.
- `Buy` không tự động đủ một mình.
  - Muốn “đơn bán kéo mua theo đơn”, cần kết hợp với `MTO`.
- Putaway Rules không tạo PO.
  - Putaway chỉ quyết định hàng nhập xong thì cất vào kệ nào.

## Cách test nhanh toàn bộ quy trình

1. Chọn 1 sản phẩm test.
2. Đặt tồn sản phẩm đó về 0.
3. Bật đúng:
   - `Buy`
   - `Replenish on Order (MTO)`
4. Gắn `Vendor`.
5. Tạo 1 `Sales Order` số lượng 1.
6. `Confirm`.
7. Kiểm tra `Purchase -> RFQ` đã sinh.
8. Confirm `RFQ` thành `PO`.
9. Mở `Receipt` và `Validate`.
10. Quay lại `Delivery` của SO.
11. `Check Availability`.
12. `Validate Delivery`.

## Dấu hiệu test thành công

- SO tạo được dù tồn = 0.
- Có RFQ/PO sinh ra từ SO.
- Receipt nhập kho thành công.
- Delivery của khách được cấp hàng sau khi hàng về.
- Có thể tiếp tục invoice như quy trình bán bình thường.

---

## 8) Quy trình mẫu đầy đủ để nhân viên mới luyện tập

## Bài tập thực hành

1. Tạo kho `KSR`.
2. Tạo location `Khu A/Kệ A1/Ngăn 01`.
3. Tạo sản phẩm `Dam da hoi A`.
4. Nhập tồn đầu kỳ 20.
5. Tạo SO bán 2 sản phẩm.
6. Kho validate delivery.
7. Kế toán tạo invoice và thu tiền.

## Tiêu chí đạt

- Tồn kho cuối còn 18.
- Đơn hàng ở trạng thái hoàn tất.
- Hóa đơn ở trạng thái paid.

---

## 9) Checklist lỗi thực tế thường gặp

- Nhân viên sales không confirm đơn được -> thiếu quyền Sales User/Manager.
- Xác nhận SO không tạo delivery -> chưa cài `sale_stock`.
- Delivery không validate được -> chưa nhập done quantity hoặc thiếu hàng.
- Không tạo invoice được -> quyền accounting chưa đủ.
- Tồn kho không trừ -> delivery chưa `Done`.

---

## 10) Gợi ý bước tiếp theo

Sau khi team thao tác thuần các bước trên, mới mở rộng:

1. Reordering rules tự động mua bù.
2. Barcode vận hành thực tế tại kho.
3. Tích hợp thanh toán online.
4. Custom module nâng cao theo TO-BE.

---

## 10.1) Thiết lập phân quyền chi tiết (2 Sales, 2 Kho, 1 Quản lý, 1 Admin)

## Mục tiêu

Thiết lập quyền đủ dùng cho đội vận hành hiện tại:

- 2 nhân viên Sales.
- 2 nhân viên Kho.
- 1 Quản lý.
- 1 Admin toàn quyền.

Đảm bảo:

- Nhân viên chỉ thấy và thao tác đúng phần việc.
- Tránh sửa nhầm cấu hình route/rule gây vỡ luồng kho.
- Vẫn có 1 user quản trị để xử lý tình huống phát sinh.

## Cấu trúc vai trò và phạm vi quyền

### 1) Sales User (2 người)

- Tạo/sửa/confirm báo giá, đơn bán theo phạm vi được cấp.
- Xem Delivery liên quan đơn bán để theo dõi trạng thái giao.
- Không được validate phiếu kho.
- Không được sửa cấu hình `Warehouse/Routes/Rules`.

### 2) Inventory User - Kho (2 người)

- Xử lý vận hành kho hằng ngày:
  - Nhận hàng `IN -> QC -> STOR`
  - Giao hàng `PICK -> PACK -> OUT`
  - Xử lý popup `Create Backorder` khi giao thiếu.
- Được xem SO/PO liên quan để đối chiếu.
- Không được chỉnh cấu hình route/rule/kho.

### 3) Manager (1 người)

- Quản lý tổng thể các bộ phận Sales, Purchase, Inventory.
- Duyệt PO, kiểm tra vận hành, xử lý ngoại lệ nghiệp vụ.
- Không bắt buộc có quyền kỹ thuật hệ thống sâu.

### 4) Admin (1 người)

- Toàn quyền hệ thống.
- Quản lý user, nhóm quyền, cấu hình modules.
- Là user duy nhất nên được phép chỉnh `Routes/Rules/Warehouse Settings`.

## Ma trận quyền đề xuất

| Vai trò | Sales | Purchase | Inventory | Settings/Technical |
| --- | --- | --- | --- | --- |
| Sales User | User (Own hoặc All Documents theo chính sách) | Không cấp | Read-only | Không cấp |
| Kho User | Read-only | Read-only (tuỳ cần) | User | Không cấp |
| Manager | Administrator | Administrator | Administrator | Không cấp hoặc cấp hạn chế |
| Admin | Administrator | Administrator | Administrator | Administrator |

> Khuyến nghị: chỉ `Admin` được phép sửa route/rule kho để tránh xung đột luồng MTO + Deliver 3 steps.

## Các bước thao tác cấp quyền trong Odoo

### Bước 1: Tạo người dùng

1. Vào `Settings -> Users & Companies -> Users`.
2. Bấm `New`.
3. Tạo đủ 6 user:
   - `sales_01`, `sales_02`
   - `kho_01`, `kho_02`
   - `manager_01`
   - `admin_01` (hoặc dùng admin hiện tại)
4. Điền thông tin cơ bản: tên, email/login, công ty, ngôn ngữ.
5. `Save`.

### Bước 2: Gán quyền cho 2 Sales

Mở từng user Sales và gán:

- `Sales`: `User: Own Documents Only` (hoặc `All Documents` nếu 2 sales xử lý chéo đơn).
- `Inventory`: chỉ mức đọc (không cấp `Inventory User/Manager`).
- `Purchase`: `None`.
- `Administration/Settings`: `None`.

`Save`.

### Bước 3: Gán quyền cho 2 user Kho

Mở từng user Kho và gán:

- `Inventory`: `User`.
- `Sales`: mức đọc (nếu cần xem SO liên quan giao hàng).
- `Purchase`: mức đọc (nếu cần tra PO/Receipt).
- Không cấp quyền quản trị cấu hình.

`Save`.

### Bước 4: Gán quyền cho Manager

Mở user Manager và gán:

- `Sales`: `Administrator`.
- `Purchase`: `Administrator`.
- `Inventory`: `Administrator`.
- `Settings`: không cấp quyền kỹ thuật nếu không cần can thiệp hệ thống.

`Save`.

### Bước 5: Gán quyền cho Admin

Mở user Admin và đảm bảo:

- `Sales/Purchase/Inventory`: `Administrator`.
- `Administration/Settings`: `Administrator`.

`Save`.

### Bước 6: Cách đăng nhập nhiều account trên cùng 1 hệ thống (1 máy local)

Mục tiêu bước này:

- Demo đúng quy trình chuyển vai `Sales -> Kho -> Manager` trên cùng database.
- Không cần nhiều máy, chỉ cần 1 máy local.

#### Cách A (đơn giản): đăng xuất và đăng nhập lại

1. Đăng nhập bằng `sales_01`.
2. Tạo và confirm SO.
3. Bấm avatar góc phải -> `Log out`.
4. Đăng nhập bằng `kho_01`.
5. Vào `Inventory` xử lý transfer theo SO vừa tạo.
6. Nếu cần bước duyệt/kiểm tra quản trị:
   - `Log out` -> đăng nhập `manager_01`.

Ưu điểm:

- Dễ làm, không cần cài thêm gì.

Nhược điểm:

- Chuyển vai hơi mất thời gian do phải nhập lại mật khẩu.

#### Cách B (khuyến nghị khi demo): mở nhiều profile trình duyệt

1. Mở 3 profile/cửa sổ trình duyệt khác nhau:
   - Profile 1: đăng nhập `sales_01`
   - Profile 2: đăng nhập `kho_01`
   - Profile 3: đăng nhập `manager_01`
2. Mỗi profile truy cập cùng URL hệ thống Odoo local.
3. Khi demo chuyển bước, chỉ cần đổi cửa sổ/profile, không cần logout.

Ưu điểm:

- Demo nhanh, liền mạch.
- Dễ cho người mới hiểu rõ phân vai thực tế.

> Có thể dùng 3 trình duyệt khác nhau (Chrome/Edge/Firefox) nếu không dùng profile.

#### Cách C (không khuyến nghị): 1 account đổi quyền liên tục

Không nên áp dụng trong vận hành và đào tạo vì:

- Không phản ánh đúng phân tách trách nhiệm.
- Dễ sai lệch quyền và khó audit.

## Kịch bản demo chuẩn step-by-step (Sales -> Kho -> Manager)

### Bước 1 - Sales tạo đơn

1. Đăng nhập `sales_01`.
2. Vào `Sales -> Orders -> Quotations`.
3. Tạo SO mới, thêm sản phẩm, `Confirm`.
4. Ghi lại mã SO (ví dụ `S00030`).

### Bước 2 - Kho xử lý xuất hàng

1. Chuyển sang account `kho_01`.
2. Vào `Inventory -> Operations -> Transfers` (hoặc Delivery Orders).
3. Tìm `Source Document = S00030`.
4. Xử lý theo trạng thái:
   - Đủ hàng: `PICK -> PACK -> OUT` và `Validate`.
   - Thiếu hàng: giao phần có sẵn và chọn `Create Backorder`.

### Bước 3 - Manager kiểm tra và duyệt

1. Chuyển sang account `manager_01`.
2. Mở SO `S00030` để kiểm tra trạng thái giao.
3. Nếu đơn thiếu hàng MTO:
   - vào `Purchase` kiểm tra/duyệt PO liên quan.

### Bước 4 - Admin kiểm tra quyền (khi cần)

1. Đăng nhập `admin_01`.
2. Vào `Settings -> Users`.
3. Kiểm tra lại nhóm quyền từng user đúng ma trận đã thiết lập.

## Checklist nhanh để xác nhận demo phân vai đúng

- `sales_01` tạo được SO nhưng không validate được transfer.
- `kho_01` validate được transfer nhưng không sửa được route/rule.
- `manager_01` xem và quản trị nghiệp vụ liên phòng ban.
- `admin_01` quản trị toàn quyền.

## Thiết lập bảo vệ cấu hình quan trọng (rất nên làm)

1. Chỉ Admin được truy cập menu:
   - `Inventory -> Configuration -> Routes`
   - `Inventory -> Configuration -> Rules`
   - `Inventory -> Configuration -> Warehouses`
2. Không cấp quyền chỉnh product route cho user vận hành thường.
3. Thống nhất SOP:
   - Khi giao thiếu hàng, user kho chọn `Create Backorder`, không chọn `No Backorder` nếu còn nhu cầu giao.

## Checklist test quyền sau khi cấu hình (10-15 phút)

### Test A - User Sales

- Đăng nhập `sales_01`.
- Tạo và confirm 1 SO.
- Kỳ vọng:
  - Làm được SO.
  - Xem được Delivery.
  - Không thấy/sửa được menu `Routes/Rules/Warehouse`.
  - Không validate được phiếu kho.

### Test B - User Kho

- Đăng nhập `kho_01`.
- Mở transfer của SO test và xử lý `PICK/PACK/OUT`.
- Kỳ vọng:
  - Validate được transfer.
  - Xử lý được backorder.
  - Không truy cập được cấu hình route/rule.

### Test C - Manager

- Đăng nhập `manager_01`.
- Duyệt PO, xem vận hành kho, kiểm tra báo cáo.
- Kỳ vọng:
  - Quản trị nghiệp vụ được.
  - Nếu không cấp kỹ thuật thì không vào phần technical settings.

### Test D - Admin

- Đăng nhập `admin_01`.
- Kiểm tra tạo user, đổi quyền, chỉnh route/rule.
- Kỳ vọng:
  - Toàn quyền đầy đủ.

## Gợi ý vận hành để quy trình ổn định

- Mỗi vai trò dùng đúng account riêng, không dùng chung.
- Đổi mật khẩu định kỳ cho `manager/admin`.
- Chỉ sửa route/rule khi có yêu cầu thay đổi quy trình và có test trước.
- Khi thay đổi cấu hình quyền lớn, luôn test lại 4 case ở checklist trên.

---

## 11) Thiết lập POS (Point of Sale) từ đầu đến cuối

## Mục tiêu

Thiết lập hoàn chỉnh kênh bán tại quầy trên Odoo để nhân viên có thể:

1. Mở ca bán hàng.
2. Chọn sản phẩm và thanh toán.
3. Đóng ca và đối soát.
4. Kiểm tra lại đơn hàng, tồn kho, và số liệu tiền.

## Điều kiện tiên quyết

- Đã có dữ liệu cơ bản: công ty, kho, sản phẩm.
- Người cấu hình có quyền `POS Manager` hoặc quyền quản trị tương đương.
- Người vận hành quầy có quyền `POS User`.
- Hệ thống có `Inventory` để trừ tồn theo đơn POS.
- Không bắt buộc cài `Accounting/Invoicing`; vẫn theo dõi được doanh thu theo phiên và phương thức thanh toán ngay trong POS.

## Luồng tổng quan

`Cài POS -> Tạo payment method -> Gắn sản phẩm vào POS -> Tạo quầy -> Mở ca -> Bán -> Đóng ca -> Kiểm tra số liệu`

## Các bước thao tác chi tiết

### Bước 1: Cài app POS và gán quyền

#### 1.1 Cài app

1. Vào `Apps`.
2. Tìm `Point of Sale`.
3. Nếu chưa cài, bấm `Install`.
4. Chờ cài xong, kiểm tra trên thanh ứng dụng đã có app `Point of Sale`.

#### 1.2 Gán quyền người dùng

1. Vào `Settings -> Users & Companies -> Users`.
2. Mở user cần cấp quyền.
3. Ở phần quyền liên quan POS:
   - User vận hành quầy: chọn `Point of Sale: User`.
   - User quản trị quầy: chọn `Point of Sale: Manager`.
4. `Save`.

## Kết quả mong đợi bước 1

- Đã thấy app `Point of Sale`.
- User đăng nhập đúng quyền, mở được menu POS.

### Bước 2: Xác định mô hình vận hành POS (không kế toán / có kế toán)

1. Nếu doanh nghiệp chỉ cần vận hành bán hàng tại quầy:
   - Chạy theo mô hình `POS-only` (không bắt buộc dùng `Accounting/Invoicing`).
   - Theo dõi tiền theo `Session`, `Payment Methods`, và báo cáo POS.
2. Nếu doanh nghiệp cần hạch toán sổ sách đầy đủ:
   - Dùng thêm `Accounting/Invoicing` để đối soát journal entries.
3. Khuyến nghị cho giai đoạn triển khai nhanh:
   - Chốt trước mô hình `POS-only`, sau đó mở rộng kế toán khi vận hành ổn định.

## Kết quả mong đợi bước 2

- Đã thống nhất mô hình triển khai POS của doanh nghiệp.

### Bước 3: Tạo phương thức thanh toán (Payment Methods)

1. Vào `Point of Sale -> Configuration -> Payment Methods`.
2. Bấm `New`.
3. Điền:
   - `Name`: ví dụ `Tiền mặt`, `Chuyển khoản`, `Thẻ`.
   - Nếu có trường `Journal`: chọn đúng sổ tương ứng.
   - Nếu không dùng kế toán và giao diện không yêu cầu `Journal`: có thể lưu trực tiếp.
4. `Save`.
5. Lặp lại cho tất cả hình thức thanh toán tại quầy.
6. Mở form quầy POS để đảm bảo các payment method vừa tạo đã được gắn vào quầy.

## Kết quả mong đợi bước 3

- Danh sách Payment Methods có đủ phương thức quầy cần dùng.

### Bước 4: Cấu hình sản phẩm hiển thị trên POS

#### 4.1 Tạo POS Product Categories (khuyến nghị)

1. Vào `Point of Sale -> Configuration -> Products -> PoS Product Categories`.
2. Bấm `New`.
3. Điền:
   - `Name`: ví dụ `Áo dài`, `Đầm dài`, `Phụ kiện`.
   - `Parent Category` nếu muốn phân cấp.
4. `Save`.

#### 4.2 Bật sản phẩm cho POS

1. Vào `Inventory -> Products -> Products` (hoặc menu Products trong POS).
2. Mở sản phẩm cần bán tại quầy.
3. Trong phần `Point of Sale`:
   - Tick `Available in POS`.
   - Chọn `POS Product Category` (nếu đã tạo).
4. `Save`.
5. Làm cho tất cả sản phẩm cần bán POS.

> Nếu sản phẩm có biến thể size, kiểm tra biến thể nào được bán và mã SKU rõ ràng để tránh thu ngân chọn nhầm.

## Kết quả mong đợi bước 4

- Sản phẩm xuất hiện trong giao diện POS theo nhóm category.

### Bước 5: Tạo quầy POS (Point of Sale / Shop)

1. Vào `Point of Sale -> Configuration -> Point of Sales`.
2. Bấm `New`.
3. Điền tối thiểu:
   - `Name`: ví dụ `POS - Showroom Phú Nhuận`.
   - `Company`.
   - `Warehouse`: kho xuất hàng của quầy.
   - `Payment Methods`: thêm các phương thức từ Bước 3.
   - `Pricelist` mặc định (nếu dùng).
4. `Save`.

#### Thiết lập khuyến nghị ngay sau khi tạo quầy

- Trong form quầy, kiểm tra thêm:
  - Có bật in biên lai hay không.
  - Có bật `Cash Control` hay không (nhập tiền đầu ca/đối soát cuối ca).
  - Có cho phép chiết khấu hay không.

## Kết quả mong đợi bước 5

- Trên `POS Dashboard` đã có thẻ quầy mới.

### Bước 6: Cài đặt POS chung (tùy nhu cầu)

1. Vào `Point of Sale -> Configuration -> Settings`.
2. Thiết lập theo chính sách cửa hàng:
   - Receipts (in biên lai tự động/thủ công).
   - Discount (cho phép giảm giá dòng hoặc toàn đơn).
   - Pricelists.
   - Customer display / thiết bị in nếu có.
3. `Save`.

## Kết quả mong đợi bước 6

- Tùy chọn toàn hệ thống POS được áp dụng cho các quầy.

### Bước 7: Quy trình vận hành tại quầy

#### 7.1 Mở ca

1. Vào `Point of Sale -> Dashboard`.
2. Chọn quầy cần chạy.
3. Bấm `Open Session` (hoặc `New Session` / `Open Register` tùy giao diện).
4. Nếu bật cash control:
   - Nhập `Opening Cash` (tiền đầu ca).
   - Xác nhận mở ca.

#### 7.2 Bán hàng

1. Trên màn hình POS, chọn sản phẩm.
2. Chỉnh số lượng nếu cần.
3. Chọn khách hàng nếu muốn gắn customer.
4. Bấm `Payment`.
5. Chọn phương thức thanh toán.
6. Nhập số tiền nhận (nếu tiền mặt) -> xác nhận.
7. In hoặc gửi biên lai.

#### 7.2A Xuất Invoice từ POS (khi đã có Invoicing)

> Áp dụng khi doanh nghiệp đã cài `Invoicing` và muốn xuất hóa đơn cho đơn bán tại quầy.

##### A. Điều kiện bắt buộc trước khi thao tác

1. Đã cài app `Invoicing` (hoặc `Accounting`) và đang dùng được như kênh Sales.
2. Trong cấu hình quầy POS, đã bật tùy chọn cho phép tạo `Invoice`.
3. Thu ngân có quyền thao tác POS và quyền tối thiểu để tạo/gửi invoice.
4. Đã có thông tin khách hàng:
   - Tên khách hàng.
   - Email (nếu gửi online).
   - Thông tin thuế theo quy định nội bộ (nếu doanh nghiệp yêu cầu).

##### B. Cấu hình 1 lần cho quầy POS (manager thực hiện)

1. Vào `Point of Sale -> Configuration -> Point of Sales`.
2. Mở quầy cần dùng.
3. Trong phần liên quan hóa đơn/kế toán:
   - Bật tùy chọn `Invoice` (hoặc tên tương đương theo giao diện).
   - Kiểm tra các cấu hình mặc định liên quan invoice (journal, template email) nếu hệ thống yêu cầu.
4. `Save`.
5. Thực hiện test nhanh 1 đơn để xác nhận quầy tạo invoice được.

##### C. Thao tác thu ngân: tạo invoice ngay khi bán

1. Mở POS session như bình thường.
2. Chọn sản phẩm khách cần mua.
3. Bấm chọn `Customer`:
   - Tìm khách cũ hoặc tạo mới nhanh.
   - Nhập email nếu dự kiến gửi online.
4. Bấm `Payment` và hoàn tất thanh toán.
5. Bấm `Invoice` / `Generate Invoice` (tên nút có thể khác nhau theo phiên bản giao diện).
6. Kiểm tra trạng thái hệ thống:
   - Đơn POS đã liên kết với chứng từ invoice.
   - Không có cảnh báo lỗi cấu hình.

##### D. Xuất invoice cho khách: 2 phương án vận hành

1. **Gửi online qua email (khuyến nghị)**:
   - Mở invoice vừa tạo.
   - Bấm `Send` / `Send & Print`.
   - Kiểm tra người nhận là email khách.
   - Gửi mail có file PDF invoice đính kèm.
2. **In giấy tại quầy hoặc back-office**:
   - Mở invoice.
   - Bấm `Print`.
   - Chọn mẫu in invoice chuẩn doanh nghiệp.
   - In A4 và giao khách.

##### E. Hậu kiểm invoice sau ca (bắt buộc)

1. Vào `Point of Sale -> Orders -> Orders`, mở đơn vừa bán:
   - Xác nhận có liên kết đến invoice.
2. Vào `Invoicing -> Customers -> Invoices`:
   - Lọc theo ngày/quầy/thu ngân.
   - Kiểm tra đủ số lượng invoice cần xuất.
3. Kiểm tra nhanh chất lượng dữ liệu:
   - Đúng khách hàng.
   - Đúng tổng tiền/thuế.
   - Đúng trạng thái gửi email hoặc đã in giấy.

##### F. Lỗi thường gặp khi xuất invoice từ POS và cách xử lý

- **Không thấy nút Invoice trên POS**:
  - Chưa bật tùy chọn invoice ở cấu hình quầy.
  - User hiện tại thiếu quyền liên quan invoice.
- **Bấm Invoice nhưng không tạo được**:
  - Chưa chọn `Customer` trên đơn POS.
  - Cấu hình kế toán nền (journal/tax) chưa đầy đủ theo yêu cầu hệ thống.
- **Gửi email thất bại**:
  - Khách chưa có email hoặc email sai định dạng.
  - Mail server/outgoing mail chưa cấu hình hoặc đang lỗi.
- **In được receipt nhưng không có invoice**:
  - Receipt POS là chứng từ bán hàng tại quầy, không thay thế invoice.
  - Cần thao tác thêm bước `Generate Invoice` sau thanh toán.
- **Số liệu POS và Invoicing lệch nhau**:
  - Một số đơn chưa tạo invoice.
  - Người dùng sửa/hủy invoice ngoài quy trình chuẩn.

#### 7.3 Đóng ca

1. Bấm `Close` / quay về dashboard của quầy.
2. Chọn `Close Session`.
3. Đếm tiền thực tế tại quầy.
4. Nhập số tiền kiểm đếm vào wizard.
5. Xác nhận `Validate Closing`.
6. Nếu lệch tiền, ghi nhận chênh lệch theo quy trình nội bộ.

## Kết quả mong đợi bước 7

- Phiên POS chuyển sang trạng thái đóng.
- Toàn bộ đơn trong ca đã ghi nhận đầy đủ.

### Bước 8: Hậu kiểm sau đóng ca

#### 8.1 Kiểm tra đơn và thanh toán POS

1. Vào `Point of Sale -> Orders -> Orders`.
2. Lọc theo ngày/quầy để kiểm tra đơn vừa bán.
3. Vào `Point of Sale -> Orders -> Payments` để kiểm tra thanh toán theo phương thức.

#### 8.2 Kiểm tra tồn kho

1. Mở sản phẩm vừa bán.
2. Xem tồn kho tại kho gắn với quầy.
3. Xác nhận tồn đã trừ đúng theo số lượng bán.

#### 8.3 Kiểm tra kế toán (nếu áp dụng)

1. Chỉ thực hiện bước này khi doanh nghiệp có dùng `Accounting/Invoicing`.
2. Vào `Accounting/Invoicing`.
3. Kiểm tra journal entries liên quan cash/bank của POS.
4. Đối chiếu tổng tiền theo ca với báo cáo POS.

## Kết quả mong đợi cuối cùng

- Quầy POS hoạt động đầy đủ: mở ca, bán, thanh toán, đóng ca.
- Sản phẩm hiện đúng trên POS, tồn kho giảm đúng kho.
- Số liệu thanh toán và đối soát cuối ca khớp thực tế.

## Cách test nhanh (10-15 phút cho người mới)

1. Tạo 1 payment method `Tiền mặt` (gắn journal nếu hệ thống yêu cầu).
2. Bật `Available in POS` cho 1 sản phẩm mẫu.
3. Tạo 1 quầy POS mới và gắn kho + payment method.
4. Mở ca với tiền đầu ca nhỏ.
5. Bán 1 đơn 1 sản phẩm.
6. Đóng ca.
7. Kiểm tra đơn POS và tồn kho giảm đúng 1.

## Lỗi thường gặp và cách xử lý nhanh

- **Không thấy sản phẩm trên màn hình POS**: chưa tick `Available in POS` hoặc lọc category sai.
- **Không thanh toán được**: quầy chưa gắn payment methods hoặc payment method thiếu cấu hình bắt buộc (ví dụ journal khi hệ thống yêu cầu).
- **Mở POS báo lỗi liên quan kế toán**: đang bật tùy chọn invoicing/kế toán nhưng công ty chưa cấu hình đủ dữ liệu kế toán nền.
- **Tồn không trừ đúng kho**: quầy gắn sai warehouse hoặc sản phẩm không phải loại quản tồn theo quy trình đang dùng.
- **Không sửa được một số thiết lập quầy**: đang có session mở, cần đóng session trước.

---

## 11.1) Cấu hình POS đồng bộ với Sales/Inventory (chi tiết rule vận hành)

## Mục tiêu

Thiết lập POS để:

- Trừ tồn kho đúng theo kho/quầy.
- Không xung đột với luồng `Sales Order` và `Delivery`.
- Đồng bộ giá bán, khuyến mãi, báo cáo doanh thu giữa POS và Sales.

## Nguyên tắc đồng bộ tổng thể (bắt buộc thống nhất)

1. Mỗi quầy POS phải gắn đúng `Warehouse`.
2. Sản phẩm bán ở POS phải là sản phẩm đang quản lý tồn kho đúng chuẩn (`Goods/Storable` + UoM đúng).
3. Không để cùng một nhân viên vừa bán POS vừa sửa cấu hình route/rule kho.
4. Chốt rõ quy tắc:
   - Bán tại quầy: dùng `POS Order`.
   - Bán theo đơn đặt trước/giao sau: dùng `Sales Order`.
5. Tránh nhập liệu trùng:
   - Không tạo SO cho giao dịch đã thanh toán trực tiếp tại POS, trừ khi doanh nghiệp có quy trình tích hợp đặc biệt.

## Bộ rule khuyến nghị cho POS

### Rule 1 - Mapping kho/quầy

- Mỗi POS config gắn 1 `Warehouse` chính.
- Nếu nhiều cửa hàng vật lý, mỗi cửa hàng nên có quầy POS riêng và kho riêng.
- Không dùng 1 quầy POS cho nhiều kho khác nhau trong cùng ca.

### Rule 2 - Quy tắc sản phẩm bán tại quầy

- Chỉ bật `Available in POS` cho sản phẩm được phép bán tại quầy.
- Sản phẩm cần quản lý tồn phải là `Goods/Storable`.
- Sản phẩm dịch vụ (`Service`) không làm thay đổi tồn.
- Với sản phẩm biến thể size/màu:
  - Chuẩn hóa SKU từng variant.
  - Kiểm tra thu ngân chọn đúng biến thể.

### Rule 3 - Giá bán và khuyến mãi

- Chốt một nguồn giá chính:
  - Nếu dùng `Pricelist`, dùng đồng nhất cho POS và Sales theo từng nhóm khách.
- Không cho phép user thường sửa giá trực tiếp tại quầy nếu chưa có quy định.
- Nếu bật discount ở POS:
  - Quy định mức tối đa nhân viên được giảm.
  - Mức cao hơn phải do quản lý xử lý.

### Rule 4 - Thanh toán và đối soát

- Mỗi phương thức thanh toán POS phải map đúng kênh thu tiền (Cash/Bank/Card).
- Bật `Cash Control` nếu có tiền mặt.
- Cuối ca luôn đối soát:
  - Tiền thực tế
  - Báo cáo session
  - Chênh lệch (nếu có) phải ghi nhận lý do.

### Rule 5 - Đồng bộ với Sales (không xung đột nghiệp vụ)

- Giao dịch khách trả ngay lấy ngay:
  - Chạy hoàn toàn qua POS.
- Giao dịch đặt cọc/giao sau/đơn số lượng lớn:
  - Chạy qua Sales Order để theo dõi `Delivery` và backorder.
- Không xử lý một giao dịch bằng cả POS và SO nếu không có SOP tách phần rõ ràng.

#### Ví dụ thực tế: Khách đang mua tại quầy nhưng hàng đã hết

- Tình huống:
  - Thu ngân đang tạo đơn trên POS, khách muốn lấy thêm sản phẩm nhưng tồn kho quầy đã hết.
- Cách xử lý chuẩn:
  1. Không cố hoàn tất phần hàng hết trong POS.
  2. Giữ POS chỉ cho phần khách nhận ngay tại quầy (nếu có).
  3. Phần hàng giao sau/chờ nhập: tạo `Sales Order` riêng để theo dõi giao hàng.
  4. Nếu đơn hiện tại chỉ gồm hàng hết:
     - Hủy đơn nháp trên POS, chuyển toàn bộ giao dịch sang `Sales Order`.
- Lý do:
  - `Sales Order` theo dõi được đặt cọc, công nợ, delivery/backorder.
  - Tránh trùng doanh thu/chứng từ do ghi cùng một giao dịch ở cả POS và SO.

#### Lưu ý hệ thống khi thao tác tại POS

- Odoo mặc định không tự nhảy từ POS sang SO khi sản phẩm hết hàng.
- Thu ngân phải thao tác thủ công theo SOP:
  - Hủy hoặc tách phần hàng trên POS (tùy tình huống),
  - Sau đó vào `Sales` tạo `Sales Order` cho phần giao sau.

## Cấu hình chi tiết trong Odoo (step-by-step)

### Bước 1: Chuẩn hóa kho cho POS

1. Vào `Inventory -> Configuration -> Warehouses`.
2. Xác định kho phục vụ bán quầy (ví dụ `KMS`).
3. Đảm bảo kho đã chạy đúng luồng nội bộ theo quy trình doanh nghiệp.
4. Ghi nhận kho này để gán cho POS.

### Bước 2: Chuẩn hóa sản phẩm cho POS

1. Vào `Inventory -> Products -> Products`.
2. Mở từng sản phẩm bán tại quầy.
3. Kiểm tra:
   - `Product Type` phù hợp (`Goods/Storable` nếu cần trừ tồn).
   - SKU/Variant đầy đủ.
   - Tick `Available in POS`.
4. `Save`.

### Bước 3: Cấu hình quầy POS đồng bộ kho

1. Vào `Point of Sale -> Configuration -> Point of Sales`.
2. Mở quầy POS.
3. Kiểm tra:
   - `Warehouse` đúng kho quầy.
   - `Payment Methods` đủ dùng.
   - `Pricelist` đúng chính sách giá.
4. `Save`.

### Bước 4: Cấu hình quyền user POS để tránh lỗi vận hành

1. `Settings -> Users`.
2. User thu ngân:
   - `Point of Sale`: `User`
   - Không cấp quyền chỉnh route/rule kho.
3. User quản lý quầy:
   - `Point of Sale`: `Manager`
4. `Save`.

### Bước 5: Test liên thông POS - Inventory - Sales

1. Mở ca POS.
2. Bán thử 1 đơn tại quầy.
3. Thanh toán và hoàn tất.
4. Kiểm tra:
   - `POS Orders` có đơn.
   - Tồn kho giảm đúng ở kho gắn quầy.
5. Tạo 1 SO riêng (đặt trước) để xác nhận luồng SO vẫn chạy độc lập.

## Tình huống thực tế và SOP xử lý

### TH1 - Bán tại quầy khi hàng sắp hết

- Thu ngân bán bình thường nếu hệ thống cho phép.
- Quản lý kho theo dõi `Replenishment` để bổ sung.
- Không để thu ngân tự sửa cấu hình route.

### TH2 - Khách cần giao sau / chưa nhận hàng ngay

- Không nên cố xử lý qua POS nếu cần theo dõi giao hàng nhiều bước.
- Tạo `Sales Order` để chạy luồng `Delivery`.

### TH3 - Khách đổi/trả hàng tại quầy

- Áp dụng đúng flow return của POS (hoặc Inventory Return tùy chính sách).
- Sau thao tác return, kiểm tra tồn kho đã cộng lại đúng location.

### TH4 - Khách mua cả tại quầy và đặt thêm hàng

- Tách thành 2 nghiệp vụ:
  - Phần lấy ngay -> POS.
  - Phần đặt thêm -> SO.
- Ghi chú liên kết mã chứng từ để dễ đối soát.

## Checklist chuẩn để vận hành ổn định hằng ngày

- Mở ca:
  - Kiểm tra đúng quầy, đúng kho, đúng payment methods.
- Trong ca:
  - Không đổi cấu hình quầy khi đang có session mở.
  - Không cho user thường đổi giá tùy tiện.
- Cuối ca:
  - Đóng session.
  - Đối soát tiền và báo cáo.
  - Kiểm tra top sản phẩm và tồn giảm bất thường.

## KPI nên theo dõi cho POS đồng bộ Sales

- Doanh thu theo quầy/ngày.
- Số đơn POS vs số đơn SO (để phát hiện nhập trùng).
- Tỷ lệ đổi/trả.
- Chênh lệch quỹ cuối ca.
- Sản phẩm bán chạy nhưng hay hết hàng (để tối ưu replenishment).

## Dấu hiệu cấu hình đúng

- Bán POS xong, tồn giảm đúng kho.
- Đơn SO không bị trùng doanh thu với POS.
- Báo cáo cuối ca khớp tiền thực tế.
- User thu ngân không vào được menu cấu hình nhạy cảm.

---

## 11.2) Quy trình vận hành thực chiến theo vai trò (phù hợp mô hình hiện tại)

## Mục tiêu

Đưa toàn bộ quy trình thực tế vào một playbook duy nhất cho mô hình của bạn:

- 2 Sales
- 2 Kho
- 1 Manager
- 1 Admin
- Luồng chính: `Sales + MTO/Buy + Receive 3 steps + Deliver 3 steps + POS`

## Phần A - Chuẩn vận hành theo vai trò (ai làm gì, khi nào)

### A1) Sales (hằng ngày)

1. Nhận nhu cầu khách.
2. Chọn đúng kiểu xử lý:
   - Lấy ngay tại quầy -> POS.
   - Đặt trước/giao sau -> SO.
3. Với SO:
   - Nếu hàng có sẵn: để trống route dòng (MTS).
   - Nếu thiếu hàng và muốn kéo mua theo đơn: chọn route MTO ở dòng (nếu được phân quyền).
4. Confirm SO.
5. Theo dõi trạng thái:
   - Delivery
   - Nếu thiếu hàng: backorder + PO liên quan.

### A2) Kho (hằng ngày)

1. Mở danh sách transfer theo `Ready/Waiting`.
2. Xử lý theo thứ tự ưu tiên:
   - `IN -> QC -> STOR`
   - `PICK -> PACK -> OUT`
3. Khi giao thiếu:
   - `Validate` phần có hàng
   - chọn `Create Backorder`.
4. Không tự ý chỉnh route/rule.

### A3) Purchase/Manager

1. Kiểm tra RFQ/PO do MTO sinh.
2. Confirm PO đúng SLA.
3. Theo dõi PO trễ.
4. Phối hợp kho để nhận hàng đúng luồng 3 bước nhập.

### A4) Admin

1. Quản lý user/role.
2. Chỉ Admin được chỉnh:
   - Warehouse
   - Routes
   - Rules
3. Khi đổi cấu hình phải test lại checklist cuối mục này.

## Phần B - Decision tree nhanh (Sales chọn POS hay SO, MTS hay MTO)

### B1) Chọn POS hay SO

- Khách trả tiền và lấy ngay -> POS.
- Khách cần giao sau, đặt giữ hàng, đặt số lượng lớn -> SO.
- Đơn có khả năng backorder hoặc giao nhiều đợt -> ưu tiên SO.

### B2) Chọn MTS hay MTO trên SO

- Hàng còn đủ tồn và muốn xuất ngay -> MTS (để trống route dòng).
- Hàng thiếu, cần kéo mua theo đơn -> MTO (route dòng MTO, sản phẩm đã có Buy/Vendor).

## Phần C - SOP theo tình huống (step-by-step chi tiết)

### TH-C1: Đơn có 1 hàng sẵn + 1 hàng thiếu (giao 2 đợt)

1. Sales tạo SO gồm 2 dòng.
2. Confirm SO.
3. Kho xử lý dòng có sẵn:
   - Pick/Pack/Out phần có hàng.
4. Popup thiếu hàng:
   - chọn `Create Backorder`.
5. Purchase/Manager:
   - Confirm PO do MTO sinh.
6. Kho nhận hàng:
   - `IN -> QC -> STOR`.
7. Kho quay lại backorder:
   - hoàn tất `PICK -> PACK -> OUT` phần còn lại.
8. Sales theo dõi trạng thái giao đủ.

### TH-C2: Khách đến quầy, hết hàng, muốn giữ đơn

1. Không cố ép qua POS nếu chưa có hàng và cần theo dõi giao.
2. Tạo SO cho khách.
3. Chọn MTO (nếu cần kéo mua theo đơn).
4. Thu cọc theo chính sách công ty (nếu áp dụng).
5. Theo dõi PO và giao sau khi hàng về.

### TH-C3: Đổi/trả từ POS

1. Tạo nghiệp vụ return đúng trong POS/Inventory.
2. Kiểm tra hàng hoàn về đúng location.
3. Đối chiếu tiền hoàn và session cuối ca.

## Phần D - Bảng kiểm soát lỗi thường gặp (đúng case hệ của bạn)

### D1) Lỗi: Không thấy bước OUT sau PICK

Kiểm tra theo thứ tự:

1. PICK đã `Validate` chưa?
2. Hàng đã vào đúng location nguồn chưa (STOR xong chưa)?
3. Rule Deliver 3 bước còn đúng không:
   - Pull Stock->Customers
   - Push Packing->Output
   - Push Output->Customers
4. Có user nào chỉnh route/rule gần đây không?

### D2) Lỗi: SO không sinh PO khi thiếu hàng

1. Sản phẩm đã có `Buy` chưa?
2. Dòng SO đã chọn MTO chưa (nếu bạn dùng chọn theo dòng)?
3. Vendor đã khai báo chưa?
4. User có confirm SO thành công chưa?

### D3) Lỗi: POS trừ tồn sai kho

1. POS config có đúng Warehouse không?
2. Product có đúng loại quản tồn không?
3. Có đang mở nhiều session/quầy dùng sai kho không?

### D4) Lỗi: Sales không chọn được route trên dòng SO

1. Route MTO đã bật `Sales Order Lines` chưa?
2. User Sales có đủ quyền đọc route không (trong hệ quyền rút gọn có thể cần `Inventory=User`)?
3. Sản phẩm có route nền phù hợp không (Buy/Vendor)?

## Phần E - Checklist test hồi quy sau mỗi lần đổi cấu hình

Sau khi chỉnh quyền, route hoặc POS config, bắt buộc test 6 case:

1. **SO MTS**: hàng có sẵn -> giao đủ một lần.
2. **SO MTO**: hàng thiếu -> sinh PO -> nhận hàng -> giao.
3. **SO mixed**: một phần giao trước + backorder.
4. **POS đơn thường**: bán xong trừ tồn đúng kho.
5. **POS return**: trả hàng cộng tồn lại đúng.
6. **Phân quyền**:
   - Sales không chỉnh route/rule.
   - Kho không chỉnh cấu hình.
   - Admin chỉnh được tất cả.

Nếu 1 trong 6 case fail:

- Dừng rollout cấu hình.
- Khôi phục cấu hình trước đó (nếu có snapshot).
- Ghi log nguyên nhân, người chỉnh, thời điểm chỉnh.

## Phần F - Báo cáo/đối soát cuối ngày (khuyến nghị bắt buộc)

### F1) Sales đối soát

- SO đã confirm trong ngày.
- SO chậm giao / đang backorder.
- Đơn cần follow-up khách.

### F2) Kho đối soát

- Transfer `Ready` chưa xử lý.
- Transfer `Waiting` do thiếu hàng.
- Backorder mở.

### F3) POS đối soát

- Doanh thu theo quầy.
- Chênh lệch quỹ.
- Top SKU bán ra.

### F4) Manager tổng hợp

- Danh sách PO trễ.
- Danh sách SO chậm giao.
- Tỷ lệ đơn giao đúng ngày.

## Dấu hiệu quy trình vận hành tốt

- Sales không phải đi chỉnh cấu hình kỹ thuật.
- Kho xử lý đúng thứ tự và không bỏ sót backorder.
- PO sinh đúng khi cần, không tạo dư.
- POS và SO không đè doanh thu lên nhau.
- Manager nhìn dashboard là thấy ngay đơn nào tắc, tắc ở bước nào.


