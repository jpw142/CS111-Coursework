def negate_evens(vals):
    if len(vals) == 0:
        return []
    rest_negate = negate_evens(vals[1:])
    if vals[0] % 2 == 0:
        return [-1 * vals[0]] + rest_negate
    else:
        return [vals[0]] + rest_negate
print()
print(negate_evens([2, 3, 5, 8]))
