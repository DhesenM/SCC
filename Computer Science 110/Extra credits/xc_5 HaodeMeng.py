# Youtube link:http://youtu.be/0j-zSpskYXo?hd=1

# xc_5

def hexagonal_1(t,n):
    '''Draw a hexagonal using turtle t. The degree is 15 among each line.
n can be True or False which decides whether there is a line in the middle or not'''
    import math
    t.lt(60)
    x,y = t.pos()
    for i in range(7):
        if n:
            if i == 3:
                t.pu()
        t.rt(15)
        t.fd(100/math.sqrt(2)/math.cos(math.pi/4-math.pi/12*i))
# Pythagorean theorem. The turtle turn right 15 degrees per time, so cos(pi/4)
# minuses pi/12 per time.
        t.rt(45-15*i)
        t.fd(80)
        t.rt(45-15*i)
        t.fd(100/math.sqrt(2)/math.cos(math.pi/4-math.pi/12*i))
        t.pu()
        t.goto(x,y)        # Move back to the start point
        t.lt(90-30*i)
        t.pd()
        if n:
            if i == 3:
                t.pd()

def lineOfHexagonal_1(t,n,num):
    '''Draw a line of hexagonals using turtle. n can be True or False which
decides whether there is a line in the middle or not'''
    import math
    for i in range(num):
        if i < (num - 1):
            hexagonal_1(t,n)
            t.lt(45)           # Let the turtle toward right
            t.pu()
            t.fd(100/math.sqrt(2)/math.cos(math.pi/4-math.pi/12*3)*2 + 80)
# When i = 3, the distance between the left vertex and the right vertex is the equation above.
            t.pd()
            t.fd(100)
        else:              # Prevent the turtle make a extra line
            hexagonal_1(tt,n)
    
def pattern(t):
    '''Draw 6 lines of hexagonals using turtle t. '''
    import math
    for i in range(8):
        if i % 2 == 0:
            n,num = True,3
        else:
            n,num = False,4
        lineOfHexagonal_1(t,n,num)
        t.pu();t.lt(45)
        t.bk(100/math.sqrt(2)/math.cos(math.pi/4-math.pi/12*3)*5 + 80*3 + 100*2 + 10)
# The horizontal distance between the left vertex of the third hexagonal in the first line and
# the left vertex of the first hexaginal in the second line
        t.rt(90);t.fd(100);t.lt(90);t.pd()
    t.ht()                 # Hide the turtle


import turtle
sc = turtle.Screen()       # Set up the window and its attributes
tt = turtle.Turtle()       # Create turtle tt
sc.bgcolor("orange")       # Set the background color       
tt.pensize(5)              # Set the pensize of turtle t
tt.speed(10)

tt.pu()                    # Move the turtle to a wider space
tt.goto(-300,300)   
tt.pd()

pattern(tt)
