# Lab 02 — Câu hỏi thảo luận

- MSSV: 202417250
- GitHub: qminh69420

## 1. Vì sao phải đồng bộ master trước khi gửi PR?

Nhánh tính năng có thể được tạo từ một phiên bản master cũ.
Trong lúc phát triển, master có thể đã nhận thay đổi từ các
nhánh khác.

Đồng bộ giúp phát hiện và giải quyết xung đột, đồng thời kiểm
tra tính năng có hoạt động cùng mã mới nhất hay không.

Quy trình:
- git fetch origin để cập nhật thông tin remote.
- git merge origin/master trên nhánh tính năng.
- Giải quyết xung đột nếu có, chạy kiểm tra rồi push.

Không có xung đột văn bản chưa chắc chương trình đúng:
hai thay đổi vẫn có thể gây lỗi hành vi khi kết hợp.

## 2. Khi nào không được rebase?

Theo quy tắc học phần, không rebase các commit đã chia sẻ
mà người khác có thể đang sử dụng, đặc biệt trên master
và release/*.

Rebase phát lại các thay đổi trên base mới, có thể tạo SHA
mới và làm lệch lịch sử với bản sao của người khác.

Chỉ thực hành rebase trên phần lịch sử riêng chưa chia sẻ.
Với nhánh chung, dùng merge để đồng bộ và revert để hoàn tác.

Rebase and merge trên GitHub là cách tích hợp PR; không có
nghĩa được phép tự rebase rồi force push lịch sử master.

## 3. feature/* khác topic/* ra sao?

feature/* dùng cho chức năng của chương trình, ví dụ:
- feature/cart-print
- feature/search-by-title

topic/* dùng cho công việc theo chủ đề, ví dụ:
- topic/pr-template
- topic/use-case-diagram
- topic/answers-lab02

Đây là quy ước đặt tên, không phải hai loại nhánh khác nhau
về kỹ thuật Git. Cả hai tạo từ master, được tích hợp qua PR,
sau đó xóa khi hoàn thành.

## 4. So sánh ba kiểu merge

### Merge commit

Giữ các commit của nhánh và tạo thêm merge commit.
Lịch sử thể hiện rõ việc phân nhánh và tích hợp.
Có thể hoàn tác phần thay đổi của merge bằng git revert
với tùy chọn -m sau khi xác định đúng mainline parent.

### Squash and merge

Gộp thay đổi của PR thành một commit mới trên nhánh đích.
Lịch sử gọn, dễ hoàn tác toàn bộ thay đổi bằng một revert.
Các commit gốc của nhánh không được giữ làm tổ tiên qua
thao tác squash.

### Rebase and merge

Phát lại các commit của PR trên nhánh đích để lịch sử
tuyến tính, không tạo merge commit.
Giữ các thay đổi theo từng commit nhưng SHA có thể đổi.
PR có nhiều commit có thể cần nhiều revert để hoàn tác.

## 5. Vì sao bật Dismiss stale approvals?

Khi tác giả push thêm thay đổi, nội dung PR không còn giống
bản đã được reviewer duyệt.

Hủy approval cũ buộc reviewer kiểm tra phiên bản mới,
đảm bảo nội dung được duyệt là nội dung được tích hợp.

## 6. Vì sao branch -d có thể thất bại sau squash/rebase?

Git kiểm tra quan hệ tổ tiên của commit để xác định nhánh
đã được merge hay chưa.

Sau squash hoặc rebase, master có thể chứa thay đổi tương
đương nhưng không chứa các commit gốc của nhánh.

Chỉ dùng git branch -D sau khi đã xác nhận PR Merged và
kiểm tra nội dung cần giữ đã có trên master.
