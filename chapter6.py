###############################################################################
# Chapter 6  Fruitful Functions
###############################################################################

# use incremental development (scaffolding) to write a function called hypotenuse
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

# Exercise 6-3 recursion Exercise
def first(word):
    '''Prints the first character of the word'''
    return word[0]

def last(word):
    '''Prints the last character of the word'''
    return word[-1]

def middle(word):
    '''Returns all but first and last chars of a string'''
    return word[1:-1]


# scaffolding version of code to visually check/understand the recursion.
def is_palendrome(word):
    '''Returns True if the word is palendrome'''
    space = ' ' * (4 * len(word)) # scaffolding.
    print(space, 'word length', len(word)) # scaffolding
    if len(word) <= 1:
        print(space, 'none', word) # scaffolding
        return True
    if last(word) != first(word):
        print (space, 'first and last letters do not match: ', first(word), last(word)) # scaffolding
        return False
    print(space, first(word), ':', last(word)) # scaffolding
    return is_palendrome(middle(word))


def is_palendrome(word):
    """Returns True if the word is palendrome"""
    if len(word) <= 1:
        return True
    if last(word) != first(word):
        return False
    return is_palendrome(middle(word))

print(is_palendrome('hannah'))
