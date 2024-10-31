def mult(vals):
    """ Multiplies all of the values together in a list"""
    if len(vals) == 1:
        return vals[0]
    rest_mult = mult(vals[1:])
    return rest_mult * vals[0]

def add_stars(s):
    """ Adds stars between each character in a list """
    if len(s) < 2:
        return s
    rest_stars = add_stars(s[1:])
    return s[0] + '*' + rest_stars


def test():
    print()
    print(mult([5, 3, 2]))
    print(mult([1, 2, 3, 4]))
    print(mult([3]))
    print()
    print(add_stars('hello'))
    print(add_stars('hangman'))
    print(add_stars('x'))

