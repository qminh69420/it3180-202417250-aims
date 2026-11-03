# Lab 04 — Câu hỏi thảo luận

- MSSV: 202417250
- GitHub: qminh69420

## 1. Vì sao release/* không merge ngược vào master?

Theo Release Flow của học phần, master là dòng phát triển,
còn release/* giữ baseline nộp bài và phục vụ bảo trì.

Merge toàn bộ release về master có thể mang theo thay đổi
chỉ dành cho bản cũ, chẳng hạn số phiên bản hoặc cấu hình
phát hành không phù hợp với dòng phát triển mới.

Khi cần lan truyền bản sửa lỗi, tách commit sửa lỗi khỏi
commit nâng phiên bản và đưa đúng bản sửa sang các dòng
liên quan bằng cherry-pick -x.

Đây là quy tắc của mô hình được dùng trong học phần,
không phải giới hạn kỹ thuật của Git.

## 2. So sánh với GitFlow

GitFlow thường có main giữ lịch sử phát hành và develop
làm dòng tích hợp phát triển. Khi hoàn tất release,
thay đổi được tích hợp vào main và develop.
Hotfix cũng được đưa vào các dòng liên quan.

Trong Release Flow của học phần, master là dòng tích hợp;
release/labXX là các dòng nộp bài được giữ song song.
Không merge ngược toàn bộ release vào master.

Vì vậy, không áp dụng máy móc quy tắc merge của GitFlow
cho quy trình release trong bài này.

## 3. Vì sao lên 1.0.0 thay vì 0.4.0?

Phiên bản 0.y.z biểu thị giai đoạn phát triển ban đầu,
chưa cam kết API công khai ổn định.

Chọn 1.0.0 khi nhóm xác nhận baseline đầu tiên đủ ổn định
và sẵn sàng cam kết hành vi/API công khai.

Không phải cứ đến Lab 04 thì bắt buộc tăng thành 1.0.0.
Nếu chưa sẵn sàng cam kết ổn định, 0.4.0 vẫn có thể phù hợp.
Trong bài thực hành, 1.0.0 được chọn làm baseline ổn định.

Sau 1.0.0:
- PATCH: sửa lỗi tương thích.
- MINOR: thêm chức năng tương thích.
- MAJOR: thay đổi phá vỡ tương thích.

## 4. Vì sao chuẩn bị phát hành trên master trước?

Version, CHANGELOG và các kiểm thử cần được review,
tích hợp và xác nhận trước khi cắt nhánh release.

Như vậy release được tạo từ trạng thái đã kiểm tra.
Sửa trực tiếp trên release sau khi cắt dễ tạo khác biệt
khó truy vết và vi phạm chính sách thay đổi qua PR.

Sau khi phát hành, sửa lỗi trên dòng release phải đi qua
quy trình hotfix.

## 5. Tag khác nhánh release thế nào?

Tag đánh dấu một phiên bản cụ thể. Annotated tag có thêm
thông tin người tạo, thời điểm và thông điệp.

Nhánh release là con trỏ có thể tiến khi nhận hotfix.
Không xóa hoặc di chuyển tag đã công bố.

Ở cuối Lab 04, v1.0.0 trỏ cùng commit với release/lab04.
Sau hotfix Lab 05, nhánh có thể tiến tới v1.0.1,
nhưng tag v1.0.0 vẫn giữ baseline ban đầu.

## 6. Ý nghĩa A..B là gì?

git log A..B liệt kê các commit có thể truy cập từ B
nhưng không thể truy cập từ A.

Đây là phép so sánh tập commit, không phải diff nội dung.
git diff A B mới dùng để so sánh cây tệp ở hai đầu.

## 7. Worktree và git archive giúp kiểm toán ra sao?

Worktree mở một phiên bản khác trong thư mục riêng,
cho phép kiểm thử baseline mà không đổi nhánh đang làm
trong thư mục repository chính.

git archive xuất các tệp được Git theo dõi tại ref đã chọn,
giúp đóng gói đúng mã nguồn của tag, không lấy nhầm
thay đổi đang phát triển trên master.

Cần đối chiếu version, CHANGELOG, kết quả test và cây tệp
để xác nhận nội dung bản phát hành.
