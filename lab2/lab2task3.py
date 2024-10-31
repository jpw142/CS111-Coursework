def mysum(x, y):
    """ takes two numbers and returns their sum """
    total = x + y
    return total

def even_odds(s):
    """ takes a string s and returns a new string in which 
        the characters in the even positions of s are followed 
        by the characters in the odd positions of s
    """
    evens = s[0::2]
    odds = s[1::2]
    return evens + odds

print(even_odds('python!'))
