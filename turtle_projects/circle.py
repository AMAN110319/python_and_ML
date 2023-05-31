import turtle
cr = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("CIRCLE")
cr.color("white")

cr.begin_fill()

cr.up()
cr.goto(100,200)
cr.down()

cr.fillcolor("red")
cr.circle(20)  # anticlock-wise movement of turtle object
cr.circle(-50) # clockwise movement of turtle object

cr.end_fill()