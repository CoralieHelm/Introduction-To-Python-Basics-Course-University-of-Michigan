#May 20 2020

#5.3. Instances: A Herd of Turtles
#Python Basics - University of Michigan


import turtle
wn = turtle.Screen()
wn.bgcolor("Navy")

tess = turtle.Turtle()
tess.color("white")
tess.pensize("5")

sam = turtle.Turtle()
sam.color("Hotpink")
sam.pensize(3)

tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(180)
tess.forward(180)

sam.forward(50)
sam.left(90)
sam.forward(50)
sam.left(90)
sam.forward(50)
sam.left(90)
sam.forward(50)
sam.left(90)

wn.exitonclick()
