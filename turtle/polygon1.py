from swampy.TurtleWorld import *

world = TurtleWorld()

def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

bob = Turtle()
polygon(bob, n=7, length=70)

alice = Turtle()
polygon(alice, length=50, n=7)

wait_for_user()
