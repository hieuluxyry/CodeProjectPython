number = int(input("Nhập một số: "))
factorial_value = 1
for i in range(1, number + 1):
    factorial_value *= i
print("Giai thừa của", number, "là:", factorial_value)
