###############################################################################
# Chapter 5  Conditionals & Recursion
###############################################################################


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
