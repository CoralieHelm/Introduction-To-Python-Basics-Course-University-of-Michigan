#May 24 2020
#8.1. Intro: What we can do with Turtles and Conditionals
#Below is my own code based on 8.1 Intro to Conditionals


import turtle

wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("8.1. Intro: What we can do with Turtles and Conditionals")

turtle_colors = ["Beige","Blue", "Brown", "Coral", "Cyan", "Green", "Grey", "Lavender", "Lime", "Magenta", "Maroon","Navy", "Olive", "Orange", "Pink", "Purple", "Red", "Teal", "White", "Yellow"]
turtle_pen_size = input("Please, select the pensize of the Turtle Instance -> ")


adam = turtle.Turtle()
adam.pencolor("Pink")
adam.pensize(turtle_pen_size)
adam.right(45)
adam.shape("turtle")


for color in turtle_colors:
    if adam.pencolor() == "Purple" or adam.pencolor() == "Grey":
        adam.stamp()
        adam.forward(60)
        adam.right(50)
    elif adam.pencolor() == "Yellow" or adam.pencolor() == "Blue":
        adam.forward(65)
        adam.left(98)
    elif adam.pencolor() == "Orange" or adam.pencolor() == "White":
        adam.forward(90)
        adam.left(60)
    elif adam.pencolor() == "Pink":
        adam.forward(50)
        adam.right(57)
    elif adam.pencolor() == "Green":
        adam.forward(75)
        adam.left(90)
    elif adam.pencolor() == "Red":
        adam.right(90)
        adam.forward(45)
    elif adam.pencolor() == "Brown" or adam.pencolor() == "Lavender":
        adam.right(30)
        adam.forward(50)
    else:
        adam.forward(95)
        adam.right(60)

    adam.pencolor(color)

        










wn.exitonclick()
