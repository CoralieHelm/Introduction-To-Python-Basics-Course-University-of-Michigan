#May 23 2020
#Drawing Exercise using Turtle
#Using Functions learned from previous courses

import turtle

def window_screen():
    window = input("Please, select the Background Color of the Window -> ")
    wn = turtle.Screen()
    wn.bgcolor(window)
    
def window_exit():
    wn = turtle.Screen()
    wn.exitonclick()

window_screen()


def rectangle_shape():
    reg_color = input("Please, select the Color of the Rectangle -> ")
    reg_size = input("Please, select the Pen Size of the Rectangle from 1 - 10 -> ")


    rectangle = turtle.Turtle()
    rectangle.color(reg_color)
    rectangle.pensize(reg_size)

    for i in range(2):

        rectangle.forward(100)
        rectangle.left(90)
        rectangle.forward(50)
        rectangle.left(90)
   

#rectangle_shape()


def triangle_shape():
    tri_color = input("Please, select the Color of the Triangle -> ")
    tri_size = input("Please, select the Pen Size of the Triangle from 1 - 10 -> ")
    tri_speed = input("Please, select the Speed of the Drawing from 1 - 8 -> ")

    triangle = turtle.Turtle()
    triangle.color(tri_color)
    triangle.pensize(tri_size)
    triangle.speed(int(tri_speed))

    for t in range(4):
        triangle.forward(250)
        triangle.left(120)

triangle_shape()

def shape_1():
    new_shape = turtle.Turtle()
    new_shape.color("red")
    new_shape.pensize(5)
    new_shape.shape("turtle")

    new_shape.left(60)
    new_shape.forward(200)
    new_shape.left(60)
    new_shape.forward(200)
    new_shape.left(60)
    new_shape.forward(200)
    new_shape.left(60)
    new_shape.forward(200)
    new_shape.left(60)
    new_shape.forward(200)
    new_shape.left(60)
    new_shape.forward(200)

window_exit()
