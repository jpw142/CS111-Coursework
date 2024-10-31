# 
# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions on strings and lists, part I
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

def last_first(values):
    """ takes a list of values and returns a new list containing the last
        value of the original list followed by the first value
    """
    last = values[-1]
    first = values[0]
    return [last, first]

def every_other(values):
    """ takes a list of values and returns a list containing every other
        value from the original list
    """
    eo = values[::2]
    return eo

def begins_with(word, prefix):
    """ takes two string inputs and returns true if the 
        word begins with the prefix, otherwise it returns false
    """
    if word[0:len(prefix)] == prefix:
        return True
    else:
        return False
