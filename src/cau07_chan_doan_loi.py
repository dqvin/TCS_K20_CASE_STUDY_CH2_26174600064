# Đoạn mã đã được sửa lỗi hoàn chỉnh
ma_may = input("Nhập mã máy: ")
# Sửa Lỗi 1: Ép kiểu input() sang float cho cong_suat_w
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

# ==============================================================================
# CHẨN ĐOÁN VÀ MÔ TẢ LỖI PHÁT HIỆN DỰA TRÊN TRACEBACK (CÂU 20 - 23):
#
# Lỗi 1: TypeError tại dòng 5 trong phép tính `cong_suat_w * so_phut / 60 / 1000`
# - Loại lỗi: TypeError (can't multiply sequence by non-int of type 'float')
# - Nguyên nhân: Biến cong_suat_w nhận giá trị từ input() dưới dạng kiểu chuỗi (str).
#   Trong Python, không thể thực hiện phép nhân giữa chuỗi (str) với số thực (float).
# - Cách sửa: Sử dụng float(input(...)) để chuyển đổi kiểu dữ liệu công suất sang số thực.
# ==============================================================================