# drawing.py
# ----------
# By: Louis Cooper
#
# Draws an animation in turtle.

from http.client import RemoteDisconnected
from turtle import *
import random

pensize(2) #Sets line width for drawing.

#Utlizes x, y positions to move the turtle
def fly(x, y): 
    penup()
    goto(x, y)
    pendown()

#sets initial position of the drawing. See fly()
def starting_position(): 
    penup()
    fly(-600, -300)
    pendown()

starting_position()

#draws rectange with height / width parameter. There is an optional parameter for corner radius. If corner radius is true then the corners are rounded by 3rd argument value, subtracted from length to maintain consistency.
def rectangle(length, height, corner_radius=0):
    for i in range(2):
        forward(length - 2 * corner_radius)
        if corner_radius:
            circle(corner_radius, 90)
        else:
            left(90)
        forward(height - 2 * corner_radius)
        if corner_radius:
            circle(corner_radius, 90)
        else:
            left(90)

#Draws a black background
def draw_background():
    speed(0)
    fillcolor("black")
    begin_fill()
    rectangle(500, 600, 0)
    end_fill()
    
draw_background()

#draws a TV
def draw_tv():
    #outer border
    fly(-500, -200)
    fillcolor("#c7b199")
    begin_fill()
    rectangle(300, 210, 10)
    end_fill()
    #Antenna
    color("#C0C0C0")
    pensize(5)
    penup()
    goto(-350, 10) 
    pendown()
    setheading(30) 
    forward(100)
    penup()
    goto(-350, 10) 
    pendown()
    setheading(150)
    forward(100)
    pensize(2)
    setheading(0) 
    #Antenna Base
    penup()
    goto(-360, 0) 
    pendown()
    fillcolor('#C0C0C0')
    begin_fill()
    circle(10)
    end_fill()
    color("black")
  
    #inner screen border
    fillcolor('#1a1a1a')
    fly(-490, -186)
    begin_fill()
    rectangle(200, 180, 5)
    end_fill()
    #inner screen
    fly(-480, -175)
    fillcolor("black")
    begin_fill()
    rectangle(180, 158, 5)
    end_fill()
    #side panel
    fly(-270, -185)
    fillcolor('#1a1a1a')
    begin_fill()
    rectangle(50, 180, 5)
    end_fill()
    #side Panel internal Panel
    fly(-265, -120)
    fillcolor("#514640")
    begin_fill()
    rectangle(40, 110, 5)
    end_fill()
    #dial1
    fly(-250, -100)
    fillcolor("#484848")
    begin_fill()
    circle(15)
    end_fill()
    fillcolor('#1a1a1a')
    begin_fill()
    left(15)
    rectangle(4, 29)
    right(15)
    end_fill()
    #dial2
    fly(-250, -60)
    fillcolor("#484848")
    begin_fill()
    circle(15)
    end_fill()
    fillcolor('#1a1a1a')
    begin_fill()
    left(5)
    rectangle(4, 29)
    right(5)
    end_fill()
    #grill adornments
    fly(-260, -115)
    fillcolor("#c7b199")
    begin_fill()
    circle(4)
    fly(-240, -115)
    fillcolor("#c7b199")
    circle(4)
    end_fill()
    #grill
    fillcolor("#c7b199")
    fly(-270, -130)
    for j in range(12):
        begin_fill()
        rectangle(40, 4)
        end_fill()
        fly(-270, -130 - (j*5))
    #Feet
    fillcolor("tan")
    fly(-495, -200)
    begin_fill()
    rectangle(14, -50)
    end_fill()
    fly(-240, -200)
    begin_fill()
    rectangle(14, -50)
    end_fill()
    
draw_tv()

#Instructional Text
def instructions_text():
    fly(-540, -290)
    color("white")
    write("Click the dials to change the channel", font=("Verdana", 15, "normal"))
    color("black")

instructions_text()

#Checks for clicks inside the round dials. Utilizes conditionals to create a button like onbject to "click" on.
def detect_circle_click(x_pos, y_pos):
    top_dial_boundry_top = -30.0
    top_dial_boundry_bottom = -95.0
    left_dial_boundry = -266.0
    right_dial_boundry = -235.0
    bottom_dial_boundry_top = -70.0
    bottom_dial_boundary_bottom = -99.0
    if x_pos > left_dial_boundry and x_pos < right_dial_boundry and y_pos < top_dial_boundry_top and y_pos > top_dial_boundry_bottom :   #These are registering as one button, whhy, it doesnt matter for this use case but I should fix
        next_screen()
    elif x_pos > left_dial_boundry and x_pos < right_dial_boundry and y_pos < bottom_dial_boundry_top and y_pos > bottom_dial_boundary_bottom:
        next_screen()
onscreenclick(detect_circle_click)

#Selects from a random list of colors to change the screen to.
def next_screen():
    hideturtle()
    screen_colors = ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta', 
              'orange', 'purple', 'pink', 'brown', 'grey', 'gold', 'lime', 'teal', 
              'lavender', 'turquoise', 'tan', 'sky blue', 'salmon', 'olive', 'maroon', 
              'navy', 'aquamarine', 'violet', 'silver', 'plum', 'peach puff', 'orchid', 
              'midnight blue', 'indigo', 'honeydew', 'ghost white', 'fuchsia', 
              'dark violet', 'dark turquoise', 'dark salmon', 'dark red', 'dark orchid', 
              'dark orange', 'dark olive green', 'dark khaki', 'dark goldenrod', 
              'dark cyan', 'dark blue', 'crimson', 'coral', 'chocolate', 'chartreuse', 
              'cadet blue', 'azure', 'aquamarine', 'antique white', 'alice blue']
    fly(-480, -175)
    fillcolor(random.choice(screen_colors))
    setheading(0)
    begin_fill()
    rectangle(180, 158, 5)
    end_fill()

mainloop() 
done() #prevents window from closing