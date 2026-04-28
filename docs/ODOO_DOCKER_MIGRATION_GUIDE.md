# Hướng dẫn chi tiết migrate Odoo 19 sang Docker

Tài liệu này hướng dẫn chi tiết cách chuyển hệ thống hiện tại từ mô hình:

- Odoo chạy trực tiếp trên Windows
- PostgreSQL chạy trực tiếp trên máy thật

sang mô hình:

- Odoo chạy trong Docker
- PostgreSQL chạy trong Docker
- dữ liệu được giữ đầy đủ gồm: database, filestore, code custom addons

Mục tiêu là sau khi làm xong, hệ thống trên Docker chạy giống hệ thống hiện tại nhất có thể, tránh lỗi kiểu:

- mất app/module
- mất file đính kèm
- lỗi dependency
- sai cấu hình môi trường

## 1. Các file Docker đã được tạo sẵn trong repo

Trong repo này mình đã chuẩn bị sẵn các file sau:

- `Dockerfile`
- `docker-compose.yml`
- `.env.example`
- `docker/entrypoint.sh`
- `docker/odoo.conf`

Ngoài ra, file hướng dẫn bạn đang đọc là:

- `docs/ODOO_DOCKER_MIGRATION_GUIDE.md`

## 2. Hiểu đúng trước khi migrate

Rất nhiều người nhầm rằng chỉ cần backup và restore PostgreSQL là đủ. Với Odoo, như vậy là chưa đủ.

Muốn chuyển hệ thống sang máy khác hoặc sang Docker mà vẫn chạy đúng, bạn phải chuyển đủ 3 phần:

1. Database PostgreSQL
2. Filestore của Odoo
3. Source code module custom

Nếu thiếu một trong ba phần trên thì thường sẽ gặp các lỗi sau:

- vào được hệ thống nhưng báo thiếu module
- mở chứng từ cũ bị mất file đính kèm
- view bị lỗi do thiếu custom module
- dữ liệu có nhưng chức năng không chạy đúng như máy cũ

## 3. Mô hình Docker đang được cấu hình

### 3.1. Service PostgreSQL

Trong `docker-compose.yml`, service database:

- dùng image `postgres:17`
- cổng trong container là `5432`
- cổng ngoài máy host mặc định map là `5433`

Lý do dùng `5433` thay vì `5432`: để tránh đụng với PostgreSQL đang cài sẵn trên Windows.

### 3.2. Service Odoo

Service Odoo được build từ `Dockerfile` trong repo này.

Repo hiện tại sẽ được mount vào container tại:

- `/opt/odoo`

Do đó:

- mã nguồn Odoo core nằm ở `/opt/odoo/odoo`
- addons chuẩn nằm ở `/opt/odoo/addons`
- addons custom nằm ở `/opt/odoo/addons_custom`

Filestore và dữ liệu runtime của Odoo trong container được đặt ở:

- `/var/lib/odoo/data`

### 3.3. Cấu hình Odoo trong container

File cấu hình dùng cho container là:

- `docker/odoo.conf`

Hiện tại file này đang cấu hình các giá trị chính như:

```ini
[options]
addons_path = /opt/odoo/odoo/addons,/opt/odoo/addons,/opt/odoo/addons_custom
data_dir = /var/lib/odoo/data
db_host = db
db_port = 5432
db_user = odoo
db_password = odoo
http_port = 8069
gevent_port = 8072
```

Điểm quan trọng nhất là:

- trong Docker, `db_host` phải là `db`
- không còn dùng `localhost` để kết nối PostgreSQL nữa

## 4. Điều kiện cần trước khi bắt đầu

Bạn cần chuẩn bị:

- Docker Desktop đã cài và đang chạy
- repo hiện tại đầy đủ source code
- thư mục `addons_custom` còn nguyên
- có quyền truy cập vào PostgreSQL hiện tại
- biết tên database đang dùng thật sự

Ngoài ra, nên biết sẵn các thông tin này:

- user PostgreSQL hiện tại
- password PostgreSQL hiện tại
- đường dẫn `data_dir` hiện tại của Odoo
- tên database đang vận hành

Theo cấu hình đang có trong máy của bạn:

- `data_dir = C:\Users\ADMIN\AppData\Local\OpenERP S.A.\Odoo`
- `pg_path = C:\Program Files\PostgreSQL\17\bin`

## 5. Tạo file môi trường `.env`

