#Nhập ba cạnh tam giác từ bàn phím
import math
a = float(input("Enter edge a : "))
b = float(input("Enter edge b : "))
c = float(input("Enter edge c : "))
# kiểm tra có phải là tam giác ko
if a + b > c and b + c > a and c + a > b:
    print("Three sides make a triangle!")
    triangle = a + b + c
    print(f"The perimeter of the triangle is:  {triangle}")
    p = triangle / 2  #tính nửa chu vi áp dụng công thức p =  P/2
    #tính diện tích của tam giác áp dụng công thức Heron S = sqrt(p*(p-a)*(p-b)*(p-c)
    Area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"The area of the triangle is :{Area}")
else:
    print("Three sides don't make a triangle")