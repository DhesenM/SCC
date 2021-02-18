def turtle_refactor(colr,ttle):
    ttle.color(colr)

def draw_rectangle(t,W,H):
    for i in range(2):
        t.fd(W)
        t.lt(90)
        t.fd(H)
        t.lt(90)

import turtle
sc = turtle.Screen()
sc.bgcolor("lightgreen")

Tess = turtle.Turtle()
Alex = turtle.Turtle()
Dave = turtle.Turtle()

turtle_refactor("hotpink",Tess)
turtle_refactor("black",Alex)
turtle_refactor("yellow",Dave)

Alex.lt(45)
Dave.lt(70)

Tess.pensize(5)
Dave.pensize(2)

draw_rectangle(Tess,100,50)
draw_rectangle(Alex,150,200)
draw_rectangle(Dave,200,250)
