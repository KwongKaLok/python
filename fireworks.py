# fireworks

import random  # module providing the randint function
import time  # time module to delay after drawing five fireworks
import turtle  # turtle module for drawing fireworks
import playsound

#### Initialize variables used in the program

# The following width and height match the GIF used by the program
screen_width, screen_height = 900, 564

firework_radius = 100  # The maximum radius a firework can have
firework_count = 30  # The number of fireworks to shoot

# A list of colours to choose from for a firework
firework_colours = ["red", "orange", "yellow", "green", "cyan", "blue", "violet"]

#### Initialize the turtle module

turtle.reset()  # Reset the turtle
turtle.setup(screen_width, screen_height)  # Set the size of the screen
turtle.bgpic("hong_kong.gif")  # Put the background image on the
# screen
turtle.width(3)  # Draw lines with a width of three
turtle.shape("circle")  # Set the turtle to be bomb shape
turtle.color("red")  # Set the turtle color to red
turtle.up()
turtle.speed(9)

#### For loop to shoot individual firework

for i in range(firework_count):
    # Clear the sky (screen) for every five fireworks
    if i > 0 and i % 5 == 0:
        time.sleep(1)
        turtle.clear()

    #### Add your code here
    # Initialize a starting position
    startx = random.randint(-screen_width / 2, screen_width / 2)
    starty = -screen_height / 2
    # Initialize a destination
    destx = random.randint(-screen_width / 2, screen_width / 2)
    desty = random.randint(0, screen_height / 2)
    # Shoot a firework from the start to the destination
    turtle.hideturtle()

    turtle.goto(startx, starty)
    turtle.showturtle()
    turtle.goto(destx, desty)
    playsound.play("explosion.wav")

    #### The turtle is in the sky, explode the firework

    #### Add your code here
    # Pick a firework color from the firework colour list
    # or can use this code to choose color              firework_colours = random,choice(firework_colours )
    color = firework_colours[random.randint(0, len(firework_colours) - 1)]
    turtle.color(color)
    # Pick a size for the firework
    size = random.randint(firework_radius / 2, firework_radius)
    # Pick the number of explosion directions
    no_of_direction = random.randint(10, 20)

    #### For loop to draw each ring of explosion
    turtle.tracer(False)

    for radius in range(10, size, 10):
        #### Add your code here
        turtle.setheading(0)
        turtle.forward(radius)
        turtle.left(90)

        for direction in range(no_of_direction):
            turtle.dot((radius / 10) % size)
            turtle.circle(radius, 360 / no_of_direction)
        turtle.left(90)
        turtle.forward(radius)
        turtle.left(90)
        turtle.forward(4)
    turtle.hideturtle()
    turtle.tracer(True)

turtle.done()  # Need to keep the window display up
