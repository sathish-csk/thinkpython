try:
    from swampy.TurtleWorld import *
except ImportError:
    from TurtleWorld import *

def koch(t, n):
    if n<3:
        fd(t, n)
        return
    m = n/3.0
    koch(t, m)
    lt(t, 60)
    koch(t, m)
    rt(t, 120)
    koch(t, m)
    lt(t, 60)
    koch(t, m)
def snowflake(t, n):
    for i in range(3):
        koch(t, n)
        rt(t, 120)
world = TurtleWorld()
bob = Turtle()
bob.delay = 0

bob.x = -150
bob.y = 90
bob.redraw()
snowflake(bob, 300)
world.mainloop()
