#
# Name: CS 111 Staff
#
# lab3.py
#

def num_consonants(s):
    """ returns the number of consonants in s
        parameter: s is a string of lower-case letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_consonants(s[1:])
        if s[0] in 'aeiou':
            return num_in_rest
        else:
            return num_in_rest + 1

print(num_consonants("pooop"))

def remove_spaces(s):
    if s == '':
        return s
    rest_string = remove_spaces(s[1:])
    if s[0] == ' ':
        return rest_string;
    else: 
        return s[0] + rest_string

print(remove_spaces("hello my name is jack and i love pickles   so much"))
