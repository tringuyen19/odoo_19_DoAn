# Hướng dẫn bàn giao và sử dụng Odoo Docker

Tài liệu này dành cho 2 vai trò:

- **Bên giao**: người chuẩn bị và gửi hệ thống.
- **Bên nhận**: người nhận và chạy hệ thống.

Mục tiêu: bên nhận có thể chạy Odoo giống môi trường của bên giao, không bị lỗi thiếu module hoặc mất file đính kèm.

---

## 1) Bạn cần gửi cho bên nhận những gì

Không chỉ gửi mỗi database. Phải gửi đủ 3 nhóm dữ liệu:

1. **Code + cấu hình Docker** (qua GitHub)
2. **Database dump** (`odoo-db.dump`) (qua Drive/OneDrive/NAS)
3. **Filestore** (`filestore/odoo-db/`) (qua Drive/OneDrive/NAS)

---

## 2) Cái gì đẩy lên GitHub, cái gì không

### 2.1 Đẩy lên GitHub

- `Dockerfile`
- `docker-compose.yml`
- `docker/odoo.conf`
- `.env.example`
- `addons_custom/`
- `docs/ODOO_DOCKER_MIGRATION_GUIDE.md`
- `docs/HUONG_DAN_BAN_GIAO_VA_SU_DUNG_ODOO_DOCKER.md`

### 2.2 Không đẩy lên GitHub

- `.env` (chứa cấu hình máy thật)
- `handover_out/`
- file dump `.dump`
- thư mục filestore
- thông tin nhạy cảm (mật khẩu thật, key, token)

---

## 3) Bên giao đóng gói và gửi như thế nào

Giả sử DB cần bàn giao là `odoo-db`.

### Bước 1: Tạo thư mục dữ liệu bàn giao

```powershell
cd E:\ODOO\odoo-19.0
New-Item -ItemType Directory -Force -Path .\handover_out | Out-Null
New-Item -ItemType Directory -Force -Path .\handover_out\filestore | Out-Null
```

### Bước 2: Dump database PostgreSQL local

```powershell
$env:PGPASSWORD="123"
& "C:\Program Files\PostgreSQL\17\bin\pg_dump.exe" `
  --format=custom `
  --no-owner `
  --no-privileges `
  --host localhost `
  --port 5432 `
  --username odoo-user `
  --dbname odoo-db `
  --file .\handover_out\odoo-db.dump
```

### Bước 3: Copy filestore

```powershell
Copy-Item `
  "C:\Users\ADMIN\AppData\Local\OpenERP S.A.\Odoo\filestore\odoo-db" `
  ".\handover_out\filestore\odoo-db" `
  -Recurse -Force
```

### Bước 4: Gửi dữ liệu cho bên nhận

- Gửi link GitHub repo (code + docker config)
- Gửi file/thư mục sau qua Drive/OneDrive/NAS:
  - `handover_out/odoo-db.dump`
  - `handover_out/filestore/odoo-db/`

---

## 4) Bên nhận setup lần đầu

## 4.1 Yêu cầu

- Đã cài Docker Desktop
- Docker Engine đang chạy

### 4.2 Clone code và tạo `.env`

```powershell
git clone <REPO_URL>
cd <TEN_THU_MUC_REPO>
Copy-Item .env.example .env
```

Mở `.env` và điền giá trị phù hợp, ví dụ:

```dotenv
POSTGRES_USER=odoo
POSTGRES_PASSWORD=odoo
POSTGRES_PORT=5433
ODOO_HTTP_PORT=8069
ODOO_LONGPOLLING_PORT=8072
ODOO_DATABASE=odoo-db
```

### 4.3 Chạy container

```powershell
docker compose up -d --build
docker compose ps
```

Kỳ vọng:

- `odoo19-db` -> `Up (healthy)`
- `odoo19-app` -> `Up`

---

## 5) Bên nhận restore dữ liệu bàn giao

Giả sử bên nhận đã đặt dữ liệu vào `.\handover_out` trong repo.

### 5.1 Restore database

```powershell
docker cp .\handover_out\odoo-db.dump odoo19-db:/tmp/odoo-db.dump
docker exec -e PGPASSWORD=odoo odoo19-db dropdb --if-exists -U odoo odoo-db
docker exec -e PGPASSWORD=odoo odoo19-db createdb -U odoo odoo-db
docker exec -e PGPASSWORD=odoo odoo19-db pg_restore --clean --if-exists --no-owner --no-privileges -U odoo -d odoo-db /tmp/odoo-db.dump
```

### 5.2 Restore filestore

```powershell
docker exec odoo19-app mkdir -p /var/lib/odoo/data/filestore/odoo-db
docker cp .\handover_out\filestore\odoo-db\. odoo19-app:/var/lib/odoo/data/filestore/odoo-db
```

### 5.3 Update module sau restore

```powershell
docker exec -it odoo19-app python odoo-bin -c docker/odoo.conf -d odoo-db -u all --stop-after-init
docker compose restart odoo
```

---

## 6) Cách sử dụng hằng ngày (bên nhận)

### Mở hệ thống

```powershell
cd <TEN_THU_MUC_REPO>
docker compose up -d
```

Mở trình duyệt:

- `http://localhost:8069`

### Kiểm tra nhanh trạng thái

```powershell
docker compose ps
```

### Xem log khi cần

```powershell
docker compose logs --tail=100 odoo
docker compose logs --tail=100 db
```

### Tắt hệ thống

```powershell
docker compose stop
```

Hoặc tắt và dỡ network/container:

```powershell
docker compose down
```

---

## 7) Kiểm tra sau bàn giao

Bên nhận nên test tối thiểu:

- đăng nhập được
- vào được các app chính
- mở được chứng từ có đính kèm
- in được report PDF
- thao tác được các module custom

---

## 8) Lỗi thường gặp

- **Thiếu module**: chưa có đủ `addons_custom` hoặc sai `addons_path`
- **Mất file đính kèm**: chưa copy đúng filestore
- **Không kết nối DB**: sai user/password trong `.env` hoặc chưa chạy container DB
- **Không vào được từ máy khác**: chưa mở firewall port `8069`

---

## 9) Ghi chú quan trọng

- `pgAdmin 4` vẫn dùng bình thường để quản trị DB trong Docker.
- Khác biệt là host/port:
  - PostgreSQL local cũ thường là `localhost:5432`
  - PostgreSQL Docker trong bộ này là `localhost:5433`

