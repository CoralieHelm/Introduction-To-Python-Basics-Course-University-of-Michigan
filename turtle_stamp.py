#May 20 2020
#5.6. A Few More turtle Methods and Observations

#Python Basics - University of Michigan

import turtle

wn = turtle.Screen()
wn.bgcolor("darkblue")

tess = turtle.Turtle()
tess.color("white")
tess.shape("turtle")
tess.speed(3)

dist = 5
tess.up()

for i in range(30):
    tess.stamp()
    tess.forward(dist)
    tess.right(24)
    dist += 5

tess.color("red")
wn.exitonclick()
