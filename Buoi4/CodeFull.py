import datetime
import math
def mua_ga():
    so_ga  = 15000
    gia_ga = 25000
    gia_mua_xuan = gia_ga * 1.15  # giá gà mùa xuân tăng lên 15%
    gia_mua_he  = gia_ga * 0.9  #giá gà mùa xuân
    gia_mua_thu = gia_ga * 1.25
    gia_mua_dong = gia_ga * 0.6
    tong_tien_ga_mua_ga_xuan = so_ga * gia_mua_xuan
    tong_tien_mua_ga_he = so_ga * gia_mua_he
    tong_tien_mua_ga_thu = so_ga * gia_mua_thu
    tong_tien_mua_ga_dong = so_ga * gia_mua_dong
    print(f" Tổng tiền mua gà mùa xuân :  {tong_tien_ga_mua_ga_xuan}")
    print(f" Tổng tiền mua gà mùa hè  :  {tong_tien_mua_ga_he}")
    print(f"Tổng tiền mua gà mùa thu : {tong_tien_mua_ga_thu}")
    print(f"Tổng tiền mua gà mùa đông : {tong_tien_mua_ga_dong}")
    gia_tot_nhat = min(tong_tien_ga_mua_ga_xuan,tong_tien_mua_ga_he,tong_tien_mua_ga_thu,tong_tien_mua_ga_dong)
    if gia_tot_nhat == tong_tien_ga_mua_ga_xuan :
        print("Mùa xuân  mua gà là hợp lý nhất ")
    elif gia_tot_nhat ==tong_tien_mua_ga_he :
        print("Mùa hè   mua gà là hợp lý nhất ")
    elif gia_tot_nhat == tong_tien_mua_ga_thu :
        print("Mùa thu  mua gà là hợp lý nhất ")
    elif gia_tot_nhat == tong_tien_mua_ga_dong :
        print("Mùa đông  mua gà là hợp lý nhất ")
def TongHieuSoChanSoLe ():
    numbers = []
    for i in range(10):
        number = int(input(f"Nhập số thứ {i+1}: "))
        numbers.append(number)
        sum_even = 0
        sum_odd = 0
    for number in numbers:
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number
    difference = sum_even - sum_odd
    print(f"Tổng các số chẵn: {sum_even}")
    print(f"Tổng các số lẻ: {sum_odd}")
    print(f"Hiệu của tổng các số chẵn và tổng các số lẻ: {difference}")
def chuyen_doi_nhiet_do():
    print("Chương trình chuyển đổi nhiệt độ")
    print("1. Chuyển đổi từ độ C sang độ F")
    print("2. Chuyển đổi từ độ F sang độ C")
    lua_chon = input("Nhập lựa chọn của bạn (1 hoặc 2): ")
    if lua_chon == '1':
        do_c = float(input("Nhập nhiệt độ trong độ C: "))
        do_f = (do_c * 9/5) + 32
        print(f"{do_c} độ C = {do_f} độ F")
    elif lua_chon == '2':
        do_f = float(input("Nhập nhiệt độ trong độ F: "))
        do_c = (do_f - 32) * 5/9
        print(f"{do_f} độ F = {do_c} độ C")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.")
def kiem_tra_nam_nhuan_va_tuoi():
    nam_sinh = int(input("Nhập năm sinh của bạn: "))
    nam_hien_tai = datetime.datetime.now().year
    tuoi = nam_hien_tai - nam_sinh
    if (nam_sinh % 4 == 0 and nam_sinh % 100 != 0) or (nam_sinh % 400 == 0):
        print(f"Năm {nam_sinh} là năm nhuận.")
    else:
        print(f"Năm {nam_sinh} không phải là năm nhuận.")
    print(f"Tuổi của bạn là: {tuoi}")
def ucln_bcnn(a, b):
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    gcd = x
    # Tính BSCNN từ ƯSCLN và 2 số a, b
    lcm = (a * b) // gcd
    return gcd, lcm
