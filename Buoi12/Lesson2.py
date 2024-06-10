from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Bài 2")
window.geometry("1280x720")
def add_to_list():
    number = Enter_a_number_Entry.get()
    if number:
        List_Text.insert(END, number + "\n")
        Enter_a_number_Entry.delete(0, END)
    else:
        messagebox.showwarning("Input Error", "Please enter a number")
def clear_list():
    List_Text.delete(1.0, END)
def save_list():
    try:
        with open("list.txt", "w") as file:
            file.write(List_Text.get(1.0, END))
        messagebox.showinfo("Success", "List saved successfully")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save list: {str(e)}")

def open_picture(picture_name):
    try:
        img = PhotoImage(file=f"{picture_name}.png")
        picture_label.config(image=img)
        picture_label.image = img
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open image: {str(e)}")
def update_image(*args):
    person = select_face.get()
    image_path = people_images.get(person)
    if image_path:
        open_picture(image_path)
people_images = {
    "Tuyết": "Tuyet",
    "Quỳnh": "Quynh",
    "Trang": "Trang",
    "Dịu": "Diu",
    "Hiếu": "Hieu"
}
def Exit():
    window.quit()
Enter_a_number_Label = Label(window, text="Enter a number:")
Enter_a_number_Label.place(x=20, y=20, width=100, height=25)
Enter_a_number_Entry = Entry(window, font=("Times New Roman", 12))
Enter_a_number_Entry.place(x=130, y=20, width=200, height=25)
List_Label = Label(window, text="List:")
List_Label.place(x=20, y=50, width=100, height=25)
List_Text = Text(window, font=("Times New Roman", 12))
List_Text.place(x=130, y=50, width=200, height=100)
Add_a_list = Button(window, text="Add to list", command=add_to_list)
Add_a_list.place(x=350, y=20, width=75, height=25)
Clear_a_list = Button(window, text="Clear list", command=clear_list)
Clear_a_list.place(x=350, y=50, width=75, height=25)
Save_a_list = Button(window, text="Save list", command=save_list)
Save_a_list.place(x=350, y=80, width=75, height=25)
Exit = Button(window, text="Exit", command=Exit)
Exit.place(x=350, y=110, width=75, height=25)
Open_picture_Dog = Button(window, text="Open picture dog", command=lambda: open_picture("dog"))
Open_picture_Dog.place(x=20, y=160, width=100, height=25)
Open_picture_Cat = Button(window, text="Open picture cat", command=lambda: open_picture("cat"))
Open_picture_Cat.place(x=130, y=160, width=100, height=25)
Open_picture_fish = Button(window, text="Open picture fish", command=lambda: open_picture("fish"))
Open_picture_fish.place(x=240, y=160, width=100, height=25)
select_face = StringVar(window)
select_face.set("Chọn người: ")
list_menu = OptionMenu(window, select_face, *people_images.keys())
list_menu.place(x=350, y=160, width=120, height=25)
picture_label = Label(window, background="white")
picture_label.place(x=20, y=200, width=255, height=255)
select_face.trace("w", update_image)
window.mainloop()