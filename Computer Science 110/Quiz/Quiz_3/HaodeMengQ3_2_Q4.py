# Q3_2_Q4

def rotSqr(t,sz):
    '''Draw a rotated square of size sz with turtle t'''
    t.lt(45)               # Let turtle t head toward the top vertex
    for i in range(4):
        t.fd(sz)           # Draw a rotated square of size sz
        t.rt(90)
    t.rt(45)               # Let turtle t head toward the right vertex

def plus(t,sz):
    '''Draw a plus sign with turlte t'''
    for i in range(4):
        t.fd(sz/2) # Draw the arm of the plus of size 1/2 sz
        t.bk(sz/2) # Move backward to the initial point
        t.lt(90)   # Next arm of the plus will be perpendicular to the first arm

def diamondWithPlus(t,sz):
    '''Draw a diamond of size sz and a plus sign of size 1/2 sz using function rotSqr and plus with turtle t'''
    plus(t,sz/2)             # Draw a plus sign of size sz/2 with turtle t
    t.pu()
    t.fd(((sz**2)/2)**(1/2)) # Turtle t moves forward 1/2 diagonal of the diamond
    t.rt(180)                # Turn turtle t to use function rotSqr()
    t.pd()
    rotSqr(t,sz)             # Draw a diamond with turtle t
    t.rt(180)                # Let turtle t toward right

def lineOfDiaPlus(t,sz,n):
    '''Draw n diamonds with a plus with turtle t'''
    for i in range(n):
        t.pu()
        t.fd(((sz**2)/2)**(1/2))  # Turtle t moves forward 1/2 diagonal of the diamond
        t.pd()
        diamondWithPlus(t,sz)

import turtle
sc = turtle.Screen()       # Set up the window and its attributes
tess = turtle.Turtle()     # Create turtle tess
tess.speed(10)

# Sample
lineOfDiaPlus(tess,50,7)

# Draw 7 diamonds of size 50 with a plus with turtle tess
