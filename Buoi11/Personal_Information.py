from tkinter import *
window = Tk()
window.title("Personal Information")
window.geometry("1200x1000")
try:
    anh = PhotoImage(file="Hieudelicate.png")
    Anh = Label(window, image=anh)
    Anh.place(x=450, y=100, width=300, height=200)
except Exception as e:
    print(f"Error loading image: {e}")
def Display_Personal_Information(message):
    display.config(state=NORMAL)
    display.insert(END, message + "\n")
    display.see(END)
    display.config(state=DISABLED)
def Personal_Information():
    name = Enternames.get()
    if name:
        greeting = f"Hello {name}, welcome to Ha Noi City <3 "
        Display_Personal_Information(greeting)
names = Label(window, text="Nhập họ và tên:")
names.place(x=400, y=350, width=120, height=40)
Enternames = Entry(window)
Enternames.place(x=520, y=350, width=300, height=25)
nut = Button(window, text="Click here", background="pink", command=Personal_Information)
nut.place(x=400, y=400, width=100, height=25)
display = Text(window, bg="white", state=DISABLED, font=("Times New Roman", 12),fg="red")
display.place(x=520, y=400, width=300, height=200)
window.mainloop()
