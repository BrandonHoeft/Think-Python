'''Chapter 4. Case Study: Interface Design with Turtle module.'''
# using http://www.skulpt.org as in browser implementation of Python.
import turtle
bob = turtle.Turtle()
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

# write the square as a for loop
for i in range(4):
    bob.fd(100)
    bob.lt(90)

# Ch4 Exercise 1.
bob = turtle.Turtle()
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
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

polygon(bob, 50, 8)
