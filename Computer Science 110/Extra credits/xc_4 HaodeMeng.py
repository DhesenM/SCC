# Youtube link: http://youtu.be/CcCE0memxao?hd=1

# xc_4

def square(t):
    '''Draw a square of size 20 * 20 using turtle t'''
    for i in range(4):
        t.fd(40);t.lt(90)

def sixSquares(t):
    '''Draw 6 squares of size 20 * 20 using turtle t'''
    for i in range(6):
        if i < 3:
            square(t)
            t.fd(40)
        elif i == 3:
            t.bk(120);t.rt(90);t.fd(40);t.lt(90)
            square(t)
        else:
            t.fd(40)
            square(t)

def color(colr,t):
    '''Set the filling color colr for turtle t'''
    t.color("black",colr)

def twoLinesOfSquares(t):
    '''Draw two lines of squares with 2 colors using turtle t'''
    for i in range(12):
        if (i % 2 == 0 and i < 6) or (i % 2 == 1 and i > 6):
            color("lightgreen",t)
        elif i == 6:
            t.bk(720);t.rt(90);t.fd(80);t.lt(90) # Move the turtle to the next line
            color("blue",t)
        else:
            color("blue",t)
            
        t.begin_fill()
        sixSquares(t)
        t.fd(40);t.lt(90);t.fd(40);t.rt(90)
        t.end_fill()

def pattern(t):
    '''Draw the pattern which is made of 6 lines of squares using turtle t'''
    for i in range(3):
        if i < 2:
            twoLinesOfSquares(t)
            t.bk(720);t.rt(90);t.fd(80);t.lt(90)
        else:
            twoLinesOfSquares(t)   # Prevent the turtle make extra lines

import turtle
sc = turtle.Screen()       # Set up the window and its attributes
tt = turtle.Turtle()       # Create turtle tt
sc.bgcolor("white")        # Set the background color       
tt.pensize(3)              # Set the pensize of turtle t
tt.speed(10)

tt.pu()                    # Move the turtle to a wider space
tt.goto(-300,300)   
tt.pd()

pattern(tt)