def ThapPhanSangNhiPhan():
    while True:
        print("Chọn chuyển đổi:")
        print("1. Thập phân sang nhị phân")
        print("2. Nhị phân sang thập phân")
        print("0. Thoát")
        choice = input("Mời nhập lựa chọn: ")
        if choice == "1":
            SoThapPhan = int(input("Nhập số thập phân: "))
            if SoThapPhan == 0:
                print("Số nhị phân: 0")
            else:
                SoNhiPhan = ""
                while SoThapPhan > 0:
                    SoNhiPhan = str(SoThapPhan % 2) + SoNhiPhan
                    SoThapPhan = SoThapPhan // 2
                print(f"Số nhị phân: {SoNhiPhan}")
        elif choice == "2":
            SoNhiPhan = input("Nhập số nhị phân: ")
            if all(char in '01' for char in SoNhiPhan):
                SoThapPhan = 0
                for char in SoNhiPhan:
                    SoThapPhan = SoThapPhan * 2 + int(char)
                print(f"Số thập phân: {SoThapPhan}")
            else:
                print("Chuỗi nhập vào không phải là số nhị phân")
        elif choice == "0":
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại")
def giao_diem_duong_thang():
    """Tìm giao điểm của hai đường thẳng y = a1*x + b1 và y = a2*x + b2."""
    print("Nhập hệ số cho đường thẳng thứ nhất (y = a1*x + b1):")
    a1 = float(input("Nhập a1: "))
    b1 = float(input("Nhập b1: "))
    print("Nhập hệ số cho đường thẳng thứ hai (y = a2*x + b2):")
    a2 = float(input("Nhập a2: "))
    b2 = float(input("Nhập b2: "))
    # Kiểm tra nếu hai đường thẳng trùng nhau
    if a1 == a2 and b1 == b2:
        print("Hai đường thẳng trùng nhau.")
    # Kiểm tra nếu hai đường thẳng song song (không có giao điểm)
    elif a1 == a2:
        print("Hai đường thẳng song song, không có giao điểm.")
    else:
        # Tính tọa độ giao điểm
        x = (b2 - b1) / (a1 - a2)
        y = a1 * x + b1
        print(f"Giao điểm của hai đường thẳng là: x = {x}, y = {y}")
def TimSoXuatHienNhieuNhat_SoXuatHienItNhat():
    danh_sach = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))
    if not danh_sach:
        print("Danh sách trống.")
        return
    tan_suat = {}
    for so in danh_sach:
        if so in tan_suat:
            tan_suat[so] += 1
        else:
            tan_suat[so] = 1
    so_nhieu_nhat = max(tan_suat, key=tan_suat.get)
    so_it_nhat = min(tan_suat, key=tan_suat.get)
    so_nhieu_nhat_tan_suat = tan_suat[so_nhieu_nhat]
    so_it_nhat_tan_suat = tan_suat[so_it_nhat]
    print(f"Số xuất hiện nhiều nhất: {so_nhieu_nhat} (xuất hiện {so_nhieu_nhat_tan_suat} lần)")
    print(f"Số xuất hiện ít nhất: {so_it_nhat} (xuất hiện {so_it_nhat_tan_suat} lần)")
def TimSoLonSoBe():
    danh_sach = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))
    if len(danh_sach) < 2:
        print("Danh sách không có đủ các phần tử để tìm số lớn thứ 2 và nhỏ thứ 2.")
        return
    danh_sach = list(set(danh_sach))
    if len(danh_sach) < 2:
        print("Danh sách không có đủ các phần tử khác nhau để tìm số lớn thứ 2 và nhỏ thứ 2.")
        return
    danh_sach.sort()
    so_nho_thu_2 = danh_sach[1]
    so_lon_thu_2 = danh_sach[-2]
    print(f"Số lớn thứ 2: {so_lon_thu_2}")
    print(f"Số nhỏ thứ 2: {so_nho_thu_2}")
def tinh_dien_tich_va_chu_vi_hinh_hoc():
    choice = input("Chọn hình để tính diện tích: 1 Hình thang, 2 Hình bình hành: ")
    if choice == '1':
        a = float(input("Nhập đáy bé: "))
        b = float(input("Nhập đáy bé: "))
        c = float(input("Nhập đáy lớn: "))
        d = float(input("Nhập đáy lớn: "))
        h = float(input("Nhập chiều cao: "))
        C = a +b+c+d
        S = (a + c) * h / 2
        print(f"Chu Vi  hình thang: {C}")
        print(f"Diện tích hình thang: {S}")
    elif choice == '2':
        a = float(input("Nhập cạnh đáy: "))
        b = float(input("Nhập cạnh đáy: "))
        h = float(input("Nhập chiều cao: "))
        S = a * h
        C = 2 * (a+b)
        print(f"Diện tích hình bình hành: {S}")
        print(f"Chu vi hình bình hành : {C}")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.")
