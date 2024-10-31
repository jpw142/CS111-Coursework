#
# ps3pr3.py (Problem Set 3, Problem 3)
#
# Caesar cipher / decipher
#

# A template for the first function that you are required to write.
def rotate(c, n):
    """ rotates a letter c forward by n places """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)
    if c.lower() not in 'abcdefghijklmnopqrstuvwxyz':
        return c
    order = ord(c) + n;
    # It's lowercase but past the lowercase numbers
    if 'Z' < chr(order) < 'a':
        order -= 26
    # Past uppercase numbers
    if chr(order) > 'z':
        order -= 26
    return chr(order)

#### Put your code for the encipher function below. ####
def encipher(s, n):
    """ rotates every letter in a string s by n places """
    if len(s) == 0:
        return ""
    rest_encipher = encipher(s[1:], n)
    return rotate(s[0], n) + rest_encipher

# A helper function that you will use in implementing your 
# string_score function.
# You should *NOT* modify this function.
def letter_score(c):
    """ takes a single character c and returns a numeric score that 
        is based on how frequently that character appears in 
        English-language text documents.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': 
        return 0.1904
    elif c == 'e' or c == 'E': 
        return 0.1017
    elif c == 't' or c == 'T': 
        return 0.0737
    elif c == 'a' or c == 'A': 
        return 0.0661
    elif c == 'o' or c == 'O': 
        return 0.0610
    elif c == 'i' or c == 'I': 
        return 0.0562
    elif c == 'n' or c == 'N': 
        return 0.0557
    elif c == 'h' or c == 'H': 
        return 0.0542
    elif c == 's' or c == 'S': 
        return 0.0508
    elif c == 'r' or c == 'R': 
        return 0.0458
    elif c == 'd' or c == 'D': 
        return 0.0369
    elif c == 'l' or c == 'L': 
        return 0.0325
    elif c == 'u' or c == 'U': 
        return 0.0228
    elif c == 'm' or c == 'M': 
        return 0.0205
    elif c == 'c' or c == 'C': 
        return 0.0192
    elif c == 'w' or c == 'W': 
        return 0.0190
    elif c == 'f' or c == 'F': 
        return 0.0175
    elif c == 'y' or c == 'Y': 
        return 0.0165
    elif c == 'g' or c == 'G': 
        return 0.0161
    elif c == 'p' or c == 'P': 
        return 0.0131
    elif c == 'b' or c == 'B': 
        return 0.0115
    elif c == 'v' or c == 'V': 
        return 0.0088
    elif c == 'k' or c == 'K': 
        return 0.0066
    elif c == 'x' or c == 'X': 
        return 0.0014
    elif c == 'j' or c == 'J': 
        return 0.0008
    elif c == 'q' or c == 'Q': 
        return 0.0008
    elif c == 'z' or c == 'Z': 
        return 0.0005
    else:
        return 0.0

#### Put your code for string_score and decipher below. ####
def string_score(s):
    """ uses a list comprehension to return the sum of letter scores of a string """
    scores = [letter_score(c) for c in s]
    return sum(scores)

def decipher(s):
    """ deciphers a string that has once been enciphered by a caeser cipher """
    options = [encipher(s, n) for n in range(26)]
    scores = [[string_score(secret), secret] for secret in options]
    return max(scores)[1]

