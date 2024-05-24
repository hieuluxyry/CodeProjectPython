print("Kiểm tra 1 tháng trong 12 tháng có bao nhiêu ngày ")
month = int(input("enter the month : "))
if month == 2:
    print("The month 2 has 28 or 29 days!")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    print(f"The month {month} has 31 days!")
elif month in [4, 6, 9, 11]:
    print(f"The month {month} has 30 days!")
else:
    print("Invalid month!!")