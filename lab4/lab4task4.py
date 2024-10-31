
def negate(i):
    if abs(i) % 2 == 0:
        return i * -1
    else:
        return i
    
def negate_evens_lc(vals):
    return [negate(x) for x in vals]


