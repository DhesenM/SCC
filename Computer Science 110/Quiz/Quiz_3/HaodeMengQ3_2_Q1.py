# Q3_2_Q1

def rotSqr(t,sz):
    '''Draw a rotated square of size sz with turtle t'''
    t.lt(45)               # Let turtle t head toward the top vertex
    for i in range(4):
        t.fd(sz)           # Draw a rotated square of size sz
        t.rt(90)
    t.rt(45)               # Let turtle t head toward the right vertex

import turtle
sc = turtle.Screen()       # Set up the window and its attributes
tess = turtle.Turtle()     # Create turtle tess

# Sample
rotSqr(tess,100)

# Draw a rotated square of size 100 with turtle tess
