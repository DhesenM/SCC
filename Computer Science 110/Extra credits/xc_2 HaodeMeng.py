# Youtube link: http://youtu.be/oZFwIVCsP1k?hd=1

# xc_2

def diamond(t):
    '''Draw a diamond of size 20+5 using turtle t'''
    for i in range(4):
        t.pu()
        t.fd(5)
        t.pd()
        t.fd(20)
        t.pu()
        t.fd(5)
        t.rt(90)
        t.pd()

def lineOfDiamonds(t):
    '''Draw a line of 5 diamonds using turtle t'''
    t.lt(45)
    for i in range(5):
        if i < 4:
            diamond(t)
            t.pu()
            t.rt(90)
            t.fd(30)
            t.rt(90)
            t.fd(30)
            t.rt(180)
            t.pd()
        else:
            diamond(t)        # Prevent the turtle make an extra line

def SquareOfDiamonds(t):
    '''Draw a square of 5*5 diamonds using turtle t'''
    for i in range(5):
        if i < 4:
            lineOfDiamonds(t)
            t.pu()
            t.fd(150)
            t.lt(90)
            t.fd(90)
            t.rt(135)
            t.pd()
        else:
            lineOfDiamonds(t) # Prevent the turtle make an extra line
    t.pu()
    t.rt(90)
    t.fd(30)
    t.lt(45)
    t.fd(15*2**.5)            # Pythagorean theorem
    t.lt(90)
    t.pd()
    for i in range(4):        # Draw a square of size 150 * 2^0.5
        t.pensize(5)
        t.fd(150*2**.5)       # Pythagorean theorem
        t.lt(90)
        t.pensize(3)

def pattern(t):
    '''Draw a pattern of 2*3 squares of diamonds using turtle t'''
    for i in range(6):
        if i < 2:
            SquareOfDiamonds(t)
            t.pu()
            t.fd(4.5*30*2**.5)
            t.rt(90)
        elif i == 2:
            SquareOfDiamonds(t) # Prevent the turtle make unnecessary moves
        elif i == 3:
            t.pu()              # Move turtle t to the next line
            t.lt(90)
            t.fd(15*30*2**.5)
            t.lt(90)
            t.fd(15*2**.5)
            t.lt(90)
            t.pd()
            SquareOfDiamonds(t)
        else:
            t.pu()
            t.fd(4.5*30*2**.5)
            t.rt(90)
            SquareOfDiamonds(t)

import turtle
sc = turtle.Screen()       # Set up the window and its attributes
tt = turtle.Turtle()       # Create turtle tt
sc.bgcolor("lightgreen")   # Set the background color
tt.color("blue")           # Set the color of turtle tt
tt.pensize(3)              # Set the pensize of turtle t
tt.speed(10)

tt.pu()                    # Move the turtle to a wider space
tt.goto(-300,300)   
tt.pd()

pattern(tt)
