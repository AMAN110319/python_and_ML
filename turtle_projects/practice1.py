import turtle
b = turtle.Turtle()
b.color('red','yellow')
b.speed(10)
b.begin_fill()
for i in range(100):
    b.forward(300)
    b.left(168.5)
b.end_fill()
turtle.done()
