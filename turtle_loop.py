#May 20 2020
#5.5. Repetition with a For Loop

#Python Basics - University of Michigan

import turtle

wn = turtle.Screen()

elan = turtle.Turtle()
elan.speed(3)

claire = turtle.Turtle()
claire.color("Hotpink")
claire.pensize(5)
claire.speed(5)

            

distance = 50
for i in range(10):
    elan.forward(distance)
    elan.right(90)
    distance = distance + 10

for i2 in range(20):
    claire.left(90)
    claire.forward(distance)
    distance = distance + 15
