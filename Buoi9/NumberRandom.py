import random
from tkinter import *
window = Tk()
window.geometry("500x500")
window.title("Number Random")
def NumberRandom():
    number = random.randint(1, 6)
    label.config(text=f"{number}")
label = Label(text="")
label.place(x=100, y=80, width=100, height=30)
button = Button(text="Roll", command=NumberRandom)
button.config( bg= "PINK")
button.place(x=110, y=20, width=80, height=20)
window.mainloop()