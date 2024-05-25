# Nhập số kWh tiêu thụ
so_kwh = float(input("Nhập số kWh tiêu thụ: "))
# Giả định bảng giá tiền điện
if so_kwh <= 50:
    gia_tien = so_kwh * 1806  # 1806 VND/kWh cho 50 đầu
elif so_kwh <= 100:
    gia_tien = 50 * 1806 + (so_kwh - 50) * 1866  # 1866 VND/kWh cho số kWh từ 51 đến 100
elif so_kwh <= 200:
    gia_tien = 50 * 1806 + 50 * 1866 + (so_kwh - 100) * 2167 # 2167 VND/kWh cho số kWh từ 101 đến 200
elif so_kwh <= 300:
    gia_tien = 50 * 1806 + 50 * 1866 + 100 * 2167 + (so_kwh - 200) * 2729 # 2729 VND/kWh cho số kWh từ 201 đến 300
elif so_kwh <= 400:
    gia_tien = 50 * 1806 + 50 * 1866 + 100 * 2167 + 100 * 2729 + (so_kwh - 300) * 3050  # 3050 VND/kWh cho số kWh từ 301 đến 400
else:
    gia_tien = 50 * 1806 + 50 * 1866 + 100 * 2167 + 100 * 2729 + 100 * 3050 + (so_kwh - 400) * 3151  # 3151 VND/kWh cho số kWh lớn hơn 400
# In kết quả
print(f"Số tiền điện cần thanh toán là: {gia_tien:.2f} VND")

