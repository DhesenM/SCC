# Youtube link:http://youtu.be/KVIE03Kmq_M?hd=1

# xc_3

def rectangle(t):
    '''Draw a rectangle of size 60*90 using turtle t'''
    for i in range(2):
        t.fd(60);t.lt(90);t.fd(90);t.lt(90)

def wiggly_circle(t):
    '''Draw a wiggly circle using turtle t'''
    for i in range(10):
        t.fd(5);t.lt(60);t.fd(5);t.rt(20)

def rectangle_circle(t):
    '''Draw a rectangle of size 60*90 and 3 wiggly circles inside the rectangle
using turtle t'''
    t.pu();rectangle(t);t.fd(15);t.pd()
    x,y = t.pos()
    for i1 in range(2):
        if i1 == 1:
            t.pu();t.goto(x+30,y);t.setheading(0);t.pd()
        for i in range(3):     # Draw three wiggly circles
            wiggly_circle(t)
            t.pu();t.goto(x+30*i1,y);t.setheading(90);t.fd(30+i*30);t.setheading(0);t.pd()

def filling_color(colr,t):
    '''Set the filling color for turtle t'''
    t.color("black",colr)

def lineOfRectangles(t,n):
    '''Draw a line of rectangles of 60*90 which are filled with 2 different
colors using turtle t'''
    x,y = t.pos()
    for i in range(12):
        t.begin_fill()
        if (i % 2 == 0 and n) or (i % 2 == 1 and not(n)):
                               # Draw a lightsteelblue rectangle every two times
            filling_color("lightsteelblue",t)
        else:                  # Draw a yellow palegoldenrod rectangle every two times
            filling_color("palegoldenrod",t)
        rectangle_circle(t)
        t.end_fill()
        t.pu();t.goto(x+60*(i+1),y);t.pd()

def twoLinesOfRectangles(t):
    '''Draw two lines of rectangles of 60*90 which are filled with 2 different
colors using turtle t'''
    lineOfRectangles(t,True)
    t.pu();t.bk(720);t.rt(90);t.fd(90);t.lt(90);t.pd() # Move the turtle to the next line
    lineOfRectangles(t,False)

def pattern(t):
    '''Draw a 5*12 pattern of rectangles using turtle t'''
    for i in range(3):
        if i < 2:
            twoLinesOfRectangles(t) # Draw the first 2 lines 
            t.pu();t.bk(720);t.rt(90);t.fd(90);t.lt(90);t.pd()
        else:
            lineOfRectangles(t,True)     # Draw the last line

import turtle
sc = turtle.Screen()       # Set up the window and its attributes
tt = turtle.Turtle()       # Create turtle tt
sc.bgcolor("white")        # Set the background color       
tt.pensize(3)              # Set the pensize of turtle t
tt.speed(10)

tt.pu();tt.goto(-300,300);tt.pd()   # Move the turtle to a wider space

pattern(tt)
