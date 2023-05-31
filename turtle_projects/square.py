import turtle
aman = turtle.Turtle()
aman.speed(1)
aman.color("white")
aman.shape("turtle")
# aman.hideturtle()
wn = turtle.Screen()
wn.bgcolor("black")
aman.begin_fill()
aman.fillcolor("red")
for i in range(4):
    aman.forward(200)
    aman.left(90)
aman.end_fill()