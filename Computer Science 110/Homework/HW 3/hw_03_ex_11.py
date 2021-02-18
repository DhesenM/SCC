# hw_03_ex_11

def draw_star(t,l):
    '''Draw a star of length l with turtle t'''
    t.hideturtle()
    t.lt(72)
    for i in range(5):
        t.fd(l)
        t.rt(144)

import turtle
sc = turtle.Screen()     # Set up the window and its attributes
tt = turtle.Turtle()     # Create turtle tt
sc.bgcolor("lightgreen") # Set the background color
tt.color("black")        # Set the color of turtle tt
tt.pensize(3)            # Set the pensize of turtle tt

draw_star(tt,200)
