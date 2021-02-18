# Q2_2_Q3

import turtle
sc = turtle.Screen()     # Set up the window and its attributes
tt = turtle.Turtle()     # Create turtle tt
sc.bgcolor("powderblue") # Set the background color

def sqr(t):
    '''Draws a square of size 100 using turtle t'''
    for i in range(4):
        t.fd(100)        # Make the turtle draw a square
        t.lt(90)

def lineOfSqrs(t):
    '''Draws a line of 3 diagonal 100*100 squares using turtle t'''
    for i in range(3):
        sqr(t)           # Call the function to draw the square
        t.pu()
        t.fd(100)        # Move the turtle to the starting point of the next square
        t.lt(90)
        t.fd(100)
        t.rt(90)
        t.pd()

lineOfSqrs(tt)
sc.mainloop()

# Draws a line of 3 diagonal 100*100 squares using turtle tt    
    
    
