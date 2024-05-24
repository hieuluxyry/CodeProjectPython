# Tính diện tích hình chữ nhật, hình vuông, hình bình hành và hình thang cân.
# Nhập các giá trị từ người dùng
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
h = int(input("Nhập chiều cao h: "))

# Tính diện tích các hình
S_hcn = a * b  # Diện tích hình chữ nhật
S_hv = a * a   # Diện tích hình vuông
S_hbh = a * h  # Diện tích hình bình hành
S_htc = 1/2 * (a + b) * h  # Diện tích hình thang cân

# In kết quả
print(f"Diện tích hình chữ nhật là: {S_hcn}")
print(f"Diện tích hình vuông là: {S_hv}")
print(f"Diện tích hình bình hành là: {S_hbh}")
print(f"Diện tích hình thang cân là: {S_htc}")

