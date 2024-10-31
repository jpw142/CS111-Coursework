#
# ps6pr4.py (Problem Set 6, Problem 4)
#
# TT Securities    
#
# Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the min price and its day')
    print('(5) Find the max single-day change and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.
def avg_price(prices):
    """ Finds average in a list of prices """
    sum = 0
    for p in prices:
        sum += p
    av = sum / len(prices)
    return av

def min_day(prices):
    """ finds the minimum price day """
    mn = 0
    for i in range(len(prices)):
        if prices[i] < prices[mn]:
            mn = i
    return mn

def max_change_day(prices):
    """ gets the day where the next day nets the greatest positive change in price """
    mx = 0
    for i in range(0, len(prices)-1):
        if (prices[i + 1] - prices[i]) > (prices[mx + 1] - prices[mx]):
            mx = i
    return mx + 1

def any_above(prices, x):
    """ tests if any prices in the list are above x"""
    for p in prices:
        if p > x:
            return True
    return False
def find_tts(prices):
    """ finds the best days to buy and sell stocks """
    mi = 0
    mj = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if (prices[j] - prices[i]) > (prices[mj] - prices[mi]):
                mi = i
                mj = j
    return [mi, mj, prices[mj] - prices[mi]]


def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        elif choice == 3:
            av = avg_price(prices)
            print('The average price is', av)
        elif choice == 4:
            day = min_day(prices)
            print('The min price is', prices[day], 'on day', day)
        ## add code to process the other choices here
        elif choice == 5:
            day = max_change_day(prices)
            print('The max single-day change occurs on day', day)
            print('when the price goes from', prices[day], 'to', prices[day + 1])
        elif choice == 6:
            threshold = int(input("Enter the threshold: "))
            v = any_above(prices, threshold)
            if v:
                print("There is at least one price above", threshold)
            else:
                print("There are no prices above", threshold)
        elif choice == 7:
            best = find_tts(prices)
            print(' Buy on day', best[0], 'at price', prices[best[0]])
            print('Sell on day', best[1], 'at price', prices[best[1]])
            print('Total profit:', prices[best[1]] - prices[best[0]])
        else: 
            print('Invalid choice. Please try again.')
    print('See you yesterday!')
