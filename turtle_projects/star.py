import turtle as tur

ws = tur.Turtle()
 

color= ['yellow','orange','green','cyan','blue']
 
tur.pensize(4)
tur.title("star pattern")
tur.penup()
tur.setpos(-90,30)
tur.pendown()
tur.hideturtle()
for i in range(5):
    tur.pencolor(color[i])
    tur.forward(200)
    tur.right(144)
 
tur.penup()
tur.setpos(80,-140)
tur.pendown()
 

tur.pencolor("Black")
tur.done()