Đây là bước dùng để tạo ra file cấu hình môi trường riêng cho lần chạy Docker trên máy của bạn.

Hiểu đơn giản:

- `.env.example` là file mẫu
- `.env` là file cấu hình thật mà Docker Compose sẽ đọc khi chạy

Bạn không nên sửa trực tiếp `.env.example` cho từng lần dùng, vì file đó chỉ đóng vai trò làm mẫu chung. Thay vào đó, bạn copy nó thành `.env`, rồi chỉnh các giá trị trong `.env` theo nhu cầu thực tế.

### 5.1. File `.env` dùng để làm gì

File `.env` giúp bạn tách phần cấu hình ra khỏi `docker-compose.yml`.

Lợi ích:

- dễ đổi cổng mà không cần sửa file compose
- dễ đổi user/password PostgreSQL
- dễ chỉ định database muốn chạy
- cùng một bộ Docker nhưng có thể dùng cho nhiều máy khác nhau

Trong `docker-compose.yml`, các giá trị như `${POSTGRES_USER}` hay `${ODOO_HTTP_PORT}` sẽ được lấy từ file `.env`.

Nói cách khác:

- `docker-compose.yml` là khung chạy
- `.env` là nơi bạn điền thông số thực tế

### 5.2. Tại sao phải copy từ `.env.example` sang `.env`

Lệnh:

```powershell
Copy-Item .env.example .env
```

có nghĩa là:

- lấy file mẫu `.env.example`
- tạo ra file thật tên là `.env`

Sau bước này, Docker Compose sẽ đọc file `.env` khi bạn chạy:

```powershell
docker compose up -d --build
```

Nếu bạn không có file `.env`, Docker vẫn có thể dùng giá trị mặc định trong `docker-compose.yml` ở một số chỗ, nhưng sẽ khó kiểm soát hơn và dễ nhầm cấu hình.

Từ thư mục gốc của repo, chạy:

```powershell
Copy-Item .env.example .env
```

Sau đó mở file `.env` và chỉnh lại nếu cần:

```dotenv
POSTGRES_USER=odoo
POSTGRES_PASSWORD=odoo
POSTGRES_PORT=5433
ODOO_HTTP_PORT=8069
ODOO_LONGPOLLING_PORT=8072
ODOO_DATABASE=
```

### 5.3. Giải thích từng dòng trong `.env`

- `POSTGRES_USER=odoo`
  Đây là tài khoản PostgreSQL sẽ được tạo trong container database. Odoo container cũng sẽ dùng chính tài khoản này để kết nối sang PostgreSQL.

- `POSTGRES_PASSWORD=odoo`
  Đây là mật khẩu của tài khoản PostgreSQL ở trên. Giá trị này phải đồng bộ với cấu hình mà Odoo dùng để kết nối DB.

- `POSTGRES_PORT=5433`
  Đây là cổng PostgreSQL được mở ra ngoài máy host của bạn. PostgreSQL bên trong container vẫn chạy ở cổng `5432`, nhưng bên ngoài máy host sẽ truy cập qua `5433`.

- `ODOO_HTTP_PORT=8069`
  Đây là cổng web để bạn mở Odoo trên trình duyệt, ví dụ `http://localhost:8069`.

- `ODOO_LONGPOLLING_PORT=8072`
  Đây là cổng realtime/websocket của Odoo, thường dùng cho các tính năng realtime hoặc bus.

- `ODOO_DATABASE=`
  Đây là tên database mà bạn muốn Odoo tập trung làm việc với. Nếu để trống, Odoo có thể hiện danh sách DB để bạn chọn. Nếu điền tên DB, bạn đang hướng tới việc chỉ chạy một DB cụ thể.

### 5.4. Khi nào cần sửa từng biến

Bạn không phải lúc nào cũng cần sửa tất cả. Thường chỉ sửa trong các trường hợp sau:

- sửa `POSTGRES_USER` và `POSTGRES_PASSWORD` nếu bạn muốn đặt tài khoản/mật khẩu PostgreSQL khác mặc định
- sửa `POSTGRES_PORT` nếu máy bạn đã có dịch vụ khác dùng cổng `5433`
- sửa `ODOO_HTTP_PORT` nếu cổng `8069` đang bị ứng dụng khác chiếm
- sửa `ODOO_LONGPOLLING_PORT` nếu `8072` đang bị trùng
- sửa `ODOO_DATABASE` khi bạn muốn Odoo chỉ làm việc với một DB cụ thể

