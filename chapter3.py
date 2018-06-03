###############################################################################
# Chapter3: Functions
###############################################################################

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
