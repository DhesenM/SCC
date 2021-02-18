##Youtube link: http://youtu.be/5OBgTHr1tHU?hd=1

##hw_04_ex_05_yt

def spiral(t,n):
    '''Draw a spiral which is made of rotated squares of angle n using turtle t'''
    size = 0
    for i in range(100):
        t.fd(size)
        t.rt(n)
        size = size + 3 

def go_to_450_0(t):
    '''Move the turtle to the point (450,0)'''
    t.pu()
    t.goto(450,0)
    t.pd()
    
import turtle
sc = turtle.Screen()       # Set up the window and its attributes
tt = turtle.Turtle()       # Create turtle tt
sc.bgcolor("lightgreen")   # Set the background color
tt.color("blue")           # Set the color of turtle tt
tt.pensize(3)              # Set the pensize of turtle tt
tt.speed(10)

spiral(tt,90)     # Draw the first spiral using turtle tt
go_to_450_0(tt)   # Move the turtle tt to the point (450,0)
spiral(tt,89)     # Draw the second spiral using turtle tt
