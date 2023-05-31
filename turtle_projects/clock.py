import turtle
t = turtle.Turtle()
turtle.title("clock")
t.write((0,0))
t.up()
t.goto(0,-100)
t.down()
t.circle(100)

t.up()
t.home() 
t.goto(0,-60)
t.down()
t.circle(60)
t.home()
t.left(90)
for i in range(12):
    

turtle.done()# for retaining the turtle 
