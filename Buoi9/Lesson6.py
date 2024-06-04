from tkinter import *
window = Tk()
window.geometry('500x500')
window.title("ListNumber")
def themList():
    number = entry.get()
    if number.isdigit():
        listbox.insert(END, number)
    entry.delete(0, END)
def xoa():
    listbox.delete(0, END)
label_nhap = Label( text="Enter a number:")
label_nhap.place(x=20, y=50, width=100, height=25)
label_list = Label( text="List:")
label_list.place(x=20, y=100, width=100, height=25)
entry = Entry()
entry.place(x=150, y=50, width=100, height=25)
button_them = Button( text="Add a list", command=themList)
button_them.place(x=300, y=50, width=100, height=25)
button_xoa = Button( text="Clear a list", command=xoa)
button_xoa.place(x=300, y=100, width=100, height=25)
listbox = Listbox()
listbox.place(x=150, y=100, width=100, height=150)
window.mainloop()
