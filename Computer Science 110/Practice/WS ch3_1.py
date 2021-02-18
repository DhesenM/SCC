import turtle
x = input("Please choose your desired background color:")
screen = turtle.Screen()
screen.bgcolor(x)
tess = turtle.Turtle()
y = input("Please choose your desired tess' color:")
tess.color(y)
z = input("Please choose your desired tess' pensize:")
tess.pensize(int(z))


