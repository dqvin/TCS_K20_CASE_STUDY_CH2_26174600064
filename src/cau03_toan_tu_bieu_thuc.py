# Cho các biến ban đầu theo đề bài
tong_phut = 135
cong_suat_w = 250

# 9. Dùng // và % để tính số giờ tròn vẹn và số phút còn lại
so_gio = tong_phut // 60
so_phut_du = tong_phut % 60

print(f"Tổng số phút: {tong_phut}")
print(f"Số giờ tròn vẹn: {so_gio} giờ")
print(f"Số phút còn lại: {so_phut_du} phút")
print("-" * 40)

# 10. Tạo biến su_dung_lau nhận True khi tong_phut > 60
su_dung_lau = tong_phut > 60
print(f"Kết quả kiểm tra su_dung_lau (tong_phut > 60): {su_dung_lau}")
print("-" * 40)

# 11. Tạo biến du_lieu_hop_le nhận True khi cong_suat_w > 0 và tong_phut > 0
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print(f"Kết quả kiểm tra du_lieu_hop_le (cong_suat_w > 0 và tong_phut > 0): {du_lieu_hop_le}")
print("-" * 40)

# 12. Dự đoán và kiểm chứng hai biểu thức: 100 + 20 * 3 và (100 + 20) * 3
# Dự đoán trước khi chạy:
# - Biểu thức 1 (100 + 20 * 3): Phép nhân (*) có độ ưu tiên cao hơn phép cộng (+) -> 100 + 60 = 160
# - Biểu thức 2 ((100 + 20) * 3): Cặp dấu ngoặc () có độ ưu tiên cao nhất -> (120) * 3 = 360

kq1 = 100 + 20 * 3
kq2 = (100 + 20) * 3

print(f"Thực thi biểu thức 100 + 20 * 3  : {kq1}")
print(f"Thực thi biểu thức (100 + 20) * 3: {kq2}")