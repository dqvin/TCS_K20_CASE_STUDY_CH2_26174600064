from datetime import datetime  #[cite: 5]

# Lấy thời điểm hiện tại và định dạng chuỗi
thoi_diem = datetime.now()  #[cite: 5]
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")  #[cite: 5]

print(thoi_diem)  #[cite: 5]
print(type(thoi_diem))  #[cite: 5]
print(thoi_diem_text)  #[cite: 5]
print(type(thoi_diem_text))  #[cite: 5]

print("-" * 40)

# Bổ sung tính toán khoảng thời gian (Timedelta)
bat_dau = datetime(2026, 10, 14, 13, 15)  #[cite: 5]
ket_thuc = datetime(2026, 10, 14, 15, 5)  #[cite: 5]
thoi_luong = ket_thuc - bat_dau  #[cite: 5]

print(thoi_luong)  #[cite: 5]
print(type(thoi_luong))  #[cite: 5]