### 5.5. Vì sao `POSTGRES_PORT` là `5433` chứ không phải `5432`

Máy của bạn hiện đã có PostgreSQL cài trực tiếp trên Windows. Thông thường PostgreSQL ngoài máy thật đang dùng cổng:

```text
5432
```

Nếu Docker cũng map ra `5432`, rất dễ bị trùng cổng và container sẽ không chạy được.

Vì vậy trong bộ cấu hình này:

- PostgreSQL trong container vẫn chạy cổng nội bộ `5432`
- nhưng Docker map ra ngoài máy host là `5433`

Nghĩa là:

- PostgreSQL máy thật cũ: `localhost:5432`
- PostgreSQL trong Docker: `localhost:5433`

Điều này giúp bạn có thể vừa giữ hệ thống cũ, vừa thử hệ thống Docker song song.

### 5.6. `ODOO_DATABASE` để trống hay điền giá trị

Có 2 cách dùng:

#### Cách 1: để trống

```dotenv
ODOO_DATABASE=
```

Ý nghĩa:

- Odoo không bị khóa cứng vào một DB duy nhất
- bạn có thể chọn DB trong giao diện nếu `list_db = True`

Phù hợp khi:

- bạn đang thử nghiệm
- bạn có nhiều database
- bạn chưa chắc tên DB sẽ restore là gì

#### Cách 2: điền tên DB cụ thể

Ví dụ:

```dotenv
ODOO_DATABASE=demo19
```

Ý nghĩa:

- bạn muốn tập trung chạy riêng DB `demo19`
- phù hợp khi hệ thống chỉ dùng một database chính

Phù hợp khi:

- bạn đã restore xong DB thật
- muốn giảm nhầm lẫn khi có nhiều database
- muốn môi trường bàn giao rõ ràng hơn

### 5.7. Ví dụ cấu hình thực tế nên dùng

Nếu bạn đang migrate một hệ thống có DB tên `demo19`, bạn có thể dùng:

```dotenv
POSTGRES_USER=odoo
POSTGRES_PASSWORD=odoo
POSTGRES_PORT=5433
ODOO_HTTP_PORT=8069
ODOO_LONGPOLLING_PORT=8072
ODOO_DATABASE=demo19
```

Nếu bạn chỉ muốn dựng Docker trước, chưa restore DB ngay, bạn có thể tạm dùng:

```dotenv
POSTGRES_USER=odoo
POSTGRES_PASSWORD=odoo
POSTGRES_PORT=5433
ODOO_HTTP_PORT=8069
ODOO_LONGPOLLING_PORT=8072
ODOO_DATABASE=
```

### 5.8. Sau khi sửa `.env` thì làm gì tiếp

Sau khi lưu file `.env`, bạn chạy:

```powershell
docker compose up -d --build
```

Lúc đó Docker Compose sẽ đọc các giá trị trong `.env` để:

- tạo container PostgreSQL với user/password tương ứng
- map cổng PostgreSQL ra ngoài máy host
- map cổng web Odoo
- khởi động stack theo đúng cấu hình bạn vừa chọn

### 5.9. Lưu ý rất quan trọng

`POSTGRES_USER` và `POSTGRES_PASSWORD` trong `.env` phải đồng bộ với thông tin Odoo dùng để kết nối database.

Hiện tại file `docker/odoo.conf` đang để:

```ini
db_user = odoo
db_password = odoo
```

Cho nên:

- nếu `.env` là `odoo/odoo` thì không cần sửa gì thêm
- nếu bạn đổi sang user/password khác trong `.env`, bạn cũng nên sửa tương ứng trong `docker/odoo.conf`

Nếu không đồng bộ, Odoo sẽ không kết nối được PostgreSQL.

### 5.10. Khuyến nghị thực tế cho bạn

Với môi trường hiện tại của bạn, để đơn giản và ít lỗi nhất, nên bắt đầu bằng cấu hình:

```dotenv
POSTGRES_USER=odoo
POSTGRES_PASSWORD=odoo
POSTGRES_PORT=5433
ODOO_HTTP_PORT=8069
ODOO_LONGPOLLING_PORT=8072
ODOO_DATABASE=
```

Sau khi restore xong DB thật, lúc đó hãy đổi:

