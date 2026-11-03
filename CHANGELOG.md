# Changelog

Ghi nhận thay đổi đáng chú ý của AIMS-mini.
Số phiên bản tuân theo Semantic Versioning.

## [Unreleased]
## [1.0.1] - 2026-11-03

### Fixed
- Tìm DVD theo tên không phân biệt hoa thường.
- Thêm regression test cho tìm kiếm theo tên.
## [1.0.0] - 2026-11-03

### Added
- Package aims chứa các lớp DigitalVideoDisc và Cart.
- Thêm và xóa DVD khỏi giỏ hàng.
- In danh sách DVD, xử lý giỏ rỗng và tính tổng tiền.
- Tìm DVD theo chuỗi con trong tiêu đề.
- Tính số tiền sau giảm giá với phần trăm từ 0 đến 100.
- Tài liệu use case, PR template và đáp án Lab 01–03.

### Fixed
- Từ chối thêm DVD thứ 21 khi giỏ đã đủ 20 đĩa.
- Sửa công thức tính tiền sau giảm giá.
- Từ chối phần trăm giảm giá ngoài khoảng 0–100.

### Changed
- Thông báo thêm DVD thành công bằng tiếng Việt.
- Đã hoàn tác phần hiển thị tên DVD trong thông báo thêm đĩa.

### Tests
- Bốn unit test kiểm tra giới hạn giỏ, tổng tiền,
  giảm giá và phần trăm không hợp lệ.

### Known issues
- Tìm kiếm theo tên còn phân biệt hoa thường.
  Lỗi này sẽ được xử lý trong bài thực hành hotfix.
