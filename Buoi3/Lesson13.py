# Nhập danh sách các số từ người dùng
numbers = list(map(int, input("Nhập danh sách các số, cách nhau bởi dấu cách: ").split()))
# Khởi tạo biến đếm
count_even = 0
count_odd = 0
# Duyệt qua từng số trong danh sách
for number in numbers:
    if number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
# In kết quả
print("Số chẵn:", count_even)
print("Số lẻ:", count_odd)
