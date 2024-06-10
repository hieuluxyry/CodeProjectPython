from tkinter import *
window = Tk()
window.title("Calculartor")
window.geometry("1280x720")
def sum_op():
    try:
        a = float(nhapa.get())
        b = float(nhapb.get())
        result.config(text=a + b)
        tinhtoan.insert(END, f"{a} + {b} = {a + b}\n")
    except ValueError:
        result.config(text="Vui lòng nhập số hợp lệ")
def subtract_op():
    try:
        a = float(nhapa.get())
        b = float(nhapb.get())
        result.config(text=a - b)
        tinhtoan.insert(END, f"{a} - {b} = {a - b}\n")
    except ValueError:
        result.config(text="Vui lòng nhập số hợp lệ")
def multiply_op():
    try:
        a = float(nhapa.get())
        b = float(nhapb.get())
        result.config(text=a * b)
        tinhtoan.insert(END, f"{a} * {b} = {a * b}\n")
    except ValueError:
        result.config(text="Vui lòng nhập số hợp lệ")
def divide_op():
    try:
        a = float(nhapa.get())
        b = float(nhapb.get())
        if b != 0:
            result.config(text=a / b)
            tinhtoan.insert(END, f"{a} / {b} = {a / b}\n")
        else:
            result.config(text="Không thể chia cho 0")
    except ValueError:
        result.config(text="Vui lòng nhập số hợp lệ")
def exit_app():
    window.quit()
soA = Label(window, text="Nhập số a:")
soA.place(x=20, y=20, width=100, height=25)
nhapa = Entry(window)
nhapa.place(x=120, y=20, width=200, height=25)
soB = Label(window, text="Nhập số b:")
soB.place(x=20, y=50, width=100, height=25)
nhapb = Entry(window)
nhapb.place(x=120, y=50, width=200, height=25)
result_label = Label(window, text="Kết quả:")
result_label.place(x=20, y=80, width=100, height=25)
result = Label(window, bg="Red", fg="Pink")
result.place(x=120, y=80, width=200, height=25)
tinhtoan_label = Label(window, text="Quá trình tính toán:")
tinhtoan_label.place(x=20, y=150, width=200, height=25)
tinhtoan = Text(window, bg="lightgrey", state=NORMAL)
tinhtoan.place(x=20, y=180, width=300, height=200)
sum_button = Button(window, text="+", command=sum_op)
sum_button.place(x=60, y=110, width=50, height=25)
subtract_button = Button(window, text="-", command=subtract_op)
subtract_button.place(x=120, y=110, width=50, height=25)
multiply_button = Button(window, text="*", command=multiply_op)
multiply_button.place(x=180, y=110, width=50, height=25)
divide_button = Button(window, text="/", command=divide_op)
divide_button.place(x=240, y=110, width=50, height=25)
exit_button = Button(window, text="Exit", command=exit_app)
exit_button.place(x=300, y=110, width=50, height=25)
window.mainloop()
