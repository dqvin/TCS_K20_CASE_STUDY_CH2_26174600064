# 17. Dùng input() để nhận bốn giá trị và in type() ngay sau khi nhập
ma_may_in = input("Nhập mã máy: ")
print("Kiểu dữ liệu ban đầu của mã máy:", type(ma_may_in))

cong_suat_str = input("Nhập công suất W: ")
print("Kiểu dữ liệu ban đầu của công suất:", type(cong_suat_str))

so_phut_str = input("Nhập số phút sử dụng: ")
print("Kiểu dữ liệu ban đầu của số phút:", type(so_phut_str))

don_gia_str = input("Nhập đơn giá/kWh: ")
print("Kiểu dữ liệu ban đầu của đơn giá:", type(don_gia_str))

# 18. Chuyển đổi kiểu dữ liệu tương ứng
cong_suat_w = float(cong_suat_str)
so_phut = int(so_phut_str)
don_gia_kwh = float(don_gia_str)

# 19. Tính lại điện năng và chi phí sau khi chuyển kiểu
dien_nang_kwh = (cong_suat_w * so_phut / 60) / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- KẾT QUẢ TÍNH TOÁN ---")
print(f"Mã máy: {ma_may_in}")
print(f"Điện năng tiêu thụ: {dien_nang_kwh} kWh")
print(f"Chi phí: {chi_phi} VNĐ")