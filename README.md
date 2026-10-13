# Bài 2: Đóng gói ứng dụng Web Backend bằng Single-stage Dockerfile

## Giới thiệu
Dự án đóng gói ứng dụng REST API Node.js/Express thành Docker Image bằng Single-stage Dockerfile chuẩn hóa phục vụ việc triển khai kiểm thử.

## Các thành phần
- `Dockerfile`: Single-stage Dockerfile với base image `node:18-alpine`, đầy đủ các chỉ thị `FROM`, `WORKDIR`, `COPY`, `RUN`, `ENV`, `EXPOSE`, `CMD`.
- `server.js`: Mã nguồn REST API Node.js/Express lắng nghe theo cổng được cấu hình qua biến môi trường `PORT`.
- `package.json`: Khai báo thông tin dự án và dependencies.
- `main.py`: Script Python kiểm tra tự động mã phản hồi HTTP và JSON response từ server.

## Hướng dẫn thực hiện

### 1. Build Docker Image
```bash
docker build -t hw-backend:v1 .
```

### 2. Khởi chạy Container
```bash
docker run -d --name app-single-stage -p 8080:3000 hw-backend:v1
```

### 3. Kiểm tra container hoạt động
```bash
docker ps
docker logs app-single-stage
```

### 4. Kiểm tra API Endpoint
Sử dụng cURL:
```bash
curl -i http://localhost:8080/
```
Hoặc sử dụng script Python kiểm tra:
```bash
python main.py http://localhost:8080/
```

### Kết quả mong đợi
- HTTP status: `200 OK`
- Response JSON: `{"status":"success","message":"Hello from Docker Single-stage!"}`