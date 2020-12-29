import turtle
bob = turtle.Turtle()

def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

polygon(bob, 5, 100)
turtle.mainloop()
