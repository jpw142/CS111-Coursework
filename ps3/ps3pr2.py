def cube_all_lc(values):
    """ Raises all numbers in a list to the power of 3"""
    return [x**3 for x in values]

def cube_all_rec(values):
    """ Raises all numbers in a list to the power of 3"""
    if len(values) == 0:
        return []
    rest_cube = cube_all_rec(values[1:])
    cubed = [values[0] ** 3]
    return cubed + rest_cube

def consonants(s):
    """ returns a list of the constonants in a string """
    return [x for x in s if x not in 'aeiou']

def num_consonants(s):
    """ returns the number of constonants in a string """
    c = [1 for x in s if x not in 'aeiou']
    return sum(c)

def most_consonants(wordlist):
    """ returns the word from a list with the most constonants """
    numlist = [[num_consonants(s), s] for s in wordlist]
    pair = max(numlist)
    return pair[1]

