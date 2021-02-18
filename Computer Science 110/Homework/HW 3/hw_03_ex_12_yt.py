# Youtube link: http://youtu.be/FqFIy6slp9k?hd=1

# hw_03_ex_12_yt

def draw_clock(t):
    '''Draw a face of a clock'''
    t.shape("turtle")
    t.stamp()
    for i in range(12):
        t.pu()
        t.fd(100)
        t.pd()
        t.fd(10)
        t.pu()
        t.fd(20)
        t.stamp()
        t.goto(0,0)
        t.lt(30)

import turtle
sc = turtle.Screen()     # Set up the window and its attributes
tt = turtle.Turtle()     # Create turtle tt
sc.bgcolor("lightgreen") # Set the background color
tt.color("blue")         # Set the color of turtle tt
tt.pensize(4)            # Set the pensize of turtle t

draw_clock(tt)
        
