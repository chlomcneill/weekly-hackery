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


def copies_of_string(string, copies):
    return [reproduce_string(string) for _ in range(copies)]


def monkey_simulator(list_of_strings):
    sorted_list_of_strings = sorted(list_of_strings, key=score_string, reverse=True)
    best_match = sorted_list_of_strings[0]
    return best_match


def main():
    iteration = 0
    string = monkey_simulator(copies_of_string(random_string(28), 100))
    score = score_string(string)
    while score < 28:
        string = monkey_simulator(copies_of_string(string, 100))
        score = score_string(string)
        iteration += 1
        print("Iteration: " + str(iteration) + ", Score: " + str(score) + ", " + string)


main()
