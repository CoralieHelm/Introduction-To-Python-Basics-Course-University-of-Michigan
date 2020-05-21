#My First Turtle Program
#Coursera - Python Basics - presented by University of Michigan


import turtle             # allows us to use the turtles library

background_color = input("Please, select a Background Color -> ")
turtle_color = input("Please, select the color of the Turtle -> ")
pensizing = input("Please, select the size of the Pen from 1 - 20 -> ")

wn = turtle.Screen()     # creates a graphics window
wn.bgcolor(background_color)

sam = turtle.Turtle()    # create a turtle named sam
sam.color(turtle_color)
sam.pensize(pensizing)

sam.forward(150)         # tell sam to move forward by 150 units
sam.left(90)             # turn by 90 degrees
sam.forward(75)          # complete the second side of a rectangle

wn.exitonclick()         # wait for a user click on the canvas
