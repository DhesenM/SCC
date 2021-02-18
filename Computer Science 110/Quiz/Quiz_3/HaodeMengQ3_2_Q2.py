# Q3_2_Q2

def plus(t,sz):
    '''Draw a plus sign with turtle t'''
    for i in range(4):
        t.fd(sz/2) # Draw the arm of the plus of size 1/2 sz
        t.bk(sz/2) # Move backward to the initial point
        t.lt(90)   # Next arm of the plus will be perpendicular to the first arm

import turtle
sc = turtle.Screen()    # Set up the window and its attributes
tess = turtle.Turtle()  # Create turtle tess

# Sample
plus(tess,100)

# Draw a plus sign of size 100 with turtle tess (four "arms" of the plus are 50)
