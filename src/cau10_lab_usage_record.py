from datetime import datetime

# 1. Nhập các thông tin từ bàn phím và chuyển đổi kiểu dữ liệu
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất thiết bị (W): "))
so_phut = int(input("Nhập thời gian sử dụng (phút): "))
don_gia_kwh = float(input("Nhập đơn giá điện (VNĐ/kWh): "))

# 2. Thực hiện tính toán và xử lý logic (không dùng if)
dien_nang_kwh = (cong_suat_w * so_phut / 60) / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
tren_60_phut = so_phut > 60

# 3. Lấy thời điểm hiện tại và định dạng chuỗi thời gian
thoi_diem_ghi_nhan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 4. Xuất kết quả ra màn hình theo đúng định dạng mẫu yêu cầu
print()
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {so_phut} phút")
print(f"Điện năng: {dien_nang_kwh} kWh")
print(f"Chi phí: {chi_phi:.2f} VNĐ")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {thoi_diem_ghi_nhan}")