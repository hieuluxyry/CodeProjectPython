print("Kiểm tra năm nhuận ")
year = int(input("Nhập năm cần kiểm tra: "))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("Là năm nhuận!")
        else:
            print("Là năm không nhuận!")
    else:
        print("Là năm nhuận!")
else:
    print("Là năm không nhuận!")
