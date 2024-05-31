import random
import shutil
import os
def SoNgauNhien(filename, soluongso, gioihan):
    with open(filename, 'w') as file:
        for _ in range(soluongso):
            songaunhien = random.randint(0, gioihan)
            file.write(f"{songaunhien}\n")
def docsongaunhien(filename):
    with open(filename, 'r') as file:
        noidung = file.read()
        return noidung
def ghibancuuchuong(filename):
    with open(filename, 'w', encoding='utf8') as file:
        for i in range(1, 11):
            for j in range(1, 11):
                file.write(f"{i} * {j} = {i*j}\n")
def kiemtrabangcuuchuong5(filename):
    with open(filename, "r", encoding="utf8") as file:
        noidung = file.read()
    return "5 * 1 = 5" in noidung
filename = 'so_ngau_nhien.txt'
soluongso = 10
gioihan = 100
tenfilecuuchuong = 'bangcuuchuong.txt'
filecopy = 'bangcuuchuong1.txt'
thumuccu = 'thumucmoi'
filemoi = 'Hieudelicate.txt'
def menu():
    print("1. Tạo file các số ngẫu nhiên")
    print("2. Đọc file số ngẫu nhiên")
    print("3. Ghi bảng cửu chương vào file")
    print("4. Sao chép nội dung file bảng cửu chương")
    print("5. Di chuyển file")
    print("6. Xoá file")
    print("7. Kiểm tra bảng cửu chương 5 có tồn tại không")
    print("8. Đổi tên file")
    print("9. Thoát chương trình")
    choice = int(input("Nhập lựa chọn của bạn: "))
    return choice
while True:
    choice = menu()
    if choice == 1:
        SoNgauNhien(filename, soluongso, gioihan)
        print(f"Đã tạo file {filename} với các số ngẫu nhiên.")
    elif choice == 2:
        noidung = docsongaunhien(filename)
        print(f"Nội dung của file {filename}:\n{noidung}")
    elif choice == 3:
        ghibancuuchuong(tenfilecuuchuong)
        print(f"Bảng cửu chương đã được ghi vào tệp {tenfilecuuchuong}")
    elif choice == 4:
        shutil.copy(tenfilecuuchuong, filecopy)
        print(f"Nội dung của tệp {tenfilecuuchuong} đã được sao chép sang tệp {filecopy}")
    elif choice == 5:
        os.makedirs(thumuccu, exist_ok=True)
        filedichuyen = os.path.join(thumuccu, os.path.basename(filecopy))
        shutil.move(filecopy, filedichuyen)
        print(f"Tệp {filecopy} đã được di chuyển đến {filedichuyen}")
    elif choice == 6:
        os.remove(filedichuyen)
        print(f"Tệp {filedichuyen} đã được xóa")
    elif choice == 7:
        bang5 = kiemtrabangcuuchuong5(tenfilecuuchuong)
        print(f"Có bảng cửu chương 5 trong tệp {tenfilecuuchuong}: {bang5}")
    elif choice == 8:
        os.rename(filename, filemoi)
        print(f"Tệp {filename} đã được đổi tên thành {filemoi}")
    elif choice == 9:
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
