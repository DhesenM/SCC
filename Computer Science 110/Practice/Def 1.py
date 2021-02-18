import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex draws a square")
alex = turtle.Turtle()

def square_1(t,Size):
    '''Draws a square of size Size using turtle t'''
    for i in range(4):
        t.forward(Size)
        t.left(90)

def pinwheel(t,size):
    '''Draws a square of size Size followed by air rotation left of 30 deg & repeats this 12 times.'''
    for i in range(12):
        square_1(t,Size)
        alex.lt(30)


Size = 100
wn.mainloop()

