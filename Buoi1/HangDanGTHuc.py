# Nhập hai số a và b từ bàn phím
a = float(input("Enter Number a : "))
b = float(input("Enter Number b : "))
# Tính các hằng đẳng thức
# 1. (a + b)^2 = a^2 + 2ab + b^2
expr1_LeftSide = (a + b)**2
expr1_RightSide = a**2 + 2*a*b + b**2
# 2. (a - b)^2 = a^2 - 2ab + b^2
expr2_LeftSide = (a - b)**2
expr2_RightSide = a**2 - 2*a*b + b**2
# 3. a^2 - b^2 = (a - b)(a + b)
expr3_LeftSide= a**2 - b**2
expr3_RightSide = (a - b) * (a + b)
# 4. (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3
expr4_LeftSide= (a + b)**3
expr4_RightSide= a**3 + 3*a**2*b + 3*a*b**2 + b**3
# In kết quả
print(f"(a + b)^2: Left Side  = {expr1_LeftSide}, Right Side  = {expr1_RightSide}")
print(f"(a - b)^2: Left Side  = {expr2_LeftSide}, Right Side  = {expr2_RightSide}")
print(f"a^2 - b^2: Left Side  = {expr3_LeftSide}, Right Side  = {expr3_RightSide}")
print(f"(a + b)^3: Left Side  = {expr4_LeftSide}, Right Side  = {expr4_RightSide}")
