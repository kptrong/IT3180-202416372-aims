# Trả lời câu hỏi thảo luận Lab 04

## 1. Vì sao release/* không merge vào master?

Trong kho của tôi, nhánh chính là `main`, tương ứng với `master` trong tài liệu.

Theo Release Flow của học phần, `main` là nơi tích hợp các thay đổi để tiếp tục phát triển; `release/*` lưu giữ và bảo trì một phiên bản đã phát hành hoặc đã nộp.

Không merge toàn bộ nhánh release ngược vào `main` để tránh đưa các thay đổi riêng của dòng phát hành, chẳng hạn số phiên bản, vào dòng phát triển mới. Khi cần lan truyền bản sửa lỗi, lựa chọn đúng commit sửa lỗi và đưa qua nhánh riêng cùng Pull Request.

Đây là quy tắc của mô hình trong học phần, không phải hạn chế kỹ thuật của Git.

## 2. So sánh với GitFlow

| Nội dung | Release Flow của học phần | GitFlow |
|---|---|---|
| Nhánh tích hợp phát triển | `master` hoặc `main` | `develop` |
| Nhánh release tạo từ | `master` hoặc `main` | `develop` |
| Khi phát hành | Giữ nhánh release và đánh dấu bằng tag | Merge nhánh release vào `master`, tạo tag và merge lại vào `develop` |
| Vòng đời nhánh release | Giữ để nộp bài và bảo trì phiên bản | Thường xóa sau khi hoàn tất phát hành |

Vì vậy, quy tắc không merge `release/*` về nhánh chính trong học phần không áp dụng nguyên trạng cho GitFlow.

Tham khảo: [Mô hình GitFlow của Vincent Driessen](https://nvie.com/posts/a-successful-git-branching-model/).

## 3. Vì sao phát hành 1.0.0 thay vì 0.4.0?

Theo Semantic Versioning, các phiên bản `0.y.z` dành cho giai đoạn phát triển ban đầu, khi giao diện công khai chưa được coi là ổn định. Phiên bản `1.0.0` đánh dấu việc xác định giao diện công khai và bắt đầu quản lý tính tương thích theo giao diện đó.

Trong bài thực hành, `1.0.0` được chọn làm mốc phát hành ổn định đầu tiên, có kiểm thử, CHANGELOG, tag và GitHub Release. Nếu dự án vẫn đang thử nghiệm và chưa cam kết tính ổn định, `0.4.0` vẫn có thể phù hợp.

Việc lên `1.0.0` là quyết định về mức độ ổn định và cam kết tương thích, không tự động xảy ra chỉ vì đây là Lab 04.

Tham khảo: [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).