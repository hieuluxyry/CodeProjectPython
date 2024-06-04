import math
print("Giải Phương Trình Bậc Hai")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a != 0:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Có nghiệm kép x1 = x2 ={x} ")
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
else:
    print("Không phải Phương trình bậc 2")
