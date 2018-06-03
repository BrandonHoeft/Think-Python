###############################################################################
# Chapter4: Case Study Interface Design with Turtle module.
# using http://www.skulpt.org as in browser implementation of Python.
# or can also use python terminal (issues executing with anaconda/spyder)
# for some reason.
###############################################################################

from turtle import *
bob = Turtle()
print(bob)

# Bob goes right then up at 90 degree angle.
bob.fd(100)
bob.lt(90)
bob.fd(100)

# bob draws a square.
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.reset()

# write the square as a for loop
for i in range(4):
    bob.fd(100)
    bob.lt(90)

# Ch4 Exercise 1.
def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

square(bob)

# Ch4 Exercise 2.
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 20)

# Ch4 Exercise 3.
def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

polygon(bob, 50, 8)

import math
# original circle function
def circle(t, n_sides, r):
    ''' Draws a circle by first calculating the circumference given the
    radius, r. Then calculates individual side_length, given the circumference.
    Draws circle by calling the polygon function. Note that the polygon will
    approach a circle for higher values of n_sides. A many sided polygon will
    be a decent approximation of a circle.'''

    circumference = 2 * math.pi * r
    side_length = circumference / n_sides
    polygon(t, n = n_sides, length = side_length)

# modified circle function. n_sides does not belong in the function interface as
# it simply pertains to how the circle should be rendered. we can automate that.
def circle(t, r):
    ''' Draws a circle by first calculating the circumference given the
    radius, r. Then renders circle by calling the polygon function with . Note
    that the polygon determines n sides by taking 1/3 of the total circumference.
    A many sided polygon will be a decent approximation of a circle.'''
    
    circumference = 2 * math.pi * r
    n_sides = int(circumference // 3) # floor division
    side_length = int(circumference // n_sides)
    polygon(t, n = n_sides, length = side_length)
