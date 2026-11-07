# Trả lời câu hỏi thảo luận Lab 05

## 1. Ưu, nhược điểm của upstream first so với release first?

### Upstream first

Bản sửa được tích hợp vào nhánh phát triển chính trước, sau đó đưa về các nhánh release cần sửa.

Ưu điểm:
- Bản sửa có mặt trong dòng phát triển mới nhất trước, giảm nguy cơ lỗi xuất hiện lại trong phiên bản tương lai.
- Có thể kiểm tra việc tích hợp với mã nguồn hiện tại trước khi đưa về các phiên bản cũ.

Nhược điểm:
- Mã trên nhánh chính có thể khác nhiều so với bản cũ, khiến việc đưa bản sửa về release cần điều chỉnh hoặc giải quyết xung đột.
- Cần xác định và kiểm tra riêng từng dòng phiên bản bị ảnh hưởng.

### Release first

Bản sửa được thực hiện trên nhánh release gặp lỗi trước, sau đó lan truyền sang nhánh chính và các release khác. Đây là cách áp dụng trong bài thực hành.

Ưu điểm:
- Sửa và kiểm thử trực tiếp trên dòng phiên bản đang gặp lỗi.
- Bản vá có phạm vi nhỏ, tránh kéo theo các tính năng mới của nhánh chính.

Nhược điểm:
- Có nguy cơ quên đưa bản sửa sang nhánh chính hoặc release khác.
- Cần truy vết và kiểm thử việc lan truyền bản sửa trên nhiều dòng phiên bản.

## 2. Nếu quên đưa bản sửa sang release/lab05, lệnh nào ở Phần F sẽ phát hiện?

Kiểm tra hành vi tìm kiếm trên các mốc `v1.0.1`, `v1.1.0` và `main` là cách xác nhận trực tiếp.

Khi tìm từ khóa `lion` trong danh sách có `The Lion King`, mỗi phiên bản đã sửa phải trả về một kết quả. Nếu bản `v1.1.0` vẫn trả về 0 trong khi hai mốc còn lại trả về 1, bản sửa chưa có trong phiên bản đó.

Lệnh tìm thông điệp `cherry picked from commit ...` hỗ trợ truy vết hai lần lan truyền, nhưng cần kiểm tra thêm commit có thực sự nằm trong nhánh hoặc tag cần kiểm toán.

Không dùng riêng `git tag --contains <FIX_SHA>` để kết luận bản sửa đã có trong `v1.1.0`, vì cherry-pick tạo commit có SHA khác.

## 3. Kết quả kiểm toán trong bài của tôi

- Issue ghi nhận lỗi: #25.
- Commit sửa lỗi gốc: `935f1e03401ae2e3e32c2d98f0a1898528bd9147`.
- Bản cherry-pick vào `main`: `3d9f559`.
- Bản cherry-pick vào `release/lab05`: `288426c`.
- Tìm `lion` trên `v1.0.1`, `v1.1.0` và `main` đều trả về một kết quả.
- Dòng `1.0.x` dùng phiên bản `1.0.1`; nhánh chính và Lab 05 giữ phiên bản `1.1.0`.

Trong kho này, `git cherry` vẫn đánh dấu `+` cho bản sửa vì diff sau khi xử lý xung đột không được Git nhận là tương đương với diff gốc. Tôi đối chiếu thêm mã nguồn, dấu vết cherry-pick và hành vi chương trình để xác nhận bản sửa đã được lan truyền.