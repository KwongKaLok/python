# Done by Kwong Ka Lok SID:20772439
import turtle

turtle.setup(800, 600)  # Set the width and height be 800 x 600
number_of_divisions = 8  # The number of subdivisions around the centre
turtle_width = 3  # The width of the turtles
# Don't show the animation
turtle.tracer(False)
# Draw the background lines
backgroundTurtle = turtle.Turtle()
backgroundTurtle.width(1)
backgroundTurtle.down()
backgroundTurtle.color("gray88")  # Draw the centered line
for i in range(number_of_divisions):
    backgroundTurtle.forward(500)
    backgroundTurtle.backward(500)
    backgroundTurtle.left(360 / number_of_divisions)
backgroundTurtle.up()
# Show the instructions
backgroundTurtle.color("purple")
backgroundTurtle.goto(-turtle.window_width() / 2 + 50, 100)
backgroundTurtle.write("""s - change a colour for one of the colour buttons
m - all 8 drawing turtles go to middle
c - clear all drawings made by the 8 drawing turtles
""", font=("Arial", 14, "normal"))
backgroundTurtle.hideturtle()
# Set up a turtle for handling message on the turtle screen
messageTurtle = turtle.Turtle()
# This sets the colour of the text to red
messageTurtle.color("red")
# We do not want it to show/draw anything, except the message text
messageTurtle.up()
# Set it the be at center, near the colour selections
messageTurtle.goto(-95, -200)
# We do not want to show it on the screen
messageTurtle.hideturtle()
# Part 2 Preparing the drawing turtles
# The drawing turtles are put in a list
allDrawingTurtles = []
# Part 2.1 Add the 8 turtles in the list
for i in range(number_of_divisions):
    newTurtle = turtle.Turtle()
    newTurtle.speed(0)
    newTurtle.width(turtle_width)
    newTurtle.hideturtle()

    allDrawingTurtles.append(newTurtle)
# Part 2.2 Set up the first turtle for drawing
dragTurtle = allDrawingTurtles[0]
dragTurtle.showturtle()
dragTurtle.shape("circle")
dragTurtle.shapesize(2, 2)


# Part 3 Preparing the basic drawing system
# Set up the ondrag event
def draw(x, y):
    dragTurtle.ondrag(None)
    turtle.tracer(False)
    dragTurtle.goto(x, y)
    x_transform = [1, 1, -1, -1, 1, 1, -1, -1]
    y_transform = [1, -1, 1, -1, 1, -1, 1, -1]
    for i in range(1, number_of_divisions):
        if i < 4:
            new_x = x * x_transform[i]
            new_y = y * y_transform[i]
        else:
            new_x = y * y_transform[i]
            new_y = x * x_transform[i]
        allDrawingTurtles[i].goto(new_x, new_y)
    turtle.tracer(True)
    dragTurtle.ondrag(draw)


dragTurtle.ondrag(draw)


# Part 5.2 clear all drawings made by the 8 drawing turtles
def clearDrawing():
    turtle.tracer(False)
    for drawingturtle in allDrawingTurtles:
        drawingturtle.clear()
    messageTurtle.clear()
    messageTurtle.write("The screen is cleared", font=("Arial", 14, "normal"))
    turtle.tracer(True)


turtle.onkeypress(clearDrawing, 'c')


# Part 5.3 all 8 drawing turtles go to middle
def goToMiddle():
    turtle.tracer(False)
    for movingturtle in allDrawingTurtles:
        movingturtle.up()
        movingturtle.goto(0, 0)
        movingturtle.down()
    messageTurtle.clear()
    messageTurtle.write("All 8 turtles returned to middle", font=("Arial", 14, "normal"))
    turtle.tracer(True)


turtle.onkeypress(goToMiddle, 'm')
# Part 4 handling the colour selection
# Make the colour selection turtles
# Here is the list of colours
colours = ["black", "orange red", "lawn green", "medium purple", "light sky blue", "orchid", "gold"]


# Part 4.2 Set up the onclick event
def handleColourChange(x, y):
    if x <= -130:
        for thisturtle in allDrawingTurtles:
            thisturtle.color(colours[0])
    elif x <= -80:
        for thisturtle in allDrawingTurtles:
            thisturtle.color(colours[1])
    elif x <= -30:
        for thisturtle in allDrawingTurtles:
            thisturtle.color(colours[2])
    elif x <= 20:
        for thisturtle in allDrawingTurtles:
            thisturtle.color(colours[3])
    elif x <= 70:
        for thisturtle in allDrawingTurtles:
            thisturtle.color(colours[4])
    elif x <= 120:
        for thisturtle in allDrawingTurtles:
            thisturtle.color(colours[5])
    elif x <= 170:
        for thisturtle in allDrawingTurtles:
            thisturtle.color(colours[6])


# Part 5.4 change a colour in the colour selection
def changeColour():
    a_list = ["0", "1", "2", "3", "4", "5", "6"]
    index = turtle.textinput("Change color", "Please type the index number for the turtle: (0-6)")
    if index != None:
        while index not in a_list:
            index = turtle.textinput("Change color", "Please enter a correct index number: (0-6)")
            if index == None:
                turtle.listen()
                return
    if index == None:
        turtle.listen()
        return
    changingcolor = turtle.textinput("Change color", "Please type the color you want to use e.g.LightBlue2:")
    if changingcolor != None:
        turtle.tracer(False)
        colours[int(index)] = changingcolor
        colourSelectionTurtles[int(index)] = colourSelectionTurtles[int(index)].color(colours[int(index)])
        messageTurtle.clear()
        messageTurtle.goto(-300, -200)
        messageTurtle.write("The colour for that button has been changed, click on the button to use it ",
                            font=("Arial", 14, "normal"))
        turtle.listen()
        turtle.tracer(True)
    elif changingcolor == None:
        turtle.listen()
        return


turtle.onkeypress(changeColour, "s")
# Part 4.1 Make the colour selection turtles
colourSelectionTurtles = []
for i in range(len(colours)):
    t = turtle.Turtle()
    t.shape("square")
    t.shapesize(2, 2)
    t.up()
    t.color(colours[i])
    t.goto(-150 + 50 * i, -250)
    t.onclick(handleColourChange)
    colourSelectionTurtles.append(t)
turtle.tracer(True)
turtle.listen()
turtle.done()