```dotenv
ODOO_DATABASE=ten_db_thuc_te
```

như vậy sẽ dễ thao tác hơn trong giai đoạn đầu migrate.

Khuyến nghị cho môi trường local/dev:

- giữ `POSTGRES_USER=odoo`
- giữ `POSTGRES_PASSWORD=odoo`

để dễ thao tác và đồng bộ với `docker/odoo.conf`.

## 6. Backup dữ liệu từ hệ thống hiện tại

Đây là phần quan trọng nhất. Nếu làm sai ở bước này thì lên Docker sẽ lỗi.

### 6.1. Backup database PostgreSQL hiện tại

Giả sử:

- PostgreSQL hiện tại đang chạy ngoài máy
- cổng là `5432`
- user là `odoo-user`
- password là `123`
- tên database là `demo19`

Bạn có thể dump database bằng lệnh:

```powershell
New-Item -ItemType Directory -Force -Path .\handover_out | Out-Null

$env:PGPASSWORD="123"
& "C:\Program Files\PostgreSQL\17\bin\pg_dump.exe" `
  --format=custom `
  --no-owner `
  --no-privileges `
  --host localhost `
  --port 5432 `
  --username odoo-user `
  --dbname demo19 `
  --file .\handover_out\demo19.dump
```

Giải thích:

- `--format=custom`: tạo file dump dạng `.dump`, phù hợp để restore bằng `pg_restore`
- `--no-owner`, `--no-privileges`: tránh lỗi quyền khi restore sang môi trường khác

Sau khi chạy xong, bạn phải có file:

```text
.\handover_out\demo19.dump
```

### 6.2. Backup filestore hiện tại

Filestore là nơi Odoo lưu:

- file đính kèm
- một số dữ liệu nhị phân
- tài nguyên liên quan đến attachment

Theo cấu hình hiện tại, `data_dir` là:

```text
C:\Users\ADMIN\AppData\Local\OpenERP S.A.\Odoo
```

Vậy filestore của database `demo19` sẽ nằm tại:

```text
C:\Users\ADMIN\AppData\Local\OpenERP S.A.\Odoo\filestore\demo19
```

Bạn cần copy nguyên thư mục đó sang chỗ tạm, ví dụ:

```text
.\handover_out\filestore\demo19
```

Bạn có thể dùng PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path .\handover_out\filestore | Out-Null
Copy-Item `
  "C:\Users\ADMIN\AppData\Local\OpenERP S.A.\Odoo\filestore\demo19" `
  ".\handover_out\filestore\demo19" `
  -Recurse -Force
```

### 6.3. Kiểm tra code custom addons

Các module custom hiện nằm trong:

```text
addons_custom
```

Vì `docker-compose.yml` đang mount cả repo vào container, nên nếu bạn chạy Docker ngay trong repo này thì không cần copy riêng thư mục `addons_custom` đi đâu nữa.

Tuy nhiên, nếu sau này bàn giao cho người khác bằng file nén hoặc repo riêng, thì phải đảm bảo thư mục `addons_custom` đi kèm đầy đủ.

## 7. Khởi động Docker stack

Sau khi đã có `.env`, bạn chạy:

```powershell
docker compose up -d --build
```

Lệnh này sẽ:

- build image Odoo từ `Dockerfile`
- kéo image PostgreSQL nếu máy chưa có
- tạo và chạy 2 container:
  - `odoo19-db`
  - `odoo19-app`

Sau đó kiểm tra trạng thái:

```powershell
docker compose ps
```

Nếu ổn, bạn sẽ thấy cả hai service đang chạy.

Nếu muốn xem log khi có lỗi:

```powershell
docker compose logs -f db
docker compose logs -f odoo
```

## 8. Restore database vào PostgreSQL container

Giả sử database cần migrate là `demo19`.

### 8.1. Copy file dump vào container PostgreSQL

```powershell
docker cp .\handover_out\demo19.dump odoo19-db:/tmp/demo19.dump
```

### 8.2. Tạo database mới trong container

Nếu database chưa tồn tại:

```powershell
docker exec -e PGPASSWORD=odoo odoo19-db `
  createdb -U odoo demo19
```

Nếu database đã tồn tại từ trước, nên xóa và tạo lại:

```powershell
docker exec -e PGPASSWORD=odoo odoo19-db `
  dropdb --if-exists -U odoo demo19

docker exec -e PGPASSWORD=odoo odoo19-db `
  createdb -U odoo demo19
