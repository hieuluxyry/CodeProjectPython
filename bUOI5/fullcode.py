def ThongTinCaNhanCuaMinh(filename):
    name = input("Nhập tên của bạn: ")
    age = input("Nhập tuổi của bạn: ")
    address = input("Nhập địa chỉ của bạn: ")
    telephone =  input("Nhập Số Điện Thoại ")
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Tên: {name}\n")
        file.write(f"Tuổi: {age}\n")
        file.write(f"Địa chỉ: {address}\n")
        file.write(f"Telephone : {telephone}")
    print(f"Đã tạo file {filename} với thông tin cá nhân của bạn.")
def ThongTinCaNhanCuaBanMinh(filename):
    friend_name = input("Nhập tên bạn của bạn: ")
    friend_age = input("Nhập tuổi bạn của bạn: ")
    friend_address = input("Nhập địa chỉ bạn của bạn: ")
    firend_telephone =  input("Nhập Số Điện Thoại ")
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"\nThông tin bạn của bạn:\n")
        file.write(f"Tên: {friend_name}\n")
        file.write(f"Tuổi: {friend_age}\n")
        file.write(f"Địa chỉ: {friend_address}\n")
        file.write(f"Số điện thoại : {firend_telephone}")
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print("Nội dung trong file:")
    print(content)
def XuLyTinhToanHaiSo(filename):
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    total = a + b
    difference = a - b
    product = a * b
    quotient = a / b if b != 0 else "Không thể chia cho 0"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Số a: {a}\n")
        file.write(f"Số b: {b}\n")
        file.write(f"Tổng: {total}\n")
        file.write(f"Hiệu: {difference}\n")
        file.write(f"Tích: {product}\n")
        file.write(f"Thương: {quotient}\n")
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print("Nội dung trong file:")
    print(content)
def VeMatCuoi(filename):
    smiley = [
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠖⠒⠉⠉⠁⠀⠀⠀⠀⠀⠉⠉⠁⠒⠢⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠊⠁⠀⢀⣠⠤⠒⠒⠋⠉⠉⠉⠉⠉⠑⠒⠒⠤⣀⡀⠀⠉⠒⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠊⠀⢀⡠⠖⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⣄⠀⠈⠷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⢀⡴⠉⠀⣠⠔⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠢⡀⠁⠑⢤⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⡰⠋⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠘⠳⡄⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⢀⡜⠁⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣄⠀⠘⣆⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⡞⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣟⡽⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠈⣆⠀⠀⠀\n"
        "⠀⠀⠀⡼⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⣿⡽⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆⠀⢿⡄⠀⠀\n"
        "⠀⠀⢰⠇⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣷⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠘⣷⠀⠀\n"
        "⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣄⡄⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⢹⡇⠀\n"
        "⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⢿⣿⢿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀\n"
        "⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⣟⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀\n"
        "⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⣯⣷⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀\n"
        "⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡇⠀\n"
        "⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⡀⠀\n"
        "⣤⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⠿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠤⠤⠚⣉⡆\n"
        "⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠭⣛⠻⠿⢿⣿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⣶⣶⠶⠽⠟⠁\n"
        "⠙⣧⣄⡑⠂⠤⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠛⠻⢶⣦⣤⡀⠀⠀⠀⢀⣀⠀⠉⠳⡄⠀⠀\n"
        "⠀⠈⠙⠻⠷⠶⣶⣦⣌⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⡤⠤⠤⠤⠶⠶⠿⠛⠃⠀⠀⢰⣧⣤⣤⣶⠿⠃⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⠶⠶⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣄⡀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⣀⡤⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⢀⠀\n"
        "⠀⠀⠀⠀⠀⢰⣃⠐⠦⠤⠤⠄⠀⠠⠤⠤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣵\n"
        "⠀⠀⠀⠀⠀⠀⠛⠿⠶⠦⠶⠶⠶⠶⢶⣂⡤⣤⡉⠉⠀⠐⠒⠒⠒⠒⠒⠒⠒⠒⠀⠀⠉⠉⢉⣀⠀⡉⠉⠉⠀⠐⠒⠤⠤⠀⠀⠄⢀⣿\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠛⠛⠛⠳⠶⠶⠶⠶⠶⠶⠿⠚⠚⠛⠓⠀⠀⠀⠀⠈⠛⠛⠓⠶⣶⣶⣤⣤⣶⡾⠋\n"
    ]
    with open(filename, 'w', encoding='utf-8') as file:
        for line in smiley:
            file.write(line + '\n')
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print("Nội dung trong file:")
    print(content)
def TongTichSoChanSoLe(filename):
    numbers = list(map(int, input("Nhập vào một dãy số, cách nhau bởi dấu phẩy: ").split(',')))
    total_even = sum(x for x in numbers if x % 2 == 0)
    total_odd = sum(x for x in numbers if x % 2 != 0)
    product_even = 1
    product_odd = 1
    for x in numbers:
        if x % 2 == 0:
            product_even *= x
        else:
            product_odd *= x
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Dãy số: {numbers}\n")
        file.write(f"Tổng các số chẵn: {total_even}\n")
        file.write(f"Tổng các số lẻ: {total_odd}\n")
        file.write(f"Tích các số chẵn: {product_even}\n")
        file.write(f"Tích các số lẻ: {product_odd}\n")
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print("Nội dung trong file:")
    print(content)
