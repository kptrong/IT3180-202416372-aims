# Trả lời câu hỏi thảo luận Lab 02

## 1. Vì sao phải đồng bộ master trước khi tạo Pull Request?

Trong kho của tôi, nhánh chính có tên là `main`, tương ứng với `master` trong tài liệu.

Trong lúc phát triển trên nhánh riêng, nhánh chính có thể đã nhận thêm thay đổi từ các PR khác. Đồng bộ giúp kiểm tra tính năng trên mã nguồn mới nhất, phát hiện và giải quyết xung đột sớm, đồng thời giảm nguy cơ lỗi khi tích hợp.

Ví dụ: nhánh `feature/search-by-title` được tạo khi nhánh chính chưa có `print_cart()`. Sau khi tính năng in giỏ hàng được merge, nhánh tìm kiếm cần lấy cập nhật đó và chạy lại chương trình trước khi gửi PR.

## 2. Khi nào không được rebase?

Không rebase các commit đã được chia sẻ và đang được người khác sử dụng làm nền cho công việc, đặc biệt trên các nhánh chung như `main` và `release/*`.

Rebase viết lại lịch sử và tạo mã SHA mới cho các commit. Nếu người khác vẫn làm việc dựa trên lịch sử cũ, việc đồng bộ có thể trở nên khó khăn, phát sinh xung đột hoặc trùng lặp thay đổi.

Theo quy tắc của bài, chỉ viết lại lịch sử đối với commit chưa chia sẻ. Với lịch sử chung, dùng merge để tích hợp và revert để hoàn tác thay đổi.

## 3. feature/* khác topic/* như thế nào?

`feature/*` thể hiện mục đích phát triển một tính năng của ứng dụng. Ví dụ:

- `feature/cart-print`: thêm chức năng in giỏ hàng.
- `feature/search-by-title`: thêm chức năng tìm kiếm theo tiêu đề.

`topic/*` thể hiện một chủ đề công việc cụ thể. Trong bài thực hành, các nhánh này được dùng cho tài liệu hoặc cấu hình quy trình. Ví dụ:

- `topic/pr-template`: thêm mẫu mô tả Pull Request.
- `topic/use-case-diagram`: bổ sung tài liệu use case.

Đây là quy ước đặt tên và tổ chức công việc, không phải hai loại nhánh có cơ chế khác nhau trong Git. Cả hai đều nên có một mục đích rõ ràng, tồn tại ngắn hạn và được tích hợp vào nhánh chính qua Pull Request.