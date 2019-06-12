from random import randint


f = open("/Users/mcneillc/Dev/weekly-hackery/hangman/google-10000-english.txt", "rb")
dictionary = f.readlines()
dictionary = [word.decode("utf-8").strip() for word in dictionary if len(word) >= 3]
f.close()


def random_word():
    selection = randint(0, len(list(dictionary))-1)
    choice = dictionary[selection]
    return choice


def cheat(guesses, length):
    matches = []

    def match_length(words, length):
        return [word for word in words if len(word) == length]

    for word in match_length(dictionary, length):
        state = True
        for guess in guesses:
            if guess in word:
                state = False
        if state:
            matches.append(word)

    if matches:
        return matches[randint(0, len(matches)-1)]
    else:
        return None


def guessing(limit):
    target = random_word()
    blanks = list('-' * len(target))
    print(target)
    print(' '.join(blanks))
    bad_guesses = []
    all_guesses = []
    while blanks != list(target):
        if len(bad_guesses) < limit:
            guess = input("You have " + str(limit - len(bad_guesses)) + " chances left. Guess a letter: ")
            all_guesses += guess
            if target.count(guess) > 0:
                cheat_attempt = cheat(all_guesses, len(target))
                if cheat_attempt:
                    target = cheat_attempt
                    bad_guesses += guess
                    print(target)
                else:
                    indices = [i for i, a in enumerate(target) if a == guess]
                    for index in indices:
                        blanks[index] = guess
            else:
                bad_guesses += guess
            print(' '.join(blanks))
        else:
            return [False, target]
    return [True, target]


def hangman(limit):
    print("Let's play hangman!")

    play = guessing(limit)
    if play[0]:
        print("Congratulations! The word was: " + play[1])
    else:
        print("You have run out of chances. The word was: " + play[1])


hangman(20)
