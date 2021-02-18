# hw_04_ex_01

def square(t):
    '''Draw a square of size 20 using turtle t'''
    for i in range(4):
        t.fd(20)
        t.lt(90)

def lineOfSquares(t,n):
    '''Draw a line of squares of size 20 using turtle t'''
    for i in range(n):
        square(t)
        t.pu()
        t.fd(40)
        t.pd()

import turtle
sc = turtle.Screen()     # Set up the window and its attributes
tt = turtle.Turtle()     # Create turtle tt
sc.bgcolor("lightgreen") # Set the background color
tt.color("hotpink")      # Set the color of turtle tt
tt.pensize(3)            # Set the pensize of turtle tt

lineOfSquares(tt,5)

# Draw a line of 5 squares of size 20 using turtle tt
