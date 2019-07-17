from random import randint

f = open("hp1.txt", "r")
text = f.read().split()
f.close()


def read_text(text):
    index1, index2, index3 = 0, 1, 2
    triples = []
    while index3 != (len(text)-1):
        triples.append([text[index1], text[index2], text[index3]])
        index1 += 1
        index2 += 1
        index3 += 1
    return triples


def generate_word(initial_pair):
    triples = read_text(text)
    options = []
    for option in triples:
        if initial_pair == option[0:2]:
            options.append(option[2])
    choice = randint(1, len(options))
    return options[choice-1]


def markov_chain(initial_pair, limit):
    markov = [initial_pair[0], initial_pair[1], generate_word(initial_pair)]
    count = 0
    while count != limit:
        new_word = generate_word([markov[-2], markov[-1]])
        markov.append(new_word)
        count += 1
    print(' '.join(markov))


markov_chain(['He', 'was'], 100)



# print(generate_word(["They", "were"]))




# print(text)



