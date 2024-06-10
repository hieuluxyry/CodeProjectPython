import tkinter as tk
from tkinter import messagebox
import random
window = tk.Tk()
window.title("Math Quiz")
window.geometry("400x300")
def generate_question():
    global num1, num2
    num1 = random.randint(10, 50)
    num2 = random.randint(10, 50)
    question_label.config(text=f"Sum is {num1} + {num2}?")
    entry_answer.delete(0, tk.END)
    result_label.config(image='')
def check_answer():
    try:
        user_answer = int(entry_answer.get())
        if user_answer == (num1 + num2):
            result_label.config(image=tick_img)
            messagebox.showinfo("Correct", "Well done! You got it right!")
        else:
            result_label.config(image=cross_img)
            messagebox.showerror("Incorrect", f"Sorry, the correct answer was {num1 + num2}.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
tick_img = tk.PhotoImage(file="tick.png")
cross_img = tk.PhotoImage(file="error.png")
question_label = tk.Label(window, text="", font=("Time New Roman", 20))
question_label.pack(pady=20)
entry_answer = tk.Entry(window, font=("Time New Roman", 20))
entry_answer.pack(pady=10)
submit_button = tk.Button(window, text="Submit", command=check_answer, font=("Arial", 16),bg="red")
submit_button.pack(pady=10)
result_label = tk.Label(window, text="", font=("Time New Roman", 16))
result_label.pack(pady=20)
next_button = tk.Button(window, text="Next", command=generate_question, font=("Arial", 16),bg="pink")
next_button.pack(pady=10)
generate_question()
window.mainloop()