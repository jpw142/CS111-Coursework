# 
# ps1pr6.py - Problem Set 1, Problem 6
#
# Functions on strings and lists, part II
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

def reverse(s):
    """ takes a string input and returns a string with the input in reverse
    """
    return s[::-1]

def ends_match(s):
    """ takes a string and returns true if the first and last character
        match otherwise returns false
    """
    if s[0] == s[-1]:
        return True
    else:
        return False

def replace_start(values, new_start_vals):
    """ takes as inputs a list values and another list new_start_vals, 
        and that returns a new list in which the elements in new_start_vals 
        have replaced the first elements of the list values
    """
    new_len = len(new_start_vals)
    return new_start_vals + values[new_len:]

def adjust(s, length):
    """takes as inputs a string s and an integer length, 
        and that returns a string in which the value of s has been adjusted 
        as necessary to produce a string with the specified length.
    """
    slice = s[:length]
    s_len = len(slice)
    if s_len != length:
        dif = length - s_len
        return slice + slice[-1] * dif
    else:
        return slice

