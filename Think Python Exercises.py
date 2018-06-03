# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 22:56:02 2017
Think Python by Allen B. Downey. Exercises
@author: bhoeft
"""

# Chapter 3 Functions Exercises ###############################################
len('allen')
# exercise 3-3
"""write a function that takes a string named s and prints the string with
enough leading spaces so tha tthe lsat letter of the strin is in column 70."""
def right_justify(s):
    print(' ' * (70 -len(s)) + s)

right_justify('Brandon')

# exercise 3-4. a function object.
def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

do_twice(print_spam)

def do_twice(f, value):
    f(value)
    f(value)

def print_twice(string):
    print(string)
    print(string)

do_twice(print_twice, 'spam')

""" Define a new function that takes a function object and value and calls the
function 4 times, passing the value as parameter. Should only be 2 statements
in the body of the function."""
def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

do_four(print_twice, 'spam')


# execise 3-5. This can be done using only the statements and other features learned so far.
print('+', end = ' ')
print('-')

def do_twice(f):
    f()
    f()

def do_four_times(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end = ' ')

def print_post():
    print('|        ', end = ' ')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

print_beam()
print_post()
print_beams()
print_posts()

def print_grid():
    print_beams()
    do_four_times(print_posts)
    print_beams()
    do_four_times(print_posts)
    print_beams()

print_grid()

# exercise 3-5 part deux. Write a function that draws similar grid, but 4 rows x 4 columns

def print_beams():
    do_four_times(print_beam)
    print('+')

def print_posts():
    do_four_times(print_post)
    print('|')

print_beams()
print_posts()

def print_4x4_grid():
    print_beams()
    do_four_times(print_posts)
    print_beams()
    do_four_times(print_posts)
    print_beams()
    do_four_times(print_posts)
    print_beams()
    do_four_times(print_posts)
    print_beams()

print_4x4_grid()


'''Chapter 4. Case Study: Interface Design with Turtle module.'''
# using http://www.skulpt.org as in browser implementation of Python.
# or can also use python terminal (issues executing with anaconda/spyder) for some reason.

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

# Chapter 5  Conditionals & Recursion ##########################################

''' A function that calls itself is recursive. Process of executing it is called
recursion. There may be times where recursion is a better alternative to a for()
loop, which we'll encounter later in the book.'''
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1) # outputs n, then runs countdown again but with n - 1.

countdown(10)

# recursively print a string n times
def print_n(s, n):
    if n <= 0:
        return
    else:
        print(s)
        print_n(s, n = n-1) # print string n-1 more times.

# Exercise 5-1: convert current time relative to epoch ()
import time
def current_time():
    '''Returns the current time in days, hours, minutes, and seconds since the
    epoch started on January 1, 1970. The time is originally stored as
    total seconds since the epoch began.'''

    time_now = time.time() # in seconds.
    seconds_per_day = 24 * 60 * 60
    seconds_per_hour = 60 * 60
    # floor division. get days.
    days = int(time_now // seconds_per_day)
    # get remainder total seconds and convert to h:m:s.
    seconds_remainder = time_now % seconds_per_day
    hours = int(seconds_remainder // seconds_per_hour)
    seconds_remainder = seconds_remainder % seconds_per_hour
    minutes = int(seconds_remainder // 60)
    seconds_remainder = seconds_remainder % 60
    seconds = int(seconds_remainder)

    print('There have been ' + str(days) + ' days, ' + str(hours)
    + ' hours, ' + str(minutes) + ' minutes, and ' + str(seconds)
    + ' second since the epoch.')

# Exercise 5-2: Fermat's Last Theorem
def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work.")

# Exercise 5-2: Fermat's Last Theorem. User input version.
def check_fermat():
    print("Test if Fermat's last theorem can be cracked.")
    # ask for user to provide input before running the program.
    a = int(input('What value to use for a?\n'))
    b = int(input('What value to use for b?\n'))
    c = int(input('What value to use for c?\n'))
    n = int(input('What value to use for n, the exponent?\n'))
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work.")

# Exercise 5-3: Given three sticks, can you form a triangle?
def is_triangle(side1, side2, side3):
    if side1 > side2 + side3 or side2 > side1 + side3 or side3 > side1 + side2:
        print('No, you cannot form a triangle.')
    elif side1 == side2 + side3 or side2 == side1 + side3 or side3 == side1 + side2:
        print('Meh, You can form a degenerate triangle.')
    else:
        print('Yes, you can form a triangle!')


def is_triangle():
    side1 = int(input('What is the length of side1?\n'))
    side2 = int(input('What is the length of side2?\n'))
    side3 = int(input('What is the length of side3?\n'))
    if side1 > side2 + side3 or side2 > side1 + side3 or side3 > side1 + side2:
        print('No, you cannot form a triangle.')
    elif side1 == side2 + side3 or side2 == side1 + side3 or side3 == side1 + side2:
        print('Meh, You can form a degenerate triangle.')
    else:
        print('Yes, you can form a triangle!')

# Exercise 5-4. recursive function provided below.

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

# Exercise 5-5.
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(2 * angle)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length * n)

# Exercise 5-6 Draw a Koch Curve
length = 15
bob.lt(60)
bob.fd(length/3)

# Chapter 6  Fruitful Functions ################################################

# use incremental development to write a function called hypotenuse
import math
def hypotenuse(a, b):
    a_squared = a ** 2
    b_squared = b ** 2
    print('a_squared equals', a_squared)
    print('b_squared equals', b_squared)
    return 0.0

def hypotenuse(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    print('hypotenuse equals', c)
    return c

def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2) # return makes it a fruitful function.

# boolean fruitful functions.
'''write a function, is_between(x, y, z) that returns True if x <= y <= z
or False otherwise'''
def is_between(x, y, z):
    if x <= y and y <= z:
        return True
    else:
        return False

def is_between(x, y, z):
    return x <= y and y <= z # concise version. booleans.

# write a recursive function of the definition of factorial.
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = recurse * n
        return result

# write a recursive function of the definition of fibonacci sequence.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
