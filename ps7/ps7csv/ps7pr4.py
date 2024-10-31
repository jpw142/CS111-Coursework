def main():
    """ handles user input """
    filename = str(input("Enter the name of data file: "))
    while True:
        print('')
        cityname = str(input("city: "))
        print('')
        if cityname == 'quit':
            break
        stateabbrv = str(input("state abbreviation: "))
        if stateabbrv == 'quit':
            break
        print('')
        process(filename, cityname, stateabbrv)

def process(filename, cityname, stateabbrv):
    """ processes the file and sees if there is a match and prints it out"""
    counter = 0
    file = open(filename, 'r')
    for line in file:
        line = line.strip('\n')
        fields = line.split(',')
        if fields[2] != cityname:
            continue
        if fields[3] != stateabbrv:
            continue
        counter += 1
        pop = int(float(fields[4]) * 1000)
        print(fields[0] + '\t' + fields[1] + '\t' + format(pop, '10,d'))
    if counter == 0:
        print('no results found for ' + cityname + ', ' + stateabbrv)

