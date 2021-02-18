# Youtube link :http://youtu.be/90Km5zRKM3U?hd=1

# hw_05_ex_08_yt

def draw_bar(t,height):
    '''Get turtle t to draw one bar, of height.'''
    t.begin_fill()           # Added this line
    t.lt(90)
    t.fd(height)
    t.write("  "+ str(height))
    t.rt(90)
    t.fd(40)
    t.rt(90)
    t.fd(height)
    t.pu()
    t.lt(90)
    t.end_fill()             # Added this line
    t.fd(10)
    t.pd()

import turtle

wn = turtle.Screen()     # Set up window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()   # Create tess and set some attributes
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    if a >= 200:                    # Turtle bar is filled with red when >= 200
        tess.color("blue","red")  
    elif a >= 100 and a < 200:      # Turtle bar is filled with yellow when >= 100 and <200
        tess.color("blue","yellow")
    else:                           # Turtle bar is filled with green when < 100
        tess.color("blue","green")
    draw_bar(tess,a)

wn.mainloop()
