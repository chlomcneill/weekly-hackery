import string
import random

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


def monkey_simulator(string):
    list_of_strings = [reproduce_string(string) for _ in range(100)]
    # list_of_strings.append('METHINKS IT IS LIKE A WEASEL')
    # pprint.pprint(list_of_strings)
    sorted_list_of_strings = sorted(list_of_strings, key=score_string, reverse=True)
    # pprint.pprint(sorted_list_of_strings)
    best_match = sorted_list_of_strings[0]
    return best_match, score_string(best_match)


def main():
    iteration = 0
    (string, score) = monkey_simulator(random_string(28))
    while score < 28:
        (string, score) = monkey_simulator(string)
        iteration += 1
        print("Iteration: " + str(iteration) + ", Score: " + str(score) + ", " + string)


main()
