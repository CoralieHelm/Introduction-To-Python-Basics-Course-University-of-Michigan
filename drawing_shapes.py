#May 23 2020
#Drawing Exercise using Turtle
#Using Functions learned from previous courses

import turtle

def window_screen():
    window = input("Please, select the Background Color of the Window -> ")
    wn = turtle.Screen()
    wn.bgcolor(window)
    wn.title("Welcome to the Shape World!")
    
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

    for t in range(3):
        triangle.forward(250)
        triangle.left(120)

#triangle_shape()

def shape_1():
    new_shape = turtle.Turtle()
    new_shape.color("red")
    new_shape.pensize(5)
    new_shape.shape("turtle")

    for ns in range(6):
        new_shape.left(60)
        new_shape.forward(200)

#shape_1()       

def draw_a_circle():
    circle = turtle.Turtle()
    circle.color("blue")
    circle.shape("arrow")
    circle.stamp()
    circle.circle(150)
    circle.pensize(15)
    

draw_a_circle()

windows_screen.wn.clear()

def tess():
    tess = turtle.Turtle()
    tess.color("white")
    tess.shape("turtle")
    tess.speed(3)

    dist = 5
    tess.up()

    for i in range(60):
        tess.stamp()
        tess.forward(dist)
        tess.right(24)
        dist += 2

def draw_rhombus(rhom):
    
    for r in range(3):
        rhom.forward(120)
        rhom.right(78)
        rhom.forward(120)
        rhom.right(102)
        rhom.forward(120)
        rhom.right(78)
        rhom.forward(120)

                
def sketch_a_flower():
    flower = turtle.Turtle()
    flower.speed(25)
    flower.shape("turtle")
    flower.color("yellow")

    for f in range(36):
        draw_rhombus(flower)
        flower.right(30)
    flower.right(70)

        
        

sketch_a_flower()
tess()



window_exit()