```

### 8.3. Restore dump vào database trong container

```powershell
docker exec -e PGPASSWORD=odoo odoo19-db `
  pg_restore `
  --clean `
  --if-exists `
  --no-owner `
  --no-privileges `
  -U odoo `
  -d demo19 `
  /tmp/demo19.dump
```

Giải thích:

- `--clean`: xóa object cũ trước khi restore
- `--if-exists`: tránh lỗi khi object chưa tồn tại
- `--no-owner`, `--no-privileges`: tránh lỗi phân quyền khi restore sang môi trường mới

## 9. Copy filestore vào container Odoo

Đây là bước rất hay bị quên.

Nếu bạn restore DB xong nhưng không copy filestore, hệ thống thường sẽ:

- mất file đính kèm
- lỗi khi mở attachment
- thiếu hình ảnh/tài liệu

Trong Docker, Odoo đang dùng:

```text
/var/lib/odoo/data
```

Vì vậy filestore của database `demo19` phải nằm ở:

```text
/var/lib/odoo/data/filestore/demo19
```

### 9.1. Tạo thư mục filestore trong container

```powershell
docker exec odoo19-app mkdir -p /var/lib/odoo/data/filestore/demo19
```

### 9.2. Copy filestore từ máy host vào container

```powershell
docker cp .\handover_out\filestore\demo19\. odoo19-app:/var/lib/odoo/data/filestore/demo19
```

Sau bước này, Odoo trong container mới có đủ file để khớp với dữ liệu đã restore.

## 10. Chỉ định database cho Odoo

Nếu bạn muốn Odoo chỉ làm việc với đúng một database, hãy sửa file `.env`:

```dotenv
ODOO_DATABASE=demo19
```

Sau đó chạy lại:

```powershell
docker compose down
docker compose up -d
```

Lưu ý:

- hiện tại `docker-compose.yml` đã có biến `ODOO_DATABASE`
- nhưng `docker/odoo.conf` chưa ép cứng `db_name`
- vì vậy nếu muốn khóa chặt theo một DB duy nhất, bạn có thể bổ sung thêm `db_name = demo19` vào `docker/odoo.conf`

Nếu chưa cần khóa cứng, bạn có thể để trống và vẫn chọn database trong giao diện Odoo.

## 11. Update module sau khi restore

Sau khi DB và filestore đã được đưa vào Docker, nên chạy update module một lần để:

- đồng bộ metadata module
- cập nhật view
- kiểm tra dependency custom module

Lệnh đầy đủ:

```powershell
docker exec -it odoo19-app python odoo-bin -c docker/odoo.conf -d demo19 -u all --stop-after-init
```

Sau đó khởi động lại Odoo:

```powershell
docker compose restart odoo
```

Nếu chỉ muốn update các module custom hiện có:

```powershell
docker exec -it odoo19-app python odoo-bin -c docker/odoo.conf -d demo19 -u activity_notification,customer_vip_tier,duplicate_guard,payment_ops_qr_flow,pos_mobile_barcode_bridge,pos_zero_stock_guard,sale_promo_helper,stock_receipt_barcode_guard --stop-after-init
```

## 12. Kiểm tra sau khi migrate

Sau khi hoàn tất, bạn nên kiểm tra theo đúng thứ tự này:

1. Mở `http://localhost:8069`
2. Đăng nhập bằng tài khoản đang dùng
3. Kiểm tra danh sách app/module có báo lỗi thiếu module hay không
4. Mở thử một vài chứng từ có file đính kèm
5. In thử một báo cáo PDF
6. Kiểm tra 1-2 luồng nghiệp vụ chính như bán hàng, kho, POS
7. Kiểm tra cron/job nếu hệ thống có dùng

Nếu tất cả đều ổn thì mới xem như migrate thành công.

## 13. Các lệnh debug hữu ích

### Xem log Odoo

```powershell
docker compose logs -f odoo
```

### Xem log PostgreSQL

```powershell
docker compose logs -f db
```

### Vào shell của container Odoo

```powershell
docker exec -it odoo19-app bash
```

### Kiểm tra danh sách database trong PostgreSQL container

```powershell
docker exec -it -e PGPASSWORD=odoo odoo19-db psql -U odoo -l
```

### Kiểm tra container đang chạy hay không

```powershell
docker compose ps
```

