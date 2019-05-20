import string
import random
from difflib import SequenceMatcher
import pprint

characters = list(string.ascii_uppercase + ' ')


def random_string(n):
    return ''.join(random.choice(characters) for _ in range(n))


def mutate_char(char):
    if random.randint(1, 100) <= 5:
        return random.choice(characters)
    else:
        return char


def reproduce_string(string):
    return ''.join([mutate_char(char) for char in string])


def score_string(string):
    target = 'METHINKS IT IS LIKE A WEASEL'
    score = 0
    for i in range(28):
        if string[i] == target[i]:
            score += 1
    return score


def fitness_comparator(string1, string2):
    return score_string(string1) - score_string(string2)


# print(score_string('METHINKX IT ISOLIKE A WEASEL'))


# def monkey_simulator(string):
#     score = 0
#
#     for i in range(100):
#         new_string = reproduce_string(string)
#         if


list_of_strings = [random_string(28) for i in range(100)]
list_of_strings.append('METHINKS IT IS LIKE A WEASEL')

# list_of_strings.sort(fitness_comparator)
pprint.pprint(list_of_strings)
sorted_list_of_strings = sorted(list_of_strings, key=score_string, reverse=True)

pprint.pprint(sorted_list_of_strings)



    # print(new_string, score_string(new_string))
    # print(scores)

#
# def main():
#     string = random_string(28)
#     monkey_simulator(string)