# Lab 01 — Câu hỏi thảo luận

- MSSV: 202417250
- GitHub: qminh69420

## 1. Cấu hình --global lưu ở đâu? Khác gì --local?

Cấu hình --global thường được lưu tại ~/.gitconfig và áp dụng
cho các repository của người dùng hiện tại.

Cấu hình --local được lưu tại .git/config và chỉ áp dụng cho
repository hiện tại. Nếu cùng một khóa có ở cả hai phạm vi,
giá trị local được ưu tiên.

Lệnh kiểm tra giá trị và nguồn cấu hình:
git config --list --show-origin

## 2. Vì sao dùng git mv?

git mv vừa di chuyển hoặc đổi tên tệp, vừa stage thay đổi,
giúp tránh quên ghi nhận đường dẫn cũ bị xóa và đường dẫn mới.

Git nhận diện việc đổi tên dựa trên độ tương đồng nội dung,
không lưu riêng một thao tác rename. Di chuyển tệp bằng cách
khác rồi chạy git add -A cũng có thể cho kết quả tương đương.

Tách commit di chuyển tệp khỏi commit sửa nội dung giúp việc
review và truy vết dễ hơn.

Lệnh theo dõi lịch sử tệp qua việc đổi tên:
git log --oneline --follow -- aims/cart.py

## 3. release/lab01 có phải baseline không?

Có, khi nhánh này xác định trạng thái đã thống nhất dùng để
nộp bài và đối chiếu kết quả Lab 01.

Tuy nhiên, nhánh có thể tiến khi nhận commit mới. Vì vậy,
baseline cần được bảo vệ bằng quy trình kiểm soát thay đổi.
Tag có thể dùng để đánh dấu chính xác một phiên bản.

Khi vừa tạo release/lab01 từ master, hai nhánh cùng trỏ đến
một commit. Sau khi master tiếp tục phát triển, hai nhánh
có thể khác nhau; đó là hành vi bình thường.

## 4. Vì sao không commit thẳng master dù làm một mình?

Nhánh riêng và Pull Request tạo cơ hội kiểm tra diff, chạy
chương trình và ghi lại mục đích thay đổi trước khi tích hợp.

Quy trình này giúp giữ master ổn định, dễ truy vết và chuẩn bị
cho làm việc nhóm. Theo đề, khi làm một mình có thể đặt số
approval bắt buộc bằng 0, nhưng vẫn phải đi qua PR.

Các commit khởi tạo ở phần A/B là bước thiết lập ban đầu,
trước khi áp dụng bảo vệ nhánh.

## 5. Phân biệt các thao tác hoàn tác đã thực hành

- git restore file: bỏ thay đổi chưa stage của tệp tracked,
  khôi phục working tree theo nội dung staging area.
- git restore --staged file: bỏ thay đổi khỏi staging area,
  nhưng giữ nội dung sửa trong working tree.
- git commit --amend: thay thế commit cuối bằng commit mới;
  trong bài này chỉ thực hiện khi commit chưa được push.
- Với commit đã chia sẻ, dùng git revert để đảo thay đổi
  mà vẫn giữ lịch sử.
