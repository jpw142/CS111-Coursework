def longer(s1, s2):
    """ returns the longer of two strings, returning the 1st if they're the same """
    if len(s2) > len(s1):
        return s2
    else:
        return s1

def swap_halves(s):
    """ swaps the first and second half of the string """
    half_len = len(s) // 2
    return s[half_len:] + s[:half_len]

def repeat_one(values, index, num_times):
    """ repeats the value of the specified index a num_times # of times in place """
    return values[:index] + [values[index]] * (num_times - 1) + values[index:]

def test():
    print()
    print()
    print(longer('computer', 'compute'))
    print(longer('hi', 'hello'))
    print(longer('begin', 'again'))
    print()
    print(swap_halves('homework'))
    print(swap_halves('carpets'))
    print()
    print(repeat_one([10, 11, 12, 13], 2, 4))
    print(repeat_one([10, 11, 12, 13], 2, 6))
    print(repeat_one([5, 6, 7], 1, 3))
