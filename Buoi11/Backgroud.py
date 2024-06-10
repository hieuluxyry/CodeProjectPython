from tkinter import *
def change_bg():
    color = color_var.get()
    window.config(bg=color)
def on_click():
    print("Button clicked!")
window = Tk()
window.title("Background")
window.config(bg="blue")
color_var = StringVar(window)
color_var.set("Blue")
color_menu = OptionMenu(window, color_var, "Blue", "Red", "Green", "Yellow", command=lambda _: change_bg())
color_menu.pack(pady=20)
action_button = Button(window, text="Click to do", command=on_click)
action_button.pack(pady=20)
window.mainloop()