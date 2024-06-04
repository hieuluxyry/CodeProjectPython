from tkinter import *
window = Tk()
window.geometry("500x500")
window.title("MilesTokKilo_KiloToMiles")
def miles_sang_kilo():
    km = 0
    entry_ip_number.get()
    km = float(entry_ip_number.get())*1.6093
    label_op_km = Label(text=f"{km}")
    label_op_km.place( x = 40, y = 200, width = 300, heigh = 25)
def kilo_sang_miles():
    miles = 0
    entry_ip_number.get()
    miles = float(entry_ip_number.get())*0.6214
    label_op_km = Label(text=f"{miles}")
    label_op_km.place(x=40, y=200, width=300, heigh=25)
lable_Ip = Label(text="Enter the value you want to convert: ")
lable_Ip.place(x = 40, y = 40, width = 300, height = 25)
entry_ip_number = Entry()
entry_ip_number.place(x = 40, y = 80 , width = 100, heigh = 25 )
button_miles = Button(text="Convert miles to kilomet",command=miles_sang_kilo)
button_miles.place( x = 40, y = 120, width = 300, heigh = 25)
button_km = Button(text="Convert km to miles",command=kilo_sang_miles)
button_km.place( x = 40, y = 160, width = 300, heigh = 25)
window.mainloop()