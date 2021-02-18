# hw_04_ex_04

def square(t):
    '''Draw a square of size 100 using turtle t'''
    for i in range(4):
        t.fd(100)
        t.lt(90)

def LargeSquare(t):
    '''Draw s square of size 200 which is made of 4 small squares using turtle t'''
    for i in range(4):
        square(t)        # Draw a square of size 100 using turtle t
        t.lt(90)  

def RotatedSquares(t):
    '''Draw 5 rotated squares of size 200 using turtle t'''
    for i in range(5):
        LargeSquare(t)   # Draw a square of size 200 using turtle t
        t.lt(18)         # Rotated angle for every square (360/20)
        
import turtle
sc = turtle.Screen()       # Set up the window and its attributes
tt = turtle.Turtle()       # Create turtle tt
sc.bgcolor("lightgreen")   # Set the background color
sc.title("Pretty pattern") # Set the title
tt.color("blue")           # Set the color of turtle tt
tt.pensize(3)              # Set the pensize of turtle tt
tt.speed(10)

RotatedSquares(tt)

# Draw 5 rotated squares of size 200 using turtle tt
