# Lab 05 — Câu hỏi thảo luận

- MSSV: 202417250
- GitHub: qminh69420

## 1. Upstream first và release first có ưu, nhược điểm gì?

Upstream first sửa trên dòng phát triển trước rồi đưa bản sửa
về các dòng release bị ảnh hưởng.

Ưu điểm:
- Dòng phát triển mới nhất có bản sửa trước.
- Giảm nguy cơ phát hành phiên bản mới vẫn chứa lỗi cũ.

Nhược điểm:
- Bản sửa có thể phụ thuộc mã mới chưa có trong release cũ.
- Backport có thể cần điều chỉnh và kiểm thử riêng.

Release first sửa từ dòng release đang bị lỗi rồi đưa bản sửa
sang master và các dòng khác.

Ưu điểm:
- Tập trung trực tiếp vào phiên bản người dùng đang sử dụng.
- Bản vá nhỏ, không kéo theo tính năng mới ngoài phạm vi.

Nhược điểm:
- Có nguy cơ quên lan truyền sang dòng phát triển hoặc release khác.
- Phải theo dõi đầy đủ các phiên bản bị ảnh hưởng.

Học phần sử dụng release first: sửa từ release/lab04 rồi
cherry-pick bản sửa sang master và release/lab05.

## 2. Nếu quên đưa fix sang release/lab05, lệnh nào phát hiện?

Vòng kiểm tra hành vi trên v1.0.1, v1.1.0 và master phát hiện
trực tiếp: tìm "lion" phải trả một kết quả ở cả ba dòng.
Nếu v1.1.0 trả 0 thì bản đó còn lỗi.

Đếm commit có trailer cherry-pick cũng giúp kiểm tra truy vết,
nhưng không thay thế kiểm thử hành vi.

git cherry -v master release/lab04 chỉ so sánh hai dòng đó,
không tự kiểm tra release/lab05. Muốn kiểm tra dòng Lab 05
cần so sánh thêm và chạy test trên chính dòng ấy.

## 3. Vì sao tách commit fix và commit nâng version?

Fix và regression test có thể áp dụng cho nhiều phiên bản.
Việc nâng version lên 1.0.1 chỉ thuộc dòng bảo trì 1.0.x.

Tách commit cho phép cherry-pick đúng mã sửa lỗi mà không
hạ version 1.1.0 của master hoặc release/lab05 xuống 1.0.1.

## 4. Tùy chọn cherry-pick -x có tác dụng gì?

Nó thêm trailer ghi SHA commit nguồn vào commit mới,
giúp truy vết bản sửa đã được lấy từ đâu.

Cherry-pick tạo commit mới; nội dung thay đổi có thể tương
đương nhưng SHA khác commit nguồn.

## 5. Vì sao tag --contains FIX_SHA không liệt kê v1.1.0?

Lệnh --contains kiểm tra quan hệ tổ tiên của commit,
không kiểm tra sự tương đương của nội dung patch.

v1.0.1 chứa commit fix gốc. v1.1.0 chứa bản cherry-pick
có SHA khác, nên không nhất thiết xuất hiện trong kết quả.

Cần kết hợp log trailer, git cherry và kiểm thử hành vi.

## 6. Vì sao chưa gắn tag v1.1.0 khi vừa cắt release/lab05?

Dòng release còn chờ nhận bản sửa và kiểm thử.
Chỉ gắn tag sau khi baseline sẵn sàng phát hành.

Nếu đã phát hành v1.1.0 rồi mới cần sửa lỗi, phải tạo
phiên bản patch mới, ví dụ v1.1.1, không di chuyển tag cũ.

## 7. Vì sao Issue được đóng qua PR vào master?

Trong bài, master là default branch.
PR đưa fix vào master dùng Fixes #N để đóng Issue khi merge.

PR hotfix vào release dùng Refs #N để tham chiếu.
Cần kiểm tra Issue Closed thực tế và vẫn kiểm toán việc
lan truyền bản sửa sang các release bị ảnh hưởng.

## 8. CI giúp kiểm soát thay đổi như thế nào?

Workflow tự chạy unit test cho PR. Required status check
khiến PR có test thất bại không được merge vào master.

Bài demo cố ý làm total_cost trả 0 để kiểm tra CI phát hiện lỗi.
PR demo phải đóng không merge; master giữ mã đúng.

CI chỉ bảo vệ những điều được kiểm tra. Test xanh không
chứng minh mọi yêu cầu đều đúng, nên vẫn cần review.

## 9. Dấu '-' và '+' trong git cherry có nghĩa gì?

Dấu '-' cho biết upstream đã có patch tương đương.
Dấu '+' cho biết chưa tìm thấy patch tương đương.

Commit fix cần có bản tương đương trên các dòng bị ảnh hưởng.
Commit bump 1.0.1 không có trên master 1.1.0 là đúng chủ đích,
không phải mọi dấu '+' đều biểu thị lỗi lan truyền.
