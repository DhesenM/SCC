# hw_04_ex_02

def square(t,sz):
    '''Draw a square of size sz using turtle t'''
    for i in range(4):
        t.fd(sz)
        t.lt(90)

def SquaresOutOfSquares(t,n):
    '''Draw squares out of squares. The innermost square is 2o units per side,
and each successive square is 20 units bigger'''
    sz = 20               # The size of the innermost square is 20
    for i in range(n):
        square(t,sz)
        t.pu()
        t.rt(135)
        t.fd(10*2**(1/2)) # Half of the diagonal of the square of size 20
        t.lt(135)
        t.pd()
        sz = sz + 20      # The next square is 20 units bigger
        
import turtle
sc = turtle.Screen()     # Set up the window and its attributes
tt = turtle.Turtle()     # Create turtle tt
sc.bgcolor("lightgreen") # Set the background color
tt.color("hotpink")      # Set the color of turtle tt
tt.pensize(3)            # Set the pensize of turtle tt

SquaresOutOfSquares(tt,5)

# Draw 5 squares that every successive square is 20 units bigger using
# turtle tt
