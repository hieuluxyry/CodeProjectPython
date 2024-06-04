# Nhập danh sách các phần tử từ người dùng
numbers = input("Nhập danh sách các số : ")
# Chuyển đổi chuỗi nhập vào thành danh sách các số
numbers_list = [float(num) for num in numbers.split(",")]
# Tính tổng của các phần tử
sum_of_numbers = sum(numbers_list)
# Tính tích của các phần tử
product_of_numbers = 1
for num in numbers_list:
    product_of_numbers *= num
# In kết quả
print("Tổng của các phần tử là:", sum_of_numbers)
print("Tích của các phần tử là:", product_of_numbers)
