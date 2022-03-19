# import package and making object

#this program was made by Rhett Applestone, also known as @pxlp on ig
#it was adapted from a program found here https://www.geeksforgeeks.org/draw-ellipse-using-turtle-in-python/

import turtle
from tkinter import *

screen = turtle.Screen()


#make slider for speed
def show_values():
    print (w1.get())

master = Tk()
master.title("Speed")
w1 = Scale(master, from_=1, to=20, length=1200, orient = HORIZONTAL)
w1.set(5)
w1.pack()


# method to draw ellipse
def draw(rad):

  # rad --> radius for arc
    for i in range(2):
        turtle.circle(rad,90)
        turtle.circle(rad//5000,90)

# Main Section
# Set screen size
screen.setup(1600,1600)
screen.title("Ratioflower by Rhett Applestone")

# Set screen color
screen.bgcolor('white')

# Colors
col=['violet','blue','green','yellow',
     'orange','red']

# some integers
val=10
ind=0

# turtle speed
turtle.speed(w1.get())

# loop for multiple ellipse
for i in range(36000):

    # oriented the ellipse at angle = -val
    turtle.seth(-val)

    # color of ellipse
    turtle.color(col[ind])

    # to access different color
    if ind==5:
        ind=0
    else:
        ind+=1

    # calling method
    draw(400)

    # orientation change
    val+=137.5077664050037

    turtle.speed(w1.get())

# for hiding the turtle
turtle.hideturtle()