def TinhTongTichTrungBinh():
    danh_sach = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))
    if not danh_sach:
        print("Danh sách trống.")
        return
    tong = sum(danh_sach)
    tich = 1
    for so in danh_sach:
        tich *= so
    trung_binh = tong / len(danh_sach)
    print(f"Tổng của các số: {tong}")
    print(f"Tích của các số: {tich}")
    print(f"Trung bình của các số: {trung_binh:.2f}")
so = int(input("Nhập một số từ 0 đến 9: "))
def doc_so(x):
    return {
        0: "Không",
        1: "Một",
        2: "Hai",
        3: "Ba",
        4: "Bốn",
        5: "Năm",
        6: "Sáu",
        7: "Bảy",
        8: "Tám",
        9: "Chín"
    }.get(x, "Số không hợp lệ")
    print(doc_so(so))
def giai_phuong_trinh_bac_nhat():
    print("Giải phương trình bậc nhất dạng ax + b = 0")
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    if a != 0:
        x = -b / a
        print(f"Nghiệm của phương trình là: x = {x}")
    else:
        if b == 0:
            print("Phương trình vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
def giai_phuong_trinh_bac_hai():
    print("Giải phương trình bậc hai dạng ax^2 + bx + c = 0")
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm.")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
def chuyen_doi_don_vi():
    print("Chương trình chuyển đổi đơn vị:")
    print("1. Chuyển đổi từ feet sang mét")
    print("2. Chuyển đổi từ mét sang feet")
    lua_chon = input("Nhập lựa chọn của bạn (1 hoặc 2): ")
    if lua_chon == '1':
        feet = float(input("Nhập giá trị feet: "))
        meters = feet * 0.3048
        print(f"{feet} feet = {meters:.2f} mét")
    elif lua_chon == '2':
        meters = float(input("Nhập giá trị mét: "))
        feet = meters * 3.28084
        print(f"{meters} mét = {feet:.2f} feet")
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.")
def   main() :
    while True:
        print("""
        MENU
        1. mua gà 
        2.   Tính Tổng và Hiệu của các số chắn và số lẻ được nhập từ bàn phím với 10 số.0
        5 chuyển đổi nhiệt độ 
        6 Kiểm tra xem một năm sinh của bạn có phải là năm nhuận hay không và cho biết tuổi của bạn8
        
        8Chuyển đổi giữa hệ thập phân sang nhị phân, và ngược lại. *
        9  Viết chương trình tìm giao điểm của 2 đường thẳng
        10 Tìm số xuất hiện nhiều và ít nhất trong một danh sách. *
        11 Tìm số lớn thứ 2 và nhỏ thứ 2 trong một danh sách *
        12   Tính toán diện tích và chu vi các hình học khác như hình thang, hình bình hành.
        13 Viết chương trình tính tổng, tích, trung bình của các số trong một danh sách. *
        15 Viết chương trình để giải bậc nhất
        16  Viết chương trình để giải phương trình bậc 2
        17  Chuyển đổi đơn vị 
        0. Thoát
        """)
        choice = input("Nhập lựa chọn của bạn: ")
        if choice == '1':
            mua_ga()
        elif choice == '2':
                 TongHieuSoChanSoLe()
        elif choice == "5" :
           chuyen_doi_nhiet_do()
        elif choice == "6" :
           kiem_tra_nam_nhuan_va_tuoi()
        elif choice =="8" :
            ThapPhanSangNhiPhan()
        elif choice =="9" :
            giao_diem_duong_thang()
        elif choice == "10" :
            TimSoXuatHienNhieuNhat_SoXuatHienItNhat()
        elif choice == "11" :
            TimSoLonSoBe()
        elif choice == "12" :
            tinh_dien_tich_va_chu_vi_hinh_hoc()
        elif choice =="13" :
            TinhTongTichTrungBinh()
        elif choice == "15" :
            giai_phuong_trinh_bac_nhat()
        elif choice == "16" :
            giai_phuong_trinh_bac_hai()
        elif choice == "17" :
            chuyen_doi_don_vi()
        elif choice == '0':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
main()