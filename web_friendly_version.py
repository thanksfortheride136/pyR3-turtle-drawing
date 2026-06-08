# drawing.py
# ----------
# By: Louis Cooper
#
# Draws an animation in turtle.

import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Change these if you want to move the whole drawing
X_OFFSET = 350
Y_OFFSET = 0

# Utilizes x, y positions to move the turtle
def fly(x, y):
    t.penup()
    t.goto(x + X_OFFSET, y + Y_OFFSET)
    t.pendown()

# Sets initial position of the drawing
def starting_position():
    fly(-600, -300)

# Draws rectangle with optional rounded corners
def rectangle(length, height, corner_radius=0):
    for i in range(2):
        t.forward(length - 2 * corner_radius)

        if corner_radius:
            t.circle(corner_radius, 90)
        else:
            t.left(90)

        t.forward(height - 2 * corner_radius)

        if corner_radius:
            t.circle(corner_radius, 90)
        else:
            t.left(90)

# Draws a black background
def draw_background():
    t.fillcolor("black")
    t.begin_fill()
    rectangle(500, 600, 0)
    t.end_fill()

# Draws a TV
def draw_tv():
    # Outer border
    fly(-500, -200)
    t.fillcolor("#c7b199")
    t.begin_fill()
    rectangle(300, 210, 10)
    t.end_fill()

    # Antenna
    t.color("#C0C0C0")

    t.penup()
    t.goto(-350 + X_OFFSET, 10 + Y_OFFSET)
    t.pendown()
    t.setheading(30)
    t.forward(100)

    t.penup()
    t.goto(-350 + X_OFFSET, 10 + Y_OFFSET)
    t.pendown()
    t.setheading(150)
    t.forward(100)

    t.setheading(0)

    # Antenna base
    t.penup()
    t.goto(-360 + X_OFFSET, 0 + Y_OFFSET)
    t.pendown()
    t.fillcolor("#C0C0C0")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.color("black")

    # Inner screen border
    t.fillcolor("#1a1a1a")
    fly(-490, -186)
    t.begin_fill()
    rectangle(200, 180, 5)
    t.end_fill()

    # Inner screen
    fly(-480, -175)
    t.fillcolor("black")
    t.begin_fill()
    rectangle(180, 158, 5)
    t.end_fill()

    # Side panel
    fly(-270, -185)
    t.fillcolor("#1a1a1a")
    t.begin_fill()
    rectangle(50, 180, 5)
    t.end_fill()

    # Side panel internal panel
    fly(-265, -120)
    t.fillcolor("#514640")
    t.begin_fill()
    rectangle(40, 110, 5)
    t.end_fill()

    # Dial 1
    fly(-250, -100)
    t.fillcolor("#484848")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.fillcolor("#1a1a1a")
    t.begin_fill()
    t.left(15)
    rectangle(4, 29)
    t.right(15)
    t.end_fill()

    # Dial 2
    fly(-250, -60)
    t.fillcolor("#484848")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.fillcolor("#1a1a1a")
    t.begin_fill()
    t.left(5)
    rectangle(4, 29)
    t.right(5)
    t.end_fill()

    # Grill adornments
    fly(-260, -115)
    t.fillcolor("#c7b199")
    t.begin_fill()
    t.circle(4)
    t.end_fill()

    fly(-240, -115)
    t.fillcolor("#c7b199")
    t.begin_fill()
    t.circle(4)
    t.end_fill()

    # Grill
    t.fillcolor("#c7b199")
    for j in range(12):
        fly(-270, -130 - (j * 5))
        t.begin_fill()
        rectangle(40, 4)
        t.end_fill()

    # Feet
    t.fillcolor("tan")

    fly(-495, -200)
    t.begin_fill()
    rectangle(14, -50)
    t.end_fill()

    fly(-240, -200)
    t.begin_fill()
    rectangle(14, -50)
    t.end_fill()

# Instructional text
def instructions_text():
    fly(-540, -260)
    t.color("white")
    t.write("Click the dials to change the channel", font=("Verdana", 15, "normal"))
    t.color("black")

# Changes the TV screen color
def next_screen():
    screen_colors = [
        "white", "black", "red", "green", "blue", "cyan", "yellow", "magenta",
        "orange", "purple", "pink", "brown", "grey", "gold", "lime", "teal",
        "lavender", "turquoise", "tan", "salmon", "olive", "maroon",
        "navy", "aquamarine", "violet", "silver", "plum", "orchid",
        "indigo", "fuchsia", "crimson", "coral", "chocolate", "chartreuse",
        "azure"
    ]

    fly(-480, -175)
    t.fillcolor(random.choice(screen_colors))
    t.setheading(0)
    t.begin_fill()
    rectangle(180, 158, 5)
    t.end_fill()

# Checks for clicks inside the dials
def detect_circle_click(x_pos, y_pos):
    left_dial_boundary = -266 + X_OFFSET
    right_dial_boundary = -235 + X_OFFSET

    top_dial_top = -45 + Y_OFFSET
    top_dial_bottom = -75 + Y_OFFSET

    bottom_dial_top = -85 + Y_OFFSET
    bottom_dial_bottom = -115 + Y_OFFSET

    clicked_top_dial = (
        x_pos > left_dial_boundary and
        x_pos < right_dial_boundary and
        y_pos < top_dial_top and
        y_pos > top_dial_bottom
    )

    clicked_bottom_dial = (
        x_pos > left_dial_boundary and
        x_pos < right_dial_boundary and
        y_pos < bottom_dial_top and
        y_pos > bottom_dial_bottom
    )

    if clicked_top_dial or clicked_bottom_dial:
        next_screen()

# Main program
starting_position()
draw_background()
draw_tv()
instructions_text()

# Click listener
# If the sandbox supports clicks, uncomment this:
# turtle.onscreenclick(detect_circle_click)

turtle.done()
