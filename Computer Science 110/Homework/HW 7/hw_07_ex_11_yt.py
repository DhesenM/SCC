# Youtube link: http://youtu.be/y7c65iNjVu8?hd=1

# hw_07_ex_11_yt

def drunk_pirate(t):
    '''Draw the path taken by a drunk pirate using turtle'''
    for angle,steps in ([160,20],[-43,10],[270,8],[-43,12]):
        t.lt(angle);t.fd(steps)

import turtle
sc = turtle.Screen()     # Set up the window and its attributes
tt = turtle.Turtle()     # Create turtle tt
sc.bgcolor("lightgreen") # Set the background color
tt.color("hotpink")      # Set the color of turtle tt
tt.pensize(3)            # Set the pensize of turtle tt

drunk_pirate(tt)
