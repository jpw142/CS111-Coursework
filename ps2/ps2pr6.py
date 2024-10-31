def letter_score(letter):
    """ Returns the scrabble score of a letter """
    assert(len(letter) == 1)
    if letter not in 'abcdefghijklmnopqrstuvwxyz':
        return 0
    if letter in 'aeilnorstu':
        return 1
    elif letter in 'dg':
        return 2
    elif letter in 'bcmp':
        return 3
    elif letter in 'fhvwy':
        return 4
    elif letter in 'k':
        return 5
    elif letter in 'jx':
        return 8
    elif letter in 'qz':
        return 10
    
def scrabble_score(word):
    """ Returns the scrabble score of a string """
    if len(word) == 0:
        return 0
    rest_score = scrabble_score(word[1:])
    return rest_score + letter_score(word[0])

def compare(s1, s2):
    """ returns the number of different letters in the same place in two strings """
    # we can assume they are the same length so we only need to check one
    if len(s1) == 0:
        return 0
    rest_compare = compare(s1[1:], s2[1:])
    if s1[0] != s2[0]:
        return rest_compare + 1
    else:
        return rest_compare

def weave(vals1, vals2):
    """ weaves together two lists, and if one is longer tacks on the extra to the end """
    if len(vals1) == 0:
        return vals2
    if len(vals2) == 0:
        return vals1
    rest_weave = weave(vals1[1:], vals2[1:])
    return [vals1[0], vals2[0]] + rest_weave

def test():
    print()
    print(letter_score('w'))
    print(letter_score('q'))
    print(letter_score('%'))
    print(letter_score('A'))
    print()
    print(scrabble_score('python'))
    print(scrabble_score('a'))
    print(scrabble_score('quetzal'))
    print()
    print(compare('alien', 'allen'))
    print(compare('alien', 'alone'))     
    print(compare('same', 'same'))
    print()
    print(weave([0, 0, 0, 0], [1, 1]))     
    print(weave([2, 1, 0], [3, 4, 5, 6]))  
    print(weave([1, 2], []))
    print(weave([], [3, 4, 5]))  
    print(weave([], []))

