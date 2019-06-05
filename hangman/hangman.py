from random import randint


f = open("/Users/mcneillc/Dev/weekly-hackery/hangman/1-1000.txt", "rb")
dictionary = f.readlines()
dictionary = [word.decode("utf-8") for word in dictionary]
f.close()


def random_word():
    selection = randint(0, len(list(dictionary)))
    choice = dictionary[selection].strip()
    return choice


def guessing(target):
    blanks = list('-' * len(target))
    print(target)
    print(' '.join(blanks))
    guesses = []
    bad_guesses = 0
    while blanks != list(target):
        if bad_guesses < 6:
            guess = input("Guess a letter: ")
            if guess in guesses:
                print("You've already guessed that!")
                guess = input("Guess again: ")
            guesses += guess
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


def hangman():
    print("Let's play hangman!")
    target = random_word()
    play = guessing(target)
    if play:
        print("Congratulations! The word was: " + target)
    else:
        print("You have run out of guesses. The word was: " + target)


hangman()




