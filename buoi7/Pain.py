from turtle import *
windown = Screen()
control = Turtle()
control.color("orange", "red")
control.pensize(5)
control.penup()
control.goto(-100,0)
control.pendown()
control.begin_fill()
for i in range(4):
    control.fd(200)
    control.left(90)
control.end_fill()
control.penup()
control.goto(-50,50)
control.pendown()
control.color("orange", "white")
control.begin_fill()
for i in range(4):
    control.fd(100)
    control.left(90)
control.end_fill()
windown.mainloop()

