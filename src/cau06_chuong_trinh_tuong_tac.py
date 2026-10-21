# Nhập các thông tin từ bàn phím
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = int(input("Nhập số phút: "))
don_gia_kwh = float(input("Nhập đơn giá/kWh: "))

# Tính toán điện năng tiêu thụ (kWh) và chi phí (VNĐ)
dien_nang_kwh = (cong_suat_w * so_phut / 60) / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# In đầu ra theo đúng yêu cầu định dạng đề bài
print()
print(f"Mã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh}")
print(f"Chi phí: {chi_phi}")