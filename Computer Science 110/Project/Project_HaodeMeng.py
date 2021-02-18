# Project_HaodeMeng


# Preparing Functions

import turtle
sc = turtle.Screen()       # Set up the window and its attributes
tt = turtle.Turtle()       # Create turtle tt
sc.bgcolor("white")        # Set the background color
tt.pensize(3)              # Set the pensize of turtle tt
sc.tracer(0,0)             # Speed up the turtle by turning off the animation

def moveToAWiderSpace(t):
    '''Move turtle t to (-400,150)'''
    t.pu();t.goto(-400,150);t.pd()
def fillingcolor(t,colr):
    '''Set the filling color for turtle t'''
    t.color("white",colr)
def square(t,colr):
    '''Draw a square of size 25 using turtle t'''
    fillingcolor(t,colr)
    t.begin_fill()
    for i in range(4):
        t.fd(25);t.lt(90)
    t.end_fill()
def rectangle(t,colr):
    '''Draw a rectangle of size 25*50 using turtle t'''
    fillingcolor(t,colr)
    t.begin_fill()
    for i in range(2):
        t.fd(50);t.lt(90);t.fd(25);t.lt(90)
    t.end_fill()
def twoSquaresAndOneRectangle(t,colr1,colr2):
    '''Draw two squares of size 25 and one rectangle of size 25*50 using
turtle t'''
    rectangle(t,colr1)
    t.rt(90);t.fd(25);t.lt(90)
    square(t,colr2);t.fd(25);square(t,colr2)
def draw_margin(t,colr2):
    '''Draw an salmon margin of the pattern using turtle t'''
    t.color("salmon",colr2)
    for i in range(4):
        t.fd(300);t.rt(90)


# Functions for Pattern A

def SquareOfSquares(t,colr1,colr2):
    '''Draw a square of squares which are made of 2 squares and one rectangle
using turtle t.'''
    for i in range(4):
        twoSquaresAndOneRectangle(t,colr1,colr2)
        t.pu();t.fd(50);t.rt(90);t.bk(50);t.pd()
def pattern_A(t,colr1,colr2):
    '''Draw a large square which is made of 9 squares of squares as the last
function using turtle t'''
    x,y = t.pos()
    for i in range(9):
        SquareOfSquares(t,colr1,colr2)
        if i < 2 or (i > 2 and i < 5) or (i > 5 and i < 8):
            t.pu();t.fd(100);t.pd()
 # Move turtle t to the next square that is in the same line
        else:
            t.pu();t.bk(200);t.rt(90);t.fd(100);t.lt(90);t.pd()
 # Move turtle t to the next square that is in the next line
    t.pu();t.goto(x,y + 25);t.setheading(0);t.pd()
 # Move turtle t to the left vertex of the large square
    draw_margin(t,"black")


# Functions for Pattern C
    
def SquareOfSquaresAndRectangles(t,colr1,colr2):
    '''Draw a square which is made of 5 rectangles and 4 squares combining
together using turtle t'''
    t.pu();t.setheading(0);t.fd(25);t.rt(90);t.pd()
 # Assume turtle t is at the left vertex of the large square.
    twoSquaresAndOneRectangle(tt,colr1,colr2)
    t.fd(50);t.lt(90);rectangle(t,colr1)
    t.rt(90);t.fd(25);t.lt(90);square(t,colr2)
    t.fd(25);rectangle(t,colr1)
    t.fd(75);t.lt(90);rectangle(t,colr1)
    t.fd(50);square(t,colr2)
    t.lt(90);t.fd(25);t.rt(90);t.bk(25);rectangle(t,colr1)
    t.lt(90);t.fd(25);t.rt(90);t.fd(50);t.rt(90);rectangle(t,colr1)
def pattern_C(t,colr1,colr2):
    '''Draw a large square which is made of 9 squares of squares and rectangles
as the last function using turtle t'''
    for i in range(9):
        SquareOfSquaresAndRectangles(t,colr1,colr2)
        if i < 2 or (i > 2 and i < 5) or (i > 5 and i < 8):
            t.pu();t.fd(50);t.rt(90);t.bk(25);t.pd()
 # Move turtle t to the next square that is in the same line
        else:
            t.pu();t.bk(250);t.rt(90);t.fd(75);t.pd()
 # Move turtle t to the next square that is in the next line
    t.pu();t.bk(300);t.lt(90);t.pd()
 # Move turtle t to the left upward vertex of the large square
    draw_margin(t,"black")


