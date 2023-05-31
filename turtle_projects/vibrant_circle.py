import turtle
t=turtle.Turtle()
s = turtle.Screen()
s.title('vibrant circle')
s.bgcolor('black')
t.color('green')
a=0
b=0
t.up()
t.speed(0)
t.goto(0,200)
t.down()
while(True):
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    t.hideturtle()

turtle.done()
