# Youtube link:http://youtu.be/WdgVQWjnMMI?hd=1

#xc_7

def setUpTheTurtle(t,colr,ps):
    '''Set up turtle t's color and pensize as colr and ps.'''
    t.color(colr)
    t.pensize(ps)

def transverse_lines(t):
    '''Draw 25 transverse lines of spacing of 25 using turtle t.'''
    for i in range(12):
        if i == 6:  # Prevent covering the black axes
            t.pu()
        t.fd(600);t.rt(90);t.fd(25);t.rt(90)
        if i == 6:
            t.pd()
        t.fd(600);t.lt(90);t.fd(25);t.lt(90)
        if i == 11:
            t.fd(600)

def grid(t):
    '''Draw the background grid of size 600*600 using turtle t.'''
    setUpTheTurtle(t,"lightblue",3)
    t.pu();t.goto(-300,300);t.pd()
    transverse_lines(t);t.bk(600);t.lt(90);transverse_lines(t)

def axes(t):
    '''Draw black axes of size 600 using turtle t.'''
    setUpTheTurtle(t,"black",5)
    t.pu();t.goto(0,0);t.setheading(0);t.pd()
    for i in range(4):
        t.fd(300);t.bk(300);t.lt(90)

def plot(t):
    '''Plot the graph of f(x)=(1/6)x**2 - (1/12)x - 7.5, from -10 <= x <= 10
in steps of 1/4, using turtle t.'''
    for x in range(-10,11):
        y = ((1/6)*x**2 - (1/12)*x - 7.5)*25
        x = x * 25
        t.pu();t.goto(x,y);t.pd()
        for i in range(4):    # Draw green crosses at all the integer points
            setUpTheTurtle(t,"green",3)
            t.fd(10);t.bk(10);t.lt(90)
        if not(x == -10*25):  # Draw the graph of the function y
            setUpTheTurtle(t,"red",4)
            t.goto(a,b)
        a,b = x,y

def pattern(t):
    '''Draw the axes, grid and plot using turtle t.'''
    axes(tt)
    grid(tt)
    plot(tt)
    
        
import turtle
sc = turtle.Screen()       # Set up the window and its attributes
tt = turtle.Turtle()       # Create turtle tt
sc.bgcolor("white")        # Set the background color
sc.title("coordinate aexs with grid")
tt.pensize(5)              # Set the pensize of turtle t
tt.speed(0)
 
pattern(tt)
