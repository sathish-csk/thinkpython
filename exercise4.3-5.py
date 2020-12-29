import turtle
import math
bob = turtle.Turtle()

def polygon(t, length, n, m=None):
    if(isinstance(t, turtle.Turtle) == False):
        return
    if(m is None):
        m = n
    t.showturtle()
    for i in range(1, m + 1):
        t.fd(length)
        t.lt(360 / n)
    turtle.mainloop()
    return
def circle(t, radius, angle=360):
    if(float(radius) == "NaN"):
        return
    circumference = 2 * math.pi * radius
    length = circumference / angle
    n = 360
    polygon(t, length, n, angle)
def arc(t, radius, angle=360):
    circle(t, radius, angle)

arc(turtle.Turtle(), 50, 180)
turtle.mainloop()
