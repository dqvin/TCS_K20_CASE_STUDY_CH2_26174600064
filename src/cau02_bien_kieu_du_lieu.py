# 5. Khai báo biến theo chuẩn snake_case
ma_phien = "LAB026"  # str
ma_may = "PC12"  # str
cong_suat_w = 250.0  # float
thoi_gian_phut = 90  # int
trang_thai_hoat_dong = True  # bool
ghi_chu = None  # NoneType

# 7. In giá trị và kiểm tra kiểu dữ liệu bằng type()
print("Giá trị:", ma_phien, "| Kiểu:", type(ma_phien))
print("Giá trị:", ma_may, "| Kiểu:", type(ma_may))
print("Giá trị:", cong_suat_w, "| Kiểu:", type(cong_suat_w))
print("Giá trị:", thoi_gian_phut, "| Kiểu:", type(thoi_gian_phut))
print("Giá trị:", trang_thai_hoat_dong, "| Kiểu:", type(trang_thai_hoat_dong))
print("Giá trị:", ghi_chu, "| Kiểu:", type(ghi_chu))

# 8. Thay đổi thời gian sử dụng từ 90 thành 120 bằng phép gán lại
thoi_gian_phut = 120
print("Thời gian sử dụng mới:", thoi_gian_phut, "| Kiểu:", type(thoi_gian_phut))