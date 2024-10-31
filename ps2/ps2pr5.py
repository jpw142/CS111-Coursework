# I worked with Sam!
# lehrich@bu.edu    

def dot(vals1, vals2):
    """ takes the dot product of two lists """
    if len(vals1) != len(vals2):
        return 0.0
    elif len(vals1) == 0 or len(vals2) == 0:
        return 0.0
    else:
        dot_rest = dot(vals1[1:], vals2[1:])
        return vals1[0] * vals2[0] + dot_rest;

def any_odd(vals):
    """ returns the bool if a list contains an odd number"""
    if len(vals) == 0:
        return False
    if vals[0] % 2 == 1:
        return True
    return any_odd(vals[1:])

def process(vals):
    """ for value in vals if it's odd square it if it's even don't do anything"""
    if len(vals) == 0:
        return []
    rest_process = process(vals[1:])
    if vals[0] % 2 == 1:
        return [vals[0] ** 2] + rest_process
    else: 
        return [vals[0]] + rest_process
