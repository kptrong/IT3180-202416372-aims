# Trả lời câu hỏi thảo luận Lab 01

## 1. Vì sao dùng git mv?

`git mv` giúp di chuyển hoặc đổi tên tệp, đồng thời đưa thay đổi đó vào staging trong một lệnh.

Trong bài thực hành, lệnh này được dùng để chuyển `dvd.py` và `cart.py` từ thư mục gốc vào package `aims`, giúp tổ chức mã nguồn rõ ràng hơn.

Git lưu các phiên bản nội dung và nhận diện việc đổi tên dựa trên sự tương đồng giữa các tệp. Vì vậy, di chuyển tệp bằng cách thông thường rồi dùng `git add` cũng có thể được nhận diện là đổi tên. `git mv` giúp thao tác thuận tiện và giảm khả năng bỏ sót thay đổi khi staging.

Có thể dùng `git log --follow -- aims/cart.py` để theo dõi lịch sử qua việc đổi tên hoặc di chuyển tệp.

## 2. release/lab01 có phải baseline không?

Có, khi được chọn làm phiên bản đã thống nhất để nộp bài, trạng thái mã nguồn trên `release/lab01` đóng vai trò baseline của Lab 01.

Baseline là mốc tham chiếu để kiểm tra, đánh giá và so sánh các thay đổi về sau. Những sửa đổi đối với bài đã nộp cần đi qua quy trình kiểm soát thay đổi bằng nhánh riêng và Pull Request.

Nhánh release có thể được cập nhật khi có bản sửa được chấp nhận. Tag giúp định danh chính xác một commit của phiên bản đã chốt.

## 3. Vì sao không commit thẳng master dù làm một mình?

Trong kho của tôi, nhánh chính có tên là `main`, tương ứng với `master` trong tài liệu.

Làm trên nhánh riêng và đưa thay đổi qua Pull Request giúp mỗi công việc có phạm vi rõ ràng, thuận tiện kiểm tra các dòng thay đổi, mô tả mục đích và ghi lại kết quả kiểm thử trước khi tích hợp.

Quy trình này giúp bảo vệ nhánh chính, dễ truy vết hoặc hoàn tác một thay đổi và hình thành thói quen làm việc phù hợp khi tham gia nhóm.

Khi làm một mình, tôi vẫn tạo PR và tự kiểm tra trước khi merge, nhưng không yêu cầu approval từ partner.