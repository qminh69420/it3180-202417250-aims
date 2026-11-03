# Lab 03 — Câu hỏi thảo luận

- MSSV: 202417250
- GitHub: qminh69420

## 1. Merge base là gì?

Merge base là tổ tiên chung tốt nhất của hai commit.
Git dùng nó làm cơ sở cho phép merge ba chiều:
phiên bản gốc chung, phiên bản của nhánh hiện tại và
phiên bản của nhánh được đưa vào.

Có thể tìm bằng:
git merge-base branch-a branch-b

Khi hai nhánh sửa cùng vùng nội dung so với merge base
theo cách Git không tự kết hợp được, merge sẽ có conflict.
Trong lịch sử phức tạp có thể có nhiều merge base.

## 2. Vì sao master và release/* phải dùng revert?

Đây là các nhánh dùng chung; người khác có thể đã lấy
commit về hoặc sử dụng làm baseline.

Reset hoặc rebase có thể viết lại lịch sử, khiến các bản
sao repository không còn đồng nhất.

Revert tạo commit mới đảo ngược thay đổi, giữ nguyên
commit cũ và dấu vết kiểm toán. Theo quy trình học phần,
bản revert cũng đi qua nhánh riêng và Pull Request.

Khi revert merge commit, phải xác định mainline parent.
Trong bài, git revert -m 1 44d6cdf đảo phần thay đổi PR #14
đưa vào master so với parent thứ nhất, giữ thông báo
tiếng Việt từ PR #13.

## 3. Vì sao cần test thất bại trước khi sửa?

Test thất bại trước sửa chứng minh nó tái hiện được lỗi.
Sau sửa, cùng test đó thành công giúp xác nhận bản sửa
đáp ứng hành vi mong đợi.

Giữ test làm regression test để phát hiện lỗi quay lại.
Commit test trước commit fix giúp dễ kiểm tra tiến trình.

## 4. Bugfix từ nhánh tính năng phải chọn base nào?

Bugfix giảm giá được tạo từ feature/discount và PR vào
feature/discount, không đưa trực tiếp vào master.

Sau khi feature nhận bản sửa và kiểm thử thành công,
PR feature/discount mới được merge vào master.

Cách này giữ tính năng chưa hoàn thiện ngoài nhánh chính.

## 5. Phân biệt reset soft, mixed và hard

- Soft: dời HEAD, giữ index và working tree.
  Thay đổi của commit bị bỏ vẫn được staged.
- Mixed: dời HEAD và đưa index về commit đích,
  giữ working tree. Tệp mới có thể trở thành untracked.
- Hard: đưa HEAD, index và các tệp tracked trong
  working tree về trạng thái commit đích.
  Có thể làm mất thay đổi chưa lưu.

Chỉ thực hành reset trên nhánh nháp chưa chia sẻ và
bắt đầu với working tree sạch.

## 6. Reflog dùng để làm gì?

Reflog ghi lại các lần thay đổi ref trong repository local,
giúp tìm lại commit sau reset hoặc thao tác nhầm.

Sau khi tìm đúng SHA, tạo nhánh rescue tại commit đó
để giữ lại nội dung.

Reflog không được push và không thay thế bản sao lưu;
các mục reflog và commit không còn được tham chiếu
có thể bị dọn theo thời gian.

## 7. Cách xử lý conflict trong bài

Hai nhánh sửa cùng dòng thông báo thêm DVD:
một nhánh dùng tiếng Việt, nhánh kia thêm tên DVD.

Khi merge master vào nhánh tính năng, kết hợp hai yêu cầu
thành thông báo tiếng Việt có tên DVD.

Sau đó xóa toàn bộ marker conflict, chạy test và demo,
stage tệp rồi commit hoàn tất merge.
