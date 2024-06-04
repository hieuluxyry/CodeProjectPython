a = int(input("Nhập số tự nhiên từ 1 tới 10 : "))
if 1 <= a <= 10:
    print(f"Bảng cửu chương của : {a}")
    for i in range(1, 11):
        print(f"{a} x {i} = {a*i}")
else:
    print(f"Lỗi mời nhập lại số từ 1 đến 10!")
