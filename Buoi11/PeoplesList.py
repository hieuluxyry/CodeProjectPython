from tkinter import *
from tkinter import messagebox

# Create the main window
window = Tk()
window.title("People List")
def add_to_list():
    name = name_entry.get().strip()
    gender = gender_var.get()
    if name and gender:
        entry = f"{name}, {gender}"
        people_list.insert(END, entry)
        try:
            with open("people_list.txt", "a") as file:
                file.write(entry + "\n")
            name_entry.delete(0, END)
            gender_var.set("M")
            messagebox.showinfo("Success", f"{entry} added to the list.")
        except IOError:
            messagebox.showerror("Error", "Unable to write to file.")
    else:
        messagebox.showwarning("Input Error", "Please enter both name and gender.")
def display_file_contents():
    try:
        with open("people_list.txt", "r") as file:
            contents = file.read()
            print("People list:\n", contents)
            messagebox.showinfo("File Contents", contents)
    except IOError:
        messagebox.showerror("Error", "Unable to read file.")
name_label = Label(window, text="Nhập tên của bạn:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)
gender_label = Label(window, text="Giới tính:")
gender_label.grid(row=1, column=0, padx=10, pady=10)
gender_var = StringVar(window)
gender_var.set("M")
gender_menu = OptionMenu(window, gender_var, "M", "F")
gender_menu.grid(row=1, column=1, padx=10, pady=10)
people_list = Listbox(window)
people_list.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
add_button = Button(window, text="Thêm vào danh sách", command=add_to_list)
add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
display_button = Button(window, text="In file", command=display_file_contents)
display_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
# Start the Tkinter event loop
window.mainloop()
