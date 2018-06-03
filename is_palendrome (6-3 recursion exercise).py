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
