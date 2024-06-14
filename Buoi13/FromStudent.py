import sqlite3
import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("Quản Lý Thông Tin Sinh Viên")
window.geometry("500x200")
def setup_database():
    with sqlite3.connect("StudentInfo.db") as db:
        cursor = db.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            Name TEXT PRIMARY KEY,
            Class TEXT NOT NULL
        )
        """)
        db.commit()
def add_student():
    student_name = name_entry.get()
    student_class = class_entry.get()
    if student_name and student_class:
        with sqlite3.connect("StudentInfo.db") as db:
            cursor = db.cursor()
            try:
                cursor.execute("INSERT INTO Students (Name, Class) VALUES (?, ?)", (student_name, student_class))
                db.commit()
                result_label.config(text=f"Đã thêm học sinh: {student_name} - Lớp: {student_class}")
            except sqlite3.IntegrityError:
                result_label.config(text="Tên học sinh đã tồn tại. Vui lòng chọn tên khác hoặc sửa thông tin.")
    else:
        result_label.config(text="Vui lòng nhập đầy đủ tên và lớp.")
def delete_student():
    student_name = name_entry.get()
    if student_name:
        with sqlite3.connect("StudentInfo.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM Students WHERE Name = ?", (student_name,))
            if cursor.fetchone():
                cursor.execute("DELETE FROM Students WHERE Name = ?", (student_name,))
                db.commit()
                result_label.config(text=f"Đã xóa học sinh: {student_name}")
            else:
                result_label.config(text=f"Không tìm thấy học sinh với tên {student_name}. Vui lòng kiểm tra lại.")
    else:
        result_label.config(text="Vui lòng nhập tên học sinh để xóa.")
def exit_application():
    window.destroy()
setup_database()

name_label = tk.Label(window, text="Enter Student Name :")
name_label.pack()
name_label.place(x=20, y=20, width=150, height=25)
name_entry = tk.Entry(window)
name_entry.pack()
name_entry.place(x=200, y=20, width=200, height=25)
class_label = tk.Label(window, text="Enter student garde :")
class_label.pack()
class_label.place(x=20, y=50, width=150, height=25)
class_entry = tk.Entry(window)
class_entry.pack()
class_entry.place(x=200, y=50, width=200, height=25)
add_button = tk.Button(window, text="Add", command=add_student)
add_button.pack()
add_button.place(x=180, y=110, width=50, height=25)
delete_button = tk.Button(window, text="Clear", command=delete_student)
delete_button.pack()
delete_button.place(x=240, y=110, width=50, height=25)
exit_button = tk.Button(window, text="Exit", command=exit_application)
exit_button.pack()
exit_button.place(x=300, y=110, width=50, height=25)
result_label = tk.Label(window, text="")
result_label.pack()
result_label.place(x=20, y=150, width=400, height=25)
window.mainloop()
