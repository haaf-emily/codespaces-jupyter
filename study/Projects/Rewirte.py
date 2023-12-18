import turtle #inside_Out
import math
import time
wn= turtle.Screen()
wn.bgcolor("dark green")
skk=turtle.Turtle()
skk.color("light green")

def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(math.sin(time.time())*30)
        size = size + 5

for i in range(6,1000,10):
    sqrfunc(i)
turtle.done()