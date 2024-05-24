number = int(input(f"Nhập số cần kiểm tra: "))
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
if is_prime:
    print("Số nguyên tố ")
else:
    print("Không phải số nguyên tố!!!")
