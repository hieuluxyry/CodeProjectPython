from turtle import *
window = Screen()
window.bgcolor("lightblue")
nha = Turtle()
nha.speed(900)
# Ve than nha
nha.begin_fill()
nha.color("pink")
nha.forward(100)
nha.left(90)
nha.forward(80)
nha.left(90)
nha.forward(200)
nha.left(90)
nha.forward(80)
nha.left(90)
nha.forward(100)
nha.end_fill()
# ve cua so 1
nha.penup()
nha.goto(-80, 40)
nha.pendown()
nha.color("black", "green")
nha.begin_fill()
for i in range(4):
    nha.fd(20)
    nha.left(90)
nha.end_fill()
# ve cua so 2
nha.penup()
nha.goto(60, 40)
nha.pendown()
nha.color("black", "green")
nha.begin_fill()
for i in range(4):
    nha.fd(20)
    nha.left(90)
nha.end_fill()
# ve cua dai
nha.penup()
nha.goto(-20, 0)
nha.pendown()
nha.color("black", "red")
nha.begin_fill()
for i in range(4):
    nha.fd(40)
    nha.left(90)
nha.end_fill()
nha.hideturtle()
# ve mat troi
sum = Turtle()
sum.penup()
sum.goto(-100, 80)
sum.pendown()
sum.color("yellow", "yellow")
sum.begin_fill()
sum.forward(200)
sum.right(35)
sum.backward(122)
sum.right(110)
sum.forward(122)
sum.end_fill()
# ve mat troi
sum.penup()
sum.goto(300, 300)
sum.pendown()
sum.color("yellow")
sum.begin_fill()
for _ in range(36):  # Vẽ cánh hoa
    sum.forward(100)
    sum.left(170)
sum.end_fill()
sum.hideturtle()
# sông
song = Turtle()
song.penup()
song.goto(600, 400)
song.pendown()
song.pensize(250)
song.color("blue")
song.setheading(0)
song.right(90)
song.forward(40)
song.circle(320, 40)
song.circle(-320, 80)
song.circle(320, 40)# sông
song.penup()
song.goto(600, 400)
song.pendown()
song.pensize(250)
song.color("blue")
song.setheading(0)
song.right(90)
song.forward(40)
song.circle(320, 40)
song.circle(-320, 80)
song.circle(320, 40)
#đám mây
cloud = Turtle()
cloud.penup()
cloud.goto(30, 260)
cloud.pendown()
cloud.color("white")
cloud.begin_fill()
cloud.circle(17)
cloud.end_fill()
cloud.penup()
cloud.goto(50, 270)
cloud.pendown()
cloud.color("white")
cloud.begin_fill()
cloud.circle(22)
cloud.end_fill()

cloud.penup()
cloud.goto(70, 262)
cloud.pendown()
cloud.color("white")
cloud.begin_fill()
cloud.circle(23)
cloud.end_fill()

cloud.penup()
cloud.goto(96, 258)
cloud.pendown()
cloud.color("white")
cloud.begin_fill()
cloud.circle(25)
cloud.end_fill()
cloud.penup()
cloud.goto(117, 267)
cloud.pendown()
cloud.color("white")
cloud.begin_fill()
cloud.circle(23)
cloud.end_fill()
cloud.hideturtle()
window.mainloop()