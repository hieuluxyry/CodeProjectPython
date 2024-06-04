# Nhập hai số a và b từ bàn phím
a = float(input("Enter Number a : "))
b = float(input("Enter Number b : "))
tong = a + b
hieu = a - b
tich = a * b
if b != 0:
   thuong = a / b
else:
    thuong = "Không thể chia cho 0"
print(f"Tổng hai số là : {tong}")
print(f"Hiệu hai số là : {hieu}")
print(f"Tích  hai số là : {tich}")
print(f"Thương hai số là : {thuong}")


