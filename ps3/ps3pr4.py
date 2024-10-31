def first_occur(elem, seq):
    """ returns the index at which the elem first occurs in the seq """
    if len(seq) == 0:
        return -1
    first = first_occur(elem, seq[1:])
    if seq[0] == elem:
        return 0
    if first == -1:
        return -1
    return first + 1

def rem_first(c, s):
    """ removes the first occurence of a letter in a string """
    if len(s) == 0:
        return ""
    elif s[0] == c:
        return s[1:]
    else:
        result_rest = rem_first(c, s[1:])
        return s[0] + result_rest

def jscore(s1, s2):
    """ Returns the jotto score of 2 strings, num of similiar chracters """
    if len(s1) == 0:
        return 0
    if len(s2) == 0:
        return 0
    first = first_occur(s1[0], s2)
    # If s1[0] doesn't appear in s2
    if first == -1:
        score = jscore(s1[1:], s2)
    # If s1[0] does occur in s2
    else:
        score = jscore(s1[1:], rem_first(s1[0], s2)) + 1
    return score

def negate_last(n, values):
    """ negates the last occurence of n in values """ 
    if len(values) == 0:
        return []
    if values[-1] == n:
        return values[:-1] + [values[-1] * -1]
    return negate_last(n, values[:-1]) + [values[-1]]
