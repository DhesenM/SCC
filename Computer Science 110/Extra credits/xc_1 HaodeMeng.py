# Youtube link:http://youtu.be/lfV-ldVDsb8?hd=1

# xc_1

def parallelogram_1(t):
    '''Draw a parallelogram of size 60*50 using turtle t'''
    for i in range(2):
        t.fd(60)
        t.lt(50)
        t.fd(50)
        t.lt(130)

def parallelogram_2(t):
    '''Draw a Draw a parallelogram which is the reverse of parallelogram_1'''
    for i in range(2):
        t.fd(60)
        t.lt(130)
        t.fd(50)
        t.lt(50)

def parallelogram_dot_1(t):
    '''Draw a parallelogram of size 60*50 with a dot using turtle t'''
    parallelogram_1(t)
    t.pu()
    t.fd(30)
    t.lt(50)
    t.fd(25)
    t.dot()
    t.bk(25)
    t.rt(50)
    t.fd(30)
    t.pd()

def parallelogram_dot_2(t):
    '''Draw a parallelogram which is the reverse of parallelogram_dot_1'''
    parallelogram_2(t)
    t.pu()
    t.fd(30)
    t.lt(130)
    t.fd(25)
    t.dot()
    t.bk(25)
    t.rt(130)
    t.fd(30)
    t.pd()


def parallelogram_line_1(t):
    '''Draw a parallelogram of size 60*50 with a line which connect two
midpoints using turtle t'''
    parallelogram_1(t)
    t.fd(30)
    t.lt(50)
    t.fd(50)
    t.bk(50)
    t.rt(50)
    t.fd(30)

def parallelogram_line_2(t):
    '''Draw a parallelogram which is the reverse of parallelogram_line_1'''
    parallelogram_2(t)
    t.fd(30)
    t.lt(130)
    t.fd(50)
    t.bk(50)
    t.rt(130)
    t.fd(30)
    
def lineOfParallelograms_1(t):
    '''Draw a line of 3 parallelograms with a dot and 3 parallelograms with
a line using turtle t'''
    for i in range(3):
        parallelogram_dot_1(t)
        parallelogram_line_1(t)

def lineOfParallelograms_2(t):
    '''Draw the reverse of the first line of parallellelograms'''
    t.rt(180)
    for i in range(3):
        parallelogram_dot_2(t)
        parallelogram_line_2(t)

def TwolinesOfParallelograms_1(t):
    '''Draw two lines of 3 parallelograms with a dot and 3 parallelograms with
a line using turtle t'''
    lineOfParallelograms_1(t)
    lineOfParallelograms_2(t)

def Pattern(t):
    '''Draw a pattern which is made of 12 lines of parallelograms using
turtle t'''
    for i in range(6):
        if i < 5:
            TwolinesOfParallelograms_1(t)
            t.lt(130)
            t.fd(50)
            t.rt(80)
            t.fd(50)
            t.lt(130)
        else:
            TwolinesOfParallelograms_1(t)  # Prevent the turtle make an extra line

import turtle
sc = turtle.Screen()     # Set up the window and its attributes
tt = turtle.Turtle()     # Create turtle tt
sc.bgcolor("lightgreen") # Set the background color
tt.color("blue")         # Set the color of turtle tt
tt.pensize(2)            # Set the pensize of turtle t
tt.speed(10)

Pattern(tt)
# Draw a pattern which is made of 12 lines of parallelograms using turtle tt
