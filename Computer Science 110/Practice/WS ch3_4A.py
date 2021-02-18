import turtle
wn = turtle.Screen()
turtle = turtle.Turtle()


def draw_rectangle(t,w,h):
    '''Draws a rectangle of width and height using turtle t'''
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
         

draw_rectangle(turtle,100,200)
wn.mainloop()
