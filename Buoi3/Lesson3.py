import math

# Nhập các cạnh của tam giác
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

# Nhập bán kính của hình tròn
radius = float(input("Nhập bán kính: "))

# Kiểm tra điều kiện tam giác và tính chu vi, diện tích nếu hợp lệ
if a + b > c and a + c > b and b + c > a:
    perimeter_triangle = a + b + c
    s = perimeter_triangle / 2
    area_triangle = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Hình tam giác có cạnh a={a}, b={b}, c={c}:")
    print(f"  Chu vi: {perimeter_triangle}")
    print(f"  Diện tích: {area_triangle}")
else:
    print(f"Các cạnh a={a}, b={b}, c={c} không tạo thành tam giác hợp lệ.")

# Tính chu vi và diện tích hình tròn
circumference_circle = 2 * math.pi * radius
area_circle = math.pi * radius ** 2
print(f"Hình tròn có bán kính {radius}:")
print(f"  Chu vi: {circumference_circle}")
print(f"  Diện tích: {area_circle}")

