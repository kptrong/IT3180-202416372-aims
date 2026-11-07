# Changelog

## [Unreleased]

## [1.0.0] - 2026-11-07

### Added

- Thêm `Cart.print_cart()` để hiển thị tổng tiền và xử lý giỏ hàng trống.
- Thêm `search_by_title()` để tìm DVD theo tiêu đề.
- Thêm `Cart.total_cost_with_discount()` để tính số tiền sau giảm giá.
- Bổ sung kiểm thử tự động bằng `unittest` cho giỏ hàng và chức năng giảm giá.

### Fixed

- Sửa lỗi giỏ hàng vẫn nhận đĩa thứ 21 dù giới hạn là 20 đĩa.
- Sửa công thức giảm giá để trả về số tiền còn phải trả.
- Từ chối phần trăm giảm giá ngoài khoảng 0–100 bằng `ValueError`.