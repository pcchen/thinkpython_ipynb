from swampy.TurtleWorld import *

world = TurtleWorld()

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

bob = Turtle()
square(bob, 100)

wait_for_user()
