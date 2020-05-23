#May 20 2020
#5.5. Repetition with a For Loop

#Python Basics - University of Michigan

import turtle

wn = turtle.Screen()
wn.bgcolor("darkblue")

elan = turtle.Turtle()
elan.pensize(3)
elan.speed(3)

claire = turtle.Turtle()
claire.color("Hotpink")
claire.pensize(5)
claire.speed(5)

color_turtle = turtle.Turtle()
color_turtle.pensize(8)
c_distance = 35




distance = 50
for i in range(10):
    elan.forward(distance)
    elan.right(90)
    distance = distance + 10

for aColor in ["yellow", "pink", "blue", "green"]:
    color_turtle.color(aColor)
    color_turtle.left(90)
    color_turtle.forward(c_distance)
    distance = distance + 15

for i2 in range(20):
    claire.left(90)
    claire.forward(distance)
    distance = distance + 15
