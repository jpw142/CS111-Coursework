import random

def create_dictionary(filename):
    """ creates dictionary of markov model """
    f = open(filename)
    text = f.read().strip().replace("\n", " ")
    words = text.split(' ')


    words = [w for w in words if len(w) != 0]

    d = {}
    current_word = '$'

    for next_word in words:
        next_word = next_word
        if current_word not in d:
            d[current_word] = [next_word]
        else:
            d[current_word] += [next_word]
        current_word = next_word
        if current_word[-1] in '.?!':
            current_word = '$'
    return d

def generate_text(dictionary, wordcount):
    """ generates text based on markov model """
    current_word = '$'

    for i in range(wordcount):
        wordlist = dictionary[current_word]
        next_word = random.choice(wordlist)

        print(next_word, end= ' ')

        current_word = next_word
        if next_word[-1] in '.?!':
            current_word = '$'
