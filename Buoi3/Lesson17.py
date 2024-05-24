# Tỷ giá
ty_gia = {
    'USD': 25.000,
    'JPY': 162.000,
    'PHP': 437.000
}
# Nhập số tiền
so_tien = float(input("Nhập số tiền cần chuyển đổi: "))
# Menu lựa chọn loại tiền tệ
print("Chọn loại tiền tệ cần chuyển đổi:")
print("1. USD")
print("2. JPY")
print("3. PHP")
lua_chon = int(input("Nhập lựa chọn của bạn (1/2/3): "))
if lua_chon == 1:
    tu_tien = 'USD'
elif lua_chon == 2:
    tu_tien = 'JPY'
elif lua_chon == 3:
    tu_tien = 'PHP'
else:
    print("Lựa chọn không hợp lệ.")
    exit()
# Kiểm tra tỷ giá có tồn tại hay không
if tu_tien in ty_gia:
    ty_gia_hien_tai = ty_gia[tu_tien]
    so_tien_vnd = so_tien * ty_gia_hien_tai
    print(f"{so_tien} {tu_tien} = {so_tien_vnd:.2f} VND")
else:
    print("Lựa chọn tiền tệ không hợp lệ.")
