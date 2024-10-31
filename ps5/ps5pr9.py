def cube_all(vals):
    """ cubes every value in a list """
    result = []

    for w in vals:
        result += [w ** 3]
    return result

def add_stars(s):
    """ adds stars inbetween each char in string """
    result = ''
    result += s[0]
    for w in range(1, len(s)):
        result += '*'
        result += s[w]
    return result    

def compare(s1, s2):
    """ returns number of differences in positions between two strings """
    result = 0
    len_shorter = min(len(s1), len(s2))

    for i in range(len_shorter):
        if s1[i] != s2[i]:
            result += 1
    result += abs(len(s1) - len(s2))
    return result

def weave(list1, list2):
    """ weaves together two lists into one, and if 1 list is longer adds rest on after """
    max_len = max(len(list1), len(list2))
    list3 = []
    for w in range(max_len):
        list3 += list1[w:w+1]
        list3 += list2[w:w+1]
    return list3
