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
    # print(target)
    print(' '.join(blanks))
    guesses = []
    while blanks != list(target):
        guess = input("Guess a letter: ")
        if guess in guesses:
            print("You've already guessed that!")
            guess = input("Guess again: ")
        guesses += guess
        for char in target:
            if guess == char:
                blanks[target.index(char)] = guess
        print(' '.join(blanks))


def hangman():
    target = random_word()
    guessing(target)
    print("Congratulations! The word was: " + target)


hangman()




