from ps4pr1 import bin_to_dec
from ps4pr1 import dec_to_bin

def pow_bin(b, e):
    """ takes two bit strings and raises b to the power of e """
    dec_base = bin_to_dec(b)
    dec_exp = bin_to_dec(e)
    powered = dec_base ** dec_exp
    return dec_to_bin(powered)

def smallest_bin(binvals):
    """ returns the smallest binary value from a list of bit strings """
    values = [[bin_to_dec(b), b] for b in binvals]
    return min(values)[1]

