from turtle import Screen, Turtle
window = Screen()
control = Turtle()
control.speed(100)
# Vẽ thân xe
control.penup()
control.goto(0, 0)
control.color("green")
control.begin_fill()
for _ in range(2):
    control.forward(200)
    control.left(90)
    control.forward(100)
    control.left(90)
control.end_fill()
control.penup()
control.goto(200, 1)
control.pendown()
control.setheading(0)
control.color("green")
control.begin_fill()
for _ in range(4):
    control.forward(50)
    control.left(90)
control.end_fill()
# Vị trí bánh xe thứ nhất
control.penup()
control.goto(50, -40)
control.pendown()
# Vẽ bánh xe thứ nhất
control.color("blue")
control.begin_fill()
control.circle(20)
control.end_fill()
control.penup()
control.goto(50, -30)
control.pendown()
control.color("white")  # Màu của vòng giữa
control.begin_fill()
control.circle(10)
control.end_fill()
# Vị trí bánh xe thứ hai
control.penup()
control.goto(150, -40)
control.pendown()
# Vẽ bánh xe thứ hai
control.begin_fill()
control.circle(20)
control.end_fill()
control.color("blue")
control.begin_fill()
control.circle(20)
control.end_fill()
control.penup()
control.goto(150, -30)
control.pendown()
control.color("white")  # Màu của vòng giữa
control.begin_fill()
control.circle(10)
control.end_fill()
# vẽ mũi tên thứ nhất
control.penup()
control.goto(45, 53)
control.pendown()
control.color("red")  # Chọn màu cho mũi tên
control.begin_fill()
control.setheading(45)
control.forward(30)
control.right(90)
control.forward(30)
control.end_fill()
control.penup()
control.goto(55, 40)
control.pendown()
control.setheading(0)
control.color("red")
control.begin_fill()
for _ in range(4):
    control.forward(20)
    control.left(90)
control.end_fill()
#vẽ mũi tên thứ hai
control.penup()
control.goto(30, 20)
control.color("red")
control.begin_fill()
for _ in range(2):
    control.forward(70)
    control.left(90)
    control.forward(30)
    control.left(90)
control.end_fill()
control.penup()
control.goto(139, 53)
control.pendown()
control.color("red")  # Chọn màu cho mũi tên
control.begin_fill()
control.setheading(45)
control.forward(30)
control.right(90)
control.forward(30)
control.end_fill()
#vẽ hình vuông
control.penup()
control.goto(150, 40)
control.pendown()
control.setheading(0)
control.color("red")
control.begin_fill()
for _ in range(4):
    control.forward(20)
    control.left(90)
control.end_fill()
control.penup()
control.goto(125, 20)
control.color("red")
control.begin_fill()
for _ in range(2):
    control.forward(70)
    control.left(90)
    control.forward(30)
    control.left(90)
control.end_fill()
#vẽ hình còn lại
control.penup()
control.goto(-250,-20)
control.pendown()
control.speed(100)
control.pensize(4)
control.pencolor("orange")
control.forward(100)
control.left(90)
control.forward(50)
control.right(90)
control.forward(20)
control.right(90)
control.forward(20)
control.left(125)
control.forward(50)
control.left(105)
control.forward(50)
control.left(130)
control.forward(20)
control.right(90)
control.forward(20)
control.right(90)
control.forward(50)
control.left(90)
control.forward(102)
control.left(90)
control.forward(120)
control.penup()
control.goto(-200,70)
control.pendown()
control.color("red")
control.begin_fill()
control.left(35)
control.forward(70)
control.right(125)
control.forward(70)
control.right(115)
control.forward(70)
control.end_fill()
control.hideturtle()
window.mainloop()