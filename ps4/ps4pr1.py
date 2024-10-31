def dec_to_bin(n):
    """ converts an integer into its bit string representation """
    if n == 0:
        return ""
    # Cuts off the right most bit in the bit representation of the integer
    # 5 = 101
    # 2 = 10
    # 1 = 1
    # 1, 0, 1
    rest_dec = dec_to_bin(n//2)
    if n % 2 == 0:
        return rest_dec + '0'
    else:
        return rest_dec + '1'

def bin_to_dec(b):
    """ converts a bit string into its integer representation """
    if b == "":
        return 0
    rest_bin = bin_to_dec(b[:-1])
    if b[-1] == '1':
        return 1 + (rest_bin * 2)
    else:
        return rest_bin * 2

