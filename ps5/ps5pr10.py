def add_odds(n):
    """ adds the first n odds together """
    result = 0
    odd = 1
    for w in range(n):
        print(result, "+", odd, "=", result + odd)
        result += odd
        odd += 2
    return result

def get_mult(n):
        """ continuously asks for a multiple of n from the user and returns when the user input is a multiple of n"""
        w = int(input("Enter a multiple: "))
        if w % n == 0:
            return w
        while True:
                w = int(input("Invalid input. Try again: "))
                if w % n == 0:
                    return w
