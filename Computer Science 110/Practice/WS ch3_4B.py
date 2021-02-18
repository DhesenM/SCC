import turtle
wn = turtle.Screen()
turtle = turtle.Turtle()
turtle.speed(10)

def rectangle(t,w,h):
    '''Draws a rectangle of width and height using turtle t'''
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)


def pinwheel(t,w,h,n):
    '''Draws a rectangle of width and height followed by rotation left of 360/n deg & repeats this n times.'''

    for i in range(n):
        rectangle(t,w,h)
        turtle.left(int(360/n))

pinwheel(turtle,100,200,12)

wn.mainloop()
