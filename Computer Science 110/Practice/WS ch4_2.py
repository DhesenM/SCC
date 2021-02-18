import turtle
s = turtle.Screen()
tess = turtle.Turtle()
s.bgcolor("lightgreen")
tess.pensize(4)

def draw_rectangle(t,W1,H1):
    '''Draws a rectangle of width w and height h'''
    for i in range(2):
        t.fd(W1)
        t.lt(90)
        t.fd(H1)
        t.lt(90)

def draw_rects(t,W1,H1,W2,H2):
    '''Draws 2 rectangles with the same center'''
    draw_rectangle(tess,W1,H1)
    t.pu()
    t.fd((W1-W2)/2)
    t.lt(90)
    t.fd(W2/2)
    t.pd()
    for i in range(2):
        t.fd(H2/2)
        t.rt(90)
        t.fd(W2)
        t.rt(90)
        t.fd(H2/2)

draw_rects(tess,200,20,25,400)
s.mainloop()
        
    
    
