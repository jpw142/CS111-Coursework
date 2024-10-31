def double_rec(binvals):
    """ doubles every bit string in a list of bit strings """
    if len(binvals) == 0:
        return []
    rest_double = double_rec(binvals[1:])
    return [binvals[0] + "0"] + rest_double

def double_lc(binvals):
    """ doubles every bit string in a list of bit strings """
    return [x + "0" for x in binvals]

def add_bitwise(b1, b2):
    """ adds two bit strings """
    if len(b1) == 0:
        return b2
    if len(b2) == 0:
        return b1
    rest_bitwise = add_bitwise(b1[:-1], b2[:-1])
    if b1[-1] == '1' and b2[-1] == '1':
        carry_bitwise = add_bitwise(rest_bitwise, "1")
        return carry_bitwise + '0'
    elif b1[-1] == '0' and b2[-1] == '0':
        return rest_bitwise + '0'
    else:
        return rest_bitwise + '1'
