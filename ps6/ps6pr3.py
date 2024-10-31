def BUtify(s):
    """ capitalizes B and U in any string """
    new_string = ""
    for i in range(len(s)):
        if s[i] == 'b':
            new_string += 'B'
        elif s[i] == 'u':
            new_string += 'U'
        else:
            new_string += s[i]
    return new_string

def diff(vals1, vals2):
    """ returns a list of absolute differences of two lists, adds extra to the end """
    newlist = []
    minlen = min(len(vals1), len(vals2))
    maxlen = max(len(vals1), len(vals2))
    for i in range(minlen):
        diff = vals1[i] - vals2[i]
        newlist += [abs(diff)]
    for i in range(minlen, maxlen):
        newlist += vals1[i: i+1]
        newlist += vals2[i: i+1]
    return newlist

def square_evens(vals):
    """ squares every even value in a list """
    for i in range(len(vals)):
        if vals[i] % 2 == 0:
            vals[i] = vals[i] ** 2

def negate_last(n, values):
    """ negates the last occurence of n in values """
    for i in range(len(values)-1, -1, -1):
        if values[i] == n:
            values[i] *= -1
            return

            
