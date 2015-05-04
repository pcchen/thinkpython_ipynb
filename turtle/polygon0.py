from swampy.TurtleWorld import *

world = TurtleWorld()

def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

bob = Turtle()
polygon(bob, 7, 70)

wait_for_user()