## 14. Các lỗi thường gặp và cách xử lý

### 14.1. Odoo chạy lên nhưng mất file đính kèm

Nguyên nhân thường gặp:

- chưa copy filestore
- copy sai tên thư mục database
- copy filestore vào sai đường dẫn

Cách kiểm tra:

- vào container Odoo
- kiểm tra xem có thư mục `/var/lib/odoo/data/filestore/<TEN_DB>` hay chưa

### 14.2. Odoo báo thiếu module

Nguyên nhân thường gặp:

- thiếu thư mục `addons_custom`
- `addons_path` không đúng
- repo mount không đúng vị trí

Cách xử lý:

- kiểm tra repo có được mount vào `/opt/odoo` không
- kiểm tra `docker/odoo.conf` có dòng `/opt/odoo/addons_custom` không

### 14.3. Odoo không kết nối được PostgreSQL

Nguyên nhân thường gặp:

- `db_host` đang để `localhost`
- user/password không khớp
- container `db` chưa healthy

Cách xử lý:

- trong Docker phải dùng `db_host = db`
- đồng bộ user/password giữa `.env` và `docker/odoo.conf`
- xem log bằng `docker compose logs -f db`

### 14.4. Bị trùng cổng

Ví dụ:

- máy đã dùng `8069`
- hoặc PostgreSQL máy thật đang dùng `5432` và bạn map nhầm

Cách xử lý:

- sửa file `.env`
- ví dụ:
  - `ODOO_HTTP_PORT=8070`
  - `POSTGRES_PORT=5434`

Sau đó chạy lại:

```powershell
docker compose down
docker compose up -d
```

### 14.5. Restore DB thành công nhưng vào Odoo vẫn lỗi view hoặc lỗi custom

Nguyên nhân thường gặp:

- code custom đang không đúng phiên bản so với DB
- quên update module sau restore

Cách xử lý:

- đảm bảo code hiện tại là đúng bộ source đã dùng để tạo DB đó
- chạy lại lệnh `-u all` hoặc `-u <custom_modules>`

## 15. Khi nào nên dùng Docker, khi nào không

### Nên dùng Docker khi:

- muốn bàn giao cho người khác chạy giống hệt môi trường của bạn
- muốn giảm lỗi do thiếu dependency
- muốn dễ mang sang máy khác
- muốn chuẩn hóa môi trường cho dev/test

### Chưa nhất thiết phải dùng Docker khi:

- người nhận không quen Docker
- chỉ cần mở tạm một lần duy nhất
- team hiện tại đang vận hành ổn hoàn toàn bằng môi trường cài trực tiếp

## 16. Nếu muốn Docker hóa Odoo nhưng vẫn dùng PostgreSQL ngoài máy

Hoàn toàn làm được.

Khi đó:

- chỉ chạy Odoo trong Docker
- PostgreSQL vẫn giữ ở máy thật
- `db_host` sẽ đổi thành IP hoặc hostname của PostgreSQL ngoài máy
- có thể bỏ service `db` trong `docker-compose.yml`

Tuy nhiên, nếu mục tiêu là bàn giao gọn và chạy giống nhau ở mọi máy, thì nên Docker hóa cả PostgreSQL luôn.

## 17. Thứ tự migrate ngắn gọn, dễ nhớ

Nếu cần một checklist cực ngắn để thao tác thực tế, hãy đi theo đúng thứ tự này:

1. `Copy-Item .env.example .env`
2. sửa `.env`
3. chạy `docker compose up -d --build`
4. dump DB hiện tại ra file `.dump`
5. copy filestore hiện tại
6. `docker cp` file dump vào `odoo19-db`
7. tạo DB trong container
8. restore dump bằng `pg_restore`
9. copy filestore vào `odoo19-app`
10. chạy `python odoo-bin -u all --stop-after-init`
11. mở web và kiểm tra nghiệp vụ

## 18. Kết luận

Hướng Docker này giúp bạn:

- đóng gói môi trường rõ ràng
- giảm lỗi do lệch dependency
- dễ bàn giao cho người khác
- dễ nhân bản sang máy mới

Nhưng dù có dùng Docker hay không, nguyên tắc vẫn không đổi:

- phải có database
- phải có filestore
- phải có code custom addons

Nếu chỉ đưa mỗi database, thì lên Docker vẫn sẽ gặp lại các lỗi missing module hoặc mất attachment như trước.
