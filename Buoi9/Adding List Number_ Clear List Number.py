from tkinter import *
windown = Tk()
windown.geometry("300x300")
windown.title("Hello name")
def name():
    name=entry_name.get()
    lable_name=Label(text=f"Hello {name}")
    lable_name.place(x=130,y=90,width=100,height=30)
    lable_name.config(bg="red",fg="pink")
entry_name=Entry()
entry_name.place(x=150,y=50,width=200,height=30)
lable_name= Label(text="Enter your name: ")
lable_name.place(x=40,y=50,width=100,height=30)
but_name=Button(text="Click Here",command=name)
but_name.place(x=50, y=90,width=80,height=30)
windown.mainloop()



