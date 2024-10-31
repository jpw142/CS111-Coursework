#
# Lab 10, Task 3
#
# Computer Science 111
#

def build_dict(filename):
    """ takes the name of a text file and builds a dictionary 
        in which each key is a lower-case letter and the corresponding 
        value is a list of all words from the file that begin with 
        that letter
    """
    # read in the file as one big string    
    file = open(filename, 'r')
    text = file.read()
    file.close()
    
    # split the file into a list of words
    words = text.split()
    
    # start with an empty dictionary
    d = {}
    
    for w in words:
        w = w.lower()
        if w[0] in d:
            d[w[0]] += [w]
        else:
            d[w[0]] = [w]
    return d
d = build_dict('edited_mission.txt')
print(d['c'])
        
