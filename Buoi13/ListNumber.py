import sqlite3
import tkinter as tk
from tkinter import messagebox
def setup_database():
    with sqlite3.connect("NumbersInfo.db") as db:
        cursor = db.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Numbers (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Number INTEGER NOT NULL
        )
        """)
        db.commit()
def add_to_list():
    number = entry.get()
    if number.isdigit():
        listbox.insert(tk.END, number)
        with sqlite3.connect("NumbersInfo.db") as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO Numbers (Number) VALUES (?)", (int(number),))
            db.commit()
        entry.delete(0, tk.END)
    else:
        entry.delete(0, tk.END)
        messagebox.showerror("Lỗi", "Vui lòng nhập một số nguyên.")
def clear_list():
    listbox.delete(0, tk.END)
    with sqlite3.connect("NumbersInfo.db") as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM Numbers")
        db.commit()
def load_numbers():
    with sqlite3.connect("NumbersInfo.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT Number FROM Numbers")
        numbers = cursor.fetchall()
        for number in numbers:
            listbox.insert(tk.END, number[0])
setup_database()
window = tk.Tk()
window.title("Nhập Số Nguyên Vào Danh Sách")
window.geometry("400x300")
instruction_label = tk.Label(window, text="Enter a Number interger:")
instruction_label.pack()
instruction_label.place(x=20, y=20, width=150, height=25)
entry = tk.Entry(window)
entry.pack()
entry.place(x=200, y=20, width=150, height=25)
add_button = tk.Button(window, text="Add a list ", command=add_to_list)
add_button.pack()
add_button.place(x=50, y=60, width=100, height=30)
listbox = tk.Listbox(window)
listbox.pack()
listbox.place(x=20, y=110, width=330, height=120)
clear_button = tk.Button(window, text="Clear a list", command=clear_list)
clear_button.pack()
clear_button.place(x=200, y=60, width=150, height=30)
load_numbers()
window.mainloop()
