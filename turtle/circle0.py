import math
from swampy.TurtleWorld import *

world = TurtleWorld()
# world.ca(500, 500)

def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

bob = Turtle()
circle(bob, 100)

wait_for_user()
