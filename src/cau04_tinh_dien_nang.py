# Cho dữ liệu ban đầu
cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# 13. Tính điện năng tiêu thụ (kWh) và chi phí (VNĐ)
# Công thức: điện năng = (Công suất (W) * thời gian (phút) / 60) / 1000
dien_nang_kwh = (cong_suat_w * so_phut / 60) / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# 14. In cả giá trị và kiểu dữ liệu của hai kết quả
print(f"Điện năng tiêu thụ: {dien_nang_kwh} kWh | Kiểu: {type(dien_nang_kwh)}")
print(f"Chi phí tiền điện: {chi_phi} VNĐ | Kiểu: {type(chi_phi)}")

# 15. Dự đoán kết quả trước khi chạy:
# - dien_nang_kwh = (250 * 90 / 60) / 1000 = (375) / 1000 = 0.375 kWh
# - chi_phi = 0.375 * 3000 = 1125.0 VNĐ

# 16. Thay so_phut bằng 60 rồi chạy lại và so sánh
so_phut = 60
dien_nang_kwh_moi = (cong_suat_w * so_phut / 60) / 1000
chi_phi_moi = dien_nang_kwh_moi * don_gia_kwh
print(f"Khi thời gian là 60 phút -> Điện năng: {dien_nang_kwh_moi} kWh, Chi phí: {chi_phi_moi} VNĐ")