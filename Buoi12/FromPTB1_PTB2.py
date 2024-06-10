import tkinter as tk
from tkinter import messagebox
import math

window = tk.Tk()
window.title("Máy tính giải phương trình")

def solve_linear_equation():
    try:
        a = float(entry_a1.get())
        b = float(entry_b1.get())
        if a == 0:
            if b == 0:
                result = "Phương trình vô số nghiệm."
            else:
                result = "Phương trình vô nghiệm."
        else:
            x = -b / a
            result = f"Nghiệm của phương trình là x = {x:.2f}"
    except ValueError:
        result = "Vui lòng nhập giá trị số hợp lệ."

    messagebox.showinfo("Kết quả", result)

def clear_linear_data():
    entry_a1.delete(0, tk.END)
    entry_b1.delete(0, tk.END)

def solve_quadratic_equation():
    try:
        a = float(entry_a2.get())
        b = float(entry_b2.get())
        c = float(entry_c2.get())

        if a == 0:
            result = "Đây không phải là phương trình bậc hai."
        else:
            delta = b**2 - 4*a*c
            if delta < 0:
                result = "Phương trình vô nghiệm."
            elif delta == 0:
                x = -b / (2 * a)
                result = f"Phương trình có nghiệm kép x = {x:.2f}"
            else:
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                result = f"Nghiệm của phương trình là x1 = {x1:.2f}, x2 = {x2:.2f}"
    except ValueError:
        result = "Vui lòng nhập giá trị số hợp lệ."

    messagebox.showinfo("Kết quả", result)

# Hàm xóa dữ liệu trong các ô nhập liệu cho phương trình bậc hai
def clear_quadratic_data():
    entry_a2.delete(0, tk.END)
    entry_b2.delete(0, tk.END)
    entry_c2.delete(0, tk.END)

# Giao diện cho phương trình bậc nhất
frame_linear = tk.Frame(window)
frame_linear.pack(padx=50, pady=10)

label_linear = tk.Label(frame_linear, text="Giải phương trình bậc nhất (ax + b = 0)")
label_linear.pack()

label_a1 = tk.Label(frame_linear, text="a:")
label_a1.pack(side=tk.LEFT)
entry_a1 = tk.Entry(frame_linear, width=30)
entry_a1.pack(side=tk.LEFT)

label_b1 = tk.Label(frame_linear, text="b:")
label_b1.pack(side=tk.LEFT)
entry_b1 = tk.Entry(frame_linear, width=30)
entry_b1.pack(side=tk.LEFT)

button_solve1 = tk.Button(frame_linear, text="Giải", command=solve_linear_equation)
button_solve1.pack(side=tk.LEFT, padx=25)

button_clear1 = tk.Button(frame_linear, text="Clear", command=clear_linear_data)
button_clear1.pack(side=tk.LEFT, padx=25)

frame_quadratic = tk.Frame(window)
frame_quadratic.pack(padx=50, pady=50)
label_quadratic = tk.Label(frame_quadratic, text="Giải phương trình bậc hai (ax^2 + bx + c = 0)")
label_quadratic.pack()
label_a2 = tk.Label(frame_quadratic, text="a:")
label_a2.pack(side=tk.LEFT)
entry_a2 = tk.Entry(frame_quadratic, width=30)
entry_a2.pack(side=tk.LEFT)
label_b2 = tk.Label(frame_quadratic, text="b:")
label_b2.pack(side=tk.LEFT)
entry_b2 = tk.Entry(frame_quadratic, width=30)
entry_b2.pack(side=tk.LEFT)
label_c2 = tk.Label(frame_quadratic, text="c:")
label_c2.pack(side=tk.LEFT)
entry_c2 = tk.Entry(frame_quadratic, width=30)
entry_c2.pack(side=tk.LEFT)
button_solve2 = tk.Button(frame_quadratic, text="Giải", command=solve_quadratic_equation)
button_solve2.pack(side=tk.LEFT, padx=25)
button_clear2 = tk.Button(frame_quadratic, text="Clear", command=clear_quadratic_data)
button_clear2.pack(side=tk.LEFT, padx=25)
window.mainloop()
