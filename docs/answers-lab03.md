# Trả lời câu hỏi thảo luận Lab 03

## 1. Merge base là gì?

Merge base là commit tổ tiên chung tốt nhất của hai commit hoặc hai nhánh được so sánh. Trong tình huống thông thường, đó là commit chung gần nhất trước khi lịch sử hai nhánh tách ra.

Git sử dụng merge base làm mốc để xác định những thay đổi của mỗi phía khi thực hiện merge.

Trong Phần C, hai nhánh `feature/vietnamese-messages` và `feature/show-added-title` cùng sửa một dòng thông báo từ phiên bản chung ban đầu. Khi tích hợp, Git không thể tự quyết định giữ cách sửa nào nên báo xung đột. Tôi giải quyết bằng cách kết hợp hai yêu cầu: dùng tiếng Việt và hiển thị tên đĩa.

## 2. Vì sao master/release/* phải dùng revert?

Trong kho của tôi, nhánh chính có tên là `main`, tương ứng với `master` trong tài liệu.

Nhánh chính và các nhánh `release/*` chứa lịch sử đã được chia sẻ hoặc dùng làm phiên bản nộp bài. Dùng reset để loại bỏ commit rồi force push có thể làm thay đổi lịch sử chung, gây khó khăn cho người đang làm việc dựa trên lịch sử cũ và ảnh hưởng việc truy vết.

Revert tạo một commit mới để đảo ngược thay đổi, đồng thời giữ nguyên các commit trước đó. Nhờ vậy, lịch sử vẫn ghi nhận thay đổi ban đầu, lý do hoàn tác và quá trình review qua Pull Request.

Trong Phần D, tôi dùng `git revert -m 1 8364c04` để hoàn tác PR #14, rồi đưa commit revert vào `main` qua PR #15. Thông báo thêm đĩa trở lại tiếng Việt không kèm tên đĩa, trong khi lịch sử cũ vẫn được giữ lại.