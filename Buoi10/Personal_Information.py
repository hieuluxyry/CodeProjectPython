from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Personal Information")
window.geometry("1280x720")
def PersonalInformation():
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    address = entry_address.get()
    if not name or not age or not gender or not address:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")
        return
    if any(char.isdigit() for char in name):
        messagebox.showerror("Lỗi", "Tên không được chứa số")
        return
    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Lỗi", "Tuổi phải là một số nguyên")
        return
    if gender.lower() not in ["nam", "nữ"]:
        messagebox.showerror("Lỗi", "Giới tính phải là 'nam' hoặc 'nữ'")
        return
    info = f"Tên: {name}\nTuổi: {age}\nGiới tính: {gender.capitalize()}\nĐịa chỉ: {address}"
    result_label.config(text=info)
    messagebox.showinfo("Thông báo", "Nhập thông tin thành công!")
label_name = Label(window, text="Tên:")
label_name.place(x=20, y=20, width=100, height=25)
entry_name = Entry(window)
entry_name.place(x=120, y=20, width=200, height=25)
label_age = Label(window, text="Tuổi:")
label_age.place(x=20, y=60, width=100, height=25)
entry_age = Entry(window)
entry_age.place(x=120, y=60, width=200, height=25)
label_gender = Label(window, text="Giới tính:")
label_gender.place(x=20, y=100, width=100, height=25)
entry_gender = Entry(window)
entry_gender.place(x=120, y=100, width=200, height=25)
label_address = Label(window, text="Địa chỉ:")
label_address.place(x=20, y=140, width=100, height=25)
entry_address = Entry(window)
entry_address.place(x=120, y=140, width=200, height=25)
submit_button = Button(window, text="Nộp thông tin", command=PersonalInformation)
submit_button.place(x=150, y=180, width=100, height=30)
result_label = Label(window, text="", bg="lightgrey")
result_label.place(x=20, y=220, width=360, height=300)
window.mainloop()