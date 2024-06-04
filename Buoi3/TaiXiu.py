import random
# Lắc ba xúc xắc
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
dice3 = random.randint(1, 6)
# Tính tổng
total = dice1 + dice2 + dice3
print(f"Kết quả của ba xúc xắc là: {dice1}, {dice2}, {dice3}")
print(f"Tổng là: {total}")
# Kiểm tra và in ra kết quả
if 3<=  total <=10:
    print("Kết quả: Xỉu")
elif  11<= total <=18 :
    print("Kết quả: Tài")

