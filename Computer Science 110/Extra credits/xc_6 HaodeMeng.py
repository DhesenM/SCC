# Youtube link:http://youtu.be/jpfb_wzzfao?hd=1

#xc_6

def draw_triangle(t,size):
    '''Draw a triangle of size size using turtle t.'''
    for i in range(3):
        t.fd(size)
        t.rt(120)

def draw_triangles(t):
    '''Draw 5 surrounded triangles using turtle t. The innermost triangle is
filled with black.'''
    size = 30
    for i in range(5):
        if i == 0:
            t.begin_fill()
        draw_triangle(t,size)
        if i == 0:
            t.end_fill()
        if not(i == 4):    # Avoid making extra moves
            t.pu();t.rt(30);t.bk(29);t.lt(30);t.pd() 
            size += 50

def twoTrianglesofTriangles(t):
    '''Draw two triangles of triangles using turtle t.'''
    t.rt(180)
    draw_triangles(t)
    t.pu();t.bk(16);t.rt(90);t.fd(29*4);t.lt(30);t.fd(30);t.rt(120);t.pd()
    # Move turtle t to the next triangle
    draw_triangles(t)

def lineOfTriangles(t):
    '''Draw a line of triangles of triangles using turtle t.'''
    for i in range(3):
        twoTrianglesofTriangles(t)
        t.pu();t.fd(30+50*4+16+30);t.rt(90);t.fd(29*4);t.rt(30);t.fd(30);t.lt(120);t.pd()
    # Move turtle t to the next triangle
    t.rt(180);draw_triangles(t)

def twoLinesOfTriangles(t):
    '''Draw two lines of triangles of triangles using turtle t.'''
    lineOfTriangles(t)
    t.pu();t.fd(130);t.lt(90);t.fd(16*4+8);t.rt(90);t.pd()
    lineOfTriangles(t)

def pattern(t):
    '''Draw the whole pattern which includes four lines of triangles of
triangles using turtle t.'''
    import math
    for i in range(2):
        twoLinesOfTriangles(t)
        if i == 0:
            t.pu();t.fd(130);t.rt(90);t.fd(16*4+2*15*math.sqrt(3)+8*29+8);t.lt(90);t.pd()
            
import turtle
sc = turtle.Screen()       # Set up the window and its attributes
tt = turtle.Turtle()       # Create turtle tt
sc.bgcolor("powderblue")   # Set the background color       
tt.pensize(7)              # Set the pensize of turtle t
tt.color("orangered","orangered")
tt.speed(0)

tt.pu()                    # Move the turtle to a wider space
tt.goto(-300,200)   
tt.pd()

pattern(tt)
tt.ht()
