from turtle import *
window = Screen()
heart = Turtle()
heart.speed(50000)
pensize(15)
heart.color("red","red")
heart.begin_fill()
heart.left(140)
heart.forward(230)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.left(120)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.forward(230)
heart.end_fill()
heart.penup()
heart.goto(220, 0)
heart.pendown()
heart.color("red", "red")
heart.begin_fill()
heart.left(45+95)
heart.left(140)
heart.forward(230)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.left(120)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.forward(230)
heart.end_fill()
heart.end_fill()
heart.hideturtle()
window.mainloop()