# My Pattern

def M(t,colr):
    '''Draw a letter M of color colr using turtle t'''
    fillingcolor(t,colr);t.setheading(0);t.begin_fill()
    x = 10
    for i in range(2):
        t.fd(x);t.lt(80);t.fd(30);t.rt(160);t.fd(30);t.lt(80)
 # Draw the sides below the M
        x += 3.3     # The line in the middle of letter M is longer
    t.fd(10);t.lt(100)
    for i in range(2):
        if i == 0:
            a,b = 30,40
        else:
            a,b = 40,30
        t.fd(b);t.lt(80);t.fd(15);t.lt(80);t.fd(a);t.rt(160)
 # Draw the sides above the M
    t.end_fill()
def lineOfMs(t,colr):
    '''Draw a line of 4 letter M of color colr using turtle t'''
    for i in range(4):
        x,y = t.pos()
        t.pu();t.lt(45);t.fd(15);t.pd()
        M(t,colr)
        t.pu();t.goto(x,y);t.setheading(0);t.fd(75)
def SquareOfMs(t,colr1,colr2):
    '''Draw a square of M of color colr1 using turtle t. The background color
of the square is colr2.'''
    t.pu();t.setheading(-90);t.fd(65);t.lt(180)
    a,b = t.pos();t.begin_fill();t.fd(65);t.rt(90);t.pd()
 # Move turtle t to the left vertex of the square
    draw_margin(t,colr2);t.end_fill()
    t.goto(a,b)
 # Move back to the start point to draw M
    for i in range(4):
        lineOfMs(t,colr1)
        if not(i == 3):
            t.pu();t.bk(300);t.rt(90);t.fd(75);t.lt(90);t.pd()
 # Avoid making extra moves
    

# Cardstock Cube Project

def trapezium(t):
    '''Draw a trapezium using turtle t.'''
    t.color("black");x,y = t.pos()
    t.lt(45);t.fd(30*2**.5);t.rt(45);t.fd(240);t.rt(45);t.fd(30*2**.5)
    t.pu();t.goto(x,y);t.setheading(0);t.pd()
 # Move back to the start point
def cardstockCube(t):
    '''Draw the whole cardstock cube using turtle t.'''
    moveToAWiderSpace(tt)
    pattern_A(t,"mediumspringgreen","orangered")
    t.fd(300);pattern_C(t,"sienna","lime")
    trapezium(t);t.pu();t.rt(90);t.fd(25);t.lt(90);t.fd(300);t.pd()
    pattern_A(t,"orangered","mediumspringgreen")
    x,y = t.pos();t.pu();t.fd(300);t.rt(90);t.pd();trapezium(t)
    t.pu();t.goto(x,y-300);t.lt(180);t.pd();trapezium(t)
 # Move to the right vertex of the square and draw the trapezium
    t.pu();t.lt(180);t.fd(600);t.lt(180);t.pd()
    SquareOfMs(t,"turquoise","gold")
    t.pu();t.goto(x-300,y-600);t.lt(180);t.pd();trapezium(t)
 # Move to the right vertex of the lower M pattern and draw the trapezium
    t.pu();t.goto(x-600,y+300);t.setheading(0);t.pd()
 # Move to the left vertex of the upper M pattern
    SquareOfMs(t,"gold","turquoise")
    t.pu();t.goto(x-600,y+300);t.setheading(0);t.pd();trapezium(t)
 # Draw the trapezium on the top of the upper M pattern
    t.pu();t.goto(x-900,y);t.setheading(0);t.pd()
 # Move to the left vertex of pattern C on the left side
    pattern_C(t,"lime","sienna")
    trapezium(t)
    t.pu();t.goto(x-600,y-300);t.lt(180);t.pd();trapezium(t)
 # Move to the right vertex of Pattern C on the left side and draw the trapezium
    t.ht()     # Hide the turtle

cardstockCube(tt)
