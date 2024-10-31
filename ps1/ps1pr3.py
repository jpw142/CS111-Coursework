# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

def root(x):
    """ returns the square root of its input
    """
    return x ** 0.5

def gap(num1, num2):
    """ returns the gap between the two inputs
    """
    if num1 > num2:
        return num1 - num2
    elif num1 < num2:
        return num2 - num1
    else:
        return 0

def larger_gap(a1, a2, b1, b2):
    """ returns the larger gap of the two sets of inputs
    """
    gapB = gap(a1, a2)
    gapA = gap(b1, b2)
    if gapA > gapB:
        return gapA
    else:
        return gapB

def median(a, b, c):
    """ returns the median of the three numbers as if they were in a list
    """
    if a < b and a < c:
        if b >= c:
            return c
        else:
            return b
    elif a > b and a > c:
        if b <= c:
            return c
        else:
            return b
    else:
        return a
    
# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))
    
    # optional but encouraged: add test calls for your functions below
    print('root(25) returns', root(25))
    print('root(2) returns', root(2))

    print('gap(5,2) returns', gap(5,2))
    print('gap(2,5) returns', gap(2,5))
    print('gap(2,2) returns', gap(2,2))
    print('gap(4,6) returns', gap(4,6))

    print('lgap(3,2,4,7) returns', larger_gap(3, 2, 4, 7))
    print('lgap(7,2,3,4) returns', larger_gap(7, 2, 3, 4))
    print('lgap(2,3,5,4) returns', larger_gap(2, 3, 5, 4))

    print('median(10,2,7) returns', median(10, 2, 7))
    print('median(7,2,10) returns', median(7, 2, 10))
    print('median(8,6,4) returns', median(8, 6, 4))
    print('median(10,2,2) returns', median(10, 2, 2))
    print('median(2,10,2) returns', median(2, 10, 2))
