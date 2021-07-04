import turtle
import random

nol = 0
turtle.width(5)
turtle.speed(0)
colorlist = ["orange red", "deep sky blue", "magenta", "yellow", "green", "cyan", "hot pink"]
while nol < 20:
    radius = random.randint(5, 50)
    xaxis = random.randint(-300, 300)
    yaxis = random.randint(-300, 300)
    color1 = random.choice(colorlist)
    color2 = random.choice(colorlist)
    turtle.color(color1, color2)
    turtle.begin_fill()
    turtle.up()
    turtle.goto(xaxis, yaxis)
    turtle.down()
    turtle.circle(radius)
    nol = nol + 1
    turtle.end_fill()

turtle.done()
