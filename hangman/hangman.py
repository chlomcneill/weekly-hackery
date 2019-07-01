from random import randint


f = open("/Users/mcneillc/Dev/weekly-hackery/hangman/google-10000-english.txt", "rb")
dictionary = f.readlines()
dictionary = [word.decode("utf-8").strip() for word in dictionary if len(word) >= 3]
f.close()


def random_word():
    selection = randint(0, len(list(dictionary))-1)
    choice = dictionary[selection]
    return choice


def guessing(target, limit):
    blanks = list('-' * len(target))
    # print(target)
    print(' '.join(blanks))
    bad_guesses = 0
    while blanks != list(target):
        if bad_guesses < limit:
            guess = input("You have " + str(limit - bad_guesses) + " chances left. Guess a letter: ")
            if target.count(guess) > 0:
                indices = [i for i, a in enumerate(target) if a == guess]
                for index in indices:
                    blanks[index] = guess
            else:
                bad_guesses += 1
            print(' '.join(blanks))
        else:
            return False
    return True


def hangman(limit):
    print("Let's play hangman!")
    target = random_word()
    play = guessing(target, limit)
    if play:
        print("Congratulations! The word was: " + target)
    else:
        print("You have run out of chances. The word was: " + target)


hangman(10)




