def create_dictionary(filename):
    """ creates dictionary of markov model """
    f = open(filename)
    text = f.read()
    words = text.split(' ')

    d = {}
    current_word = '$'

    for next_word in words:
        if current_word not in d:
            d[current_word] = [next_word]
        else:
            d[current_word] += [next_word]
        if current_word[-1] in '.?!':
            current_word = '$'
        else:
            current_word = next_word
    return d

def generate_text(dictionary, wordcount):
    """ generates text based on markov model """
    current_word = '$'

    for i in range(wordcount):
        wordlist = dictionary[current_word]
        next_word = random.choice(wordlist)

        print(next_word, end= ' ')

        if next_word[-1] in '.?!':
            current_word = '$'
        else:
            current_word = next_word
    print()

