while True:
    print("1. km -> hm")
    print("2. Km -> dam")
    print("3. km -> m")
    print("4. dm -> dam")
    print("5. dm -> m")
    print("6. dam -> m")
    print("0. Quit")
    x = int(input("Nhập yêu cầu của bạn: "))
    if x == 0:
        print("Thoát khỏi chương trình.")
        break
    elif(x < 7):
        value = float(input("Nhập giá trị bạn muốn chuyển đổi: "))
        print("Giá trị chuyển đổi là", end=" ")
        if x == 1:
            print(10 * value, "hm")
        elif x == 2:
            print(100 * value, "dam")
        elif x == 3:
            print(1000 * value, "m")
        elif x == 4:
            print(10 * value, "dam")
        elif x == 5:
            print(100 * value, "m")
        elif x == 6:
            print(10 * value, "m")
    else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 0 đến 6.")