def DemKiTu(filename):
    name = input("Nhập tên của bạn: ")
    age = input("Nhập tuổi của bạn: ")
    address = input("Nhập địa chỉ của bạn: ")
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Tên: {name}\n")
        file.write(f"Tuổi: {age}\n")
        file.write(f"Địa chỉ: {address}\n")
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print(f"Số ký tự trong file là: {len(content)}")
def TinhGiaiThua(filename):
    n = int(input("Nhập vào số tự nhiên n: "))
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Giai thừa của {n} là {factorial}\n")
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print("Nội dung trong file:")
    print(content)
def TinhTong_TinhTrungBinh_MaxDiem_MinDiem(filename):
    students = {}
    for i in range(5):
        name = input(f"Nhập tên sinh viên thứ {i + 1}: ")
        scores = list(map(float, input("Nhập điểm 5 môn, cách nhau bởi dấu phẩy: ").split(',')))
        total = sum(scores)
        average = total / len(scores)
        students[name] = {'total': total, 'average': average}
    with open(filename, 'w', encoding='utf-8') as file:
        for name, data in students.items():
            file.write(f"Sinh viên: {name}\n")
            file.write(f"Tổng điểm: {data['total']}\n")
            file.write(f"Điểm trung bình: {data['average']}\n")
            file.write("\n")
        highest_avg_student = max(students, key=lambda x: students[x]['average'])
        lowest_avg_student = min(students, key=lambda x: students[x]['average'])
        file.write(f"Sinh viên có điểm trung bình cao nhất: {highest_avg_student}\n")
        file.write(f"Sinh viên có điểm trung bình thấp nhất: {lowest_avg_student}\n")
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print("Nội dung trong file:")
    print(content)
def DanhSachThuMoi(filename):
    invitations = []
    while True:
        name = input("Nhập tên người mời (hoặc nhập 'done' để kết thúc): ")
        if name.lower() == 'done':
            break
        invitations.append(name)
    with open(filename, 'w', encoding='utf-8') as file:
        for name in invitations:
            file.write(name + '\n')
    print("Danh sách thư mời:")
    print('\n'.join(invitations))
    remove_name = input("Nhập tên người muốn xóa khỏi danh sách: ")
    if remove_name in invitations:
        invitations.remove(remove_name)
    with open(filename, 'w', encoding='utf-8') as file:
        for name in invitations:
            file.write(name + '\n')
    print("Danh sách thư mời sau khi xóa:")
    print('\n'.join(invitations))
def DocChuoiBatKi(filename):
    content = input("Nhập vào một chuỗi bất kỳ: ")
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content + '\n')
    with open(filename, 'r', encoding='utf-8') as file:
        read_content = file.read()
    print("Nội dung trong file:")
    print(read_content)
def menu():
    while True:
        print("\nChọn chức năng:")
        print("1. Tạo file với thông tin cá nhân")
        print("2. Thêm thông tin của bạn và đọc toàn bộ thông tin")
        print("3. Tính toán các phép toán cơ bản với hai số")
        print("4. Vẽ mặt cười")
        print("5. Tính tổng và tích của số chẵn và lẻ")
        print("6. Nhập thông tin cá nhân và đếm ký tự của file")
        print("7. Tính giai thừa của số tự nhiên n")
        print("8. Tính điểm sinh viên")
        print("9. Quản lý danh sách thư mời")
        print("10. Đọc chuỗi bất kỳ")
        print("0. Thoát")
        choice = int(input("Nhập lựa chọn của bạn: "))
        if choice == 1:
            filename = "PhamVanHieu.txt"
            ThongTinCaNhanCuaMinh(filename)
        elif choice == 2:
            filename = "ThongTinCaNhanCuaBanMinh.txt"
            ThongTinCaNhanCuaBanMinh(filename)
        elif choice == 3:
            filename = "XuLyTinhToanHaiSo.txt"
            XuLyTinhToanHaiSo(filename)
        elif choice == 4:
            filename = "  VeMatCuoi.txt"
            VeMatCuoi(filename)
        elif choice == 5:
            filename = "TongTichSoChanSoLe.txt"
            TongTichSoChanSoLe(filename)
        elif choice == 6:
            filename = "DemKiTu.txt"
            DemKiTu(filename)
        elif choice == 7:
            filename = "TinhGiaiThua.txt"
            TinhGiaiThua(filename)
        elif choice == 8:
            filename = "TinhTong_TinhTrungBinh_MaxDiem_MinDiem.txt"
            TinhTong_TinhTrungBinh_MaxDiem_MinDiem(filename)
        elif choice == 9:
            filename = "DanhSachThuMoi.txt"
            DanhSachThuMoi(filename)
        elif choice == 10:
            filename = "DocChuoiBatKi.txt"
            DocChuoiBatKi(filename)
        elif choice == 0:
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
menu()