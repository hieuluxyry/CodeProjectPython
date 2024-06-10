from tkinter import *
from tkinter import messagebox
import math
window = Tk()
window.title("Versatile Calculation Program")
window.geometry('500x600')
def tinh_giai_thua():
    try:
        n = int(entry_factorial.get())
        result = math.factorial(n)
        messagebox.showinfo("Kết quả", f"Giai thừa của {n} là: {result}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ!")
def tinh_toan():
    try:
        a = float(entry_num1.get())
        b = float(entry_num2.get())
        tong = a + b
        hieu = a - b
        tich  = a * b
        if b != 0:
            thuong  = a / b
        else:
            thuong = "Không xác định"
        messagebox.showinfo("Kết quả", f"Tổng: {tong}\nHiệu: {hieu}\nTích: {tich}\nThương: {thuong}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")
def giai_pt_bac_nhat():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if a != 0:
            nghiem = -b / a
            messagebox.showinfo("Kết quả", f"Phương trình có nghiệm x = {nghiem}")
        else:
            messagebox.showerror("Lỗi", "a phải khác 0!")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")
def tinh_hang_dang_thuc():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        binh_phuong_tong = (x + y) ** 2
        binh_phuong_hieu = (x - y) ** 2
        hieu_binh_phuong = x ** 2 - y ** 2
        lap_phuong_tong = (x + y) ** 3
        messagebox.showinfo("Kết quả", f"(x + y)^2 = {binh_phuong_tong}\n(x - y)^2 = {binh_phuong_hieu}\n(x^2 - y^2) = {hieu_binh_phuong}\n(x + y)^3 = {lap_phuong_tong}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")
def vetamgiac():
    canvas.delete("all")
    canvas.create_line(50, 150, 150, 150, fill="black")
    canvas.create_line(50, 150, 100, 50, fill="black")
    canvas.create_line(150, 150, 100, 50, fill="black")
    et_kq.delete(0, END)
    et_kq.insert(0, "Đã vẽ tam giác")
def thoat_chuong_trinh():
    window.quit()
Label(window, text="Nhập số để tính giai thừa:")
entry_factorial = Entry(window)
entry_factorial.grid(row=0, column=1, padx=10, pady=5, sticky=W)
Button(window, text="Tính giai thừa", command=tinh_giai_thua).grid(row=1, column=0, columnspan=2, padx=10, pady=5)
Label(window, text="Nhập hai số để tính tổng, hiệu, tích, thương:").grid(row=2, column=0, padx=10, pady=5, sticky=W)
entry_num1 = Entry(window)
entry_num1.grid(row=3, column=0, padx=10, pady=5, sticky=W)
entry_num2 = Entry(window)
entry_num2.grid(row=3, column=1, padx=10, pady=5, sticky=W)
Button(window, text="Tính toán", command=tinh_toan).grid(row=4, column=0, columnspan=2, padx=10, pady=5)
Label(window, text="Nhập a và b để giải phương trình ax + b = 0:").grid(row=5, column=0, padx=10, pady=5, sticky=W)
entry_a = Entry(window)
entry_a.grid(row=6, column=0, padx=10, pady=5, sticky=W)
entry_b = Entry(window)
entry_b.grid(row=6, column=1, padx=10, pady=5, sticky=W)
Button(window, text="Giải phương trình bậc nhất", command=giai_pt_bac_nhat).grid(row=7, column=0, columnspan=2, padx=10, pady=5)
Label(window, text="Nhập x và y để tính hằng đẳng thức:").grid(row=8, column=0, padx=10, pady=5, sticky=W)
entry_x = Entry(window)
entry_x.grid(row=9, column=0, padx=10, pady=5, sticky=W)
entry_y = Entry(window)
entry_y.grid(row=9, column=1, padx=10, pady=5, sticky=W)
Button(window, text="Tính hằng đẳng thức", command=tinh_hang_dang_thuc).grid(row=10, column=0, columnspan=2, padx=10, pady=5)
Button(window, text="Vẽ tam giác", command=vetamgiac).grid(row=11, column=0, columnspan=2, padx=10, pady=5)
canvas = Canvas(window, width=400, height=300, bg="white")
canvas.grid(row=12, column=0, columnspan=2, padx=10, pady=5)
Label(window, text="Kết quả vẽ tam giác:").grid(row=13, column=0, padx=10, pady=5, sticky=W)
et_kq = Entry(window)
et_kq.grid(row=13, column=1, padx=10, pady=5, sticky=W)
Button(window, text="Thoát", command=thoat_chuong_trinh).grid(row=14, column=0, columnspan=2, padx=10, pady=5)
window.mainloop()
