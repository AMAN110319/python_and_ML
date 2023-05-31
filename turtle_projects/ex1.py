import turtle

def drawcircle(color,x,y,radius):
    ex.up()
    ex.home()# for going to the home position
    ex.begin_fill()
    ex.goto(x,y)
    ex.down()
    ex.fillcolor(color)
    ex.circle(radius)
    ex.end_fill()
    
    
ex = turtle.Turtle()


ex.up()
ex.begin_fill()
ex.goto(0,-50)
ex.down()
ex.fillcolor("green")
ex.circle(50)
ex.end_fill()
ex.up()
ex.home()

drawcircle('navy',200,200,50)
drawcircle('red',-200,200,-50)
drawcircle('orange',-200,-200,-50)
drawcircle('purple',200,-200,50)