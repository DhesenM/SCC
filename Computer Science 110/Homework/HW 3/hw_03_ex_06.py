## hw_03_ex_07

def draw_triangle(t,l):
    '''Draws an equilateral triangle of length l with turtle t'''
    for i in range(3):
        t.fd(l)
        t.lt(120)

def draw_square(t,l):
    '''Draws a square of length l with turtle t'''
    for i in range(4):
        t.fd(l)
        t.lt(90)

def draw_hexagon(t,l):
    '''Draws a hexagon of length l with turtle t'''
    for i in range(6):
        t.fd(l)       
        t.lt(60)

def draw_octagon(t,l):
    '''Draws an octagon of length l with turtle t'''
    for i in range(8):
        t.fd(l)     
        t.lt(45)

import turtle
sc = turtle.Screen()     # Set up the window and its attributes
tt = turtle.Turtle()     # Create turtle tt
sc.bgcolor("powderblue") # Set the background color
tt.color("red")          # Set the color of turtle tt
tt.pensize(5)            # Set the pensize of turtle tt

draw_triangle(tt,150)
draw_square(tt,150)
draw_hexagon(tt,150)
draw_octagon(tt,150)
# Draw 4 regular polygons of length 150 with turtle tt
