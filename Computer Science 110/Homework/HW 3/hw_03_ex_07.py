## hw_03_ex_07

def drunk_pirate(t):
    '''The path taken by a drunk pirate'''
    for turn in (160,-43,270,-97,-43,200,-940,17,-86):
        t.lt(turn)
        t.fd(100)
    
import turtle
sc = turtle.Screen()     # Set up the window and its attributes
tt = turtle.Turtle()     # Create turtle tt
sc.bgcolor("lightgreen") # Set the background color
tt.color("hotpink")      # Set the color of turtle tt
tt.pensize(3)            # Set the pensize of turtle tt

drunk_pirate(tt)
