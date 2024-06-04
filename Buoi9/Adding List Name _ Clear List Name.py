from tkinter import *
window = Tk()
window.title("User Input")
window.geometry("500x500")
names = []
def add_name():
    name = entry.get()
    if name:
        names.append(name)
        listbox.insert(END, name)
        entry.delete(0, END)
def clear_list():
    names.clear()
    listbox.delete(0, END)
entry = Entry(window, width=50)
entry.pack(pady=10)
add_button = Button(window, text="Add", command=add_name)
add_button.pack(pady=10)
listbox = Listbox(window, width=50, height=15)
listbox.pack(pady=10)
clear_button = Button(window, text="Clear", command=clear_list)
clear_button.pack(pady=10)
window.mainloop()


