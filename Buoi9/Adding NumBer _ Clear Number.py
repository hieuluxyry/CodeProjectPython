from tkinter import *
def add_number():
    try:
        number = int(entry.get())
        current_result = int(result_label['text'])
        result_label.config(text=str(current_result + number))
    except ValueError:
        result_label.config(text="không hợp lệ")
def clear():
    entry.delete(0, END)
    result_label.config(text="0")
window = Tk()
window.title("Adding NumBer _ Clear Number")
Label(window, text="Nhập Số:").grid(row=0, column=0, padx=10, pady=10)
entry = Entry(window)
entry.grid(row=0, column=1, padx=10, pady=10)
add_button = Button(window, text="Add", command=add_number)
add_button.grid(row=0, column=2, padx=10, pady=10)
Label(window, text="Trả lời=").grid(row=1, column=0, padx=10, pady=10)
result_label = Label(window, text="0")
result_label.grid(row=1, column=1, padx=10, pady=10)
clear_button = Button(window, text="Clear", command=clear)
clear_button.grid(row=1, column=2, padx=10, pady=10)
window.mainloop()
