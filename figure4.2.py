import turtle
t=turtle.Turtle()
for i in range(6):
    t.left(60)
    t.forward(100)
for j in range(3):
    t.left(120)
    t.forward(200)
    t.left(120)
    if j is not 2:
        t.forward(100)

