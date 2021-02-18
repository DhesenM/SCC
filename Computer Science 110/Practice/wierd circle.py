
import turtle
sc = turtle.Screen()       # Set up the window and its attributes
t = turtle.Turtle()       # Create turtle tt
sc.bgcolor("orange")       # Set the background color       
t.pensize(5)              # Set the pensize of turtle t
t.speed(2)

t.pu()                    # Move the turtle to a wider space
t.goto(-300,300)   
t.pd()


for i in range(20):
    t.fd(10);t.rt(60);t.fd(10);t.lt(40)
