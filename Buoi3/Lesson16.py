# Nhập điểm của 3 môn
diem_van = float(input("Nhập điểm môn Văn: "))
diem_toan = float(input("Nhập điểm môn Toán: "))
diem_anh = float(input("Nhập điểm môn Anh: "))
# Tính điểm trung bình
diem_trung_binh = (diem_van + diem_toan + diem_anh) / 3
# In kết quả
print(f"Điểm trung bình của 3 môn là: {diem_trung_binh:.2f}")
