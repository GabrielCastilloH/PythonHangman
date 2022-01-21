from words import word_list
import random
secret_word = random.choice(word_list)


def get_guess():
    oneL = False
    while not oneL:
        guess = input("Guess: ").lower()
        if len(guess) == 1:
            if guess.islower():
                oneL = True
                return guess
            else:
                print("Your guess must be a lowercase letter!")
                oneL = False
        else:
            print("Your guess must have exactly one character!")
            oneL = False


dashes = []
for i in range(len(secret_word)):
    dashes.append("-")
word = "".join(dashes)


def update_dashes(secret_word, dashes, guess):
    if guess in secret_word:
        for i in range(len(secret_word)):
            if dashes[i] == "-":
                if guess == secret_word[i]:
                    dashes[i] = guess
        global word
        word = "".join(dashes)
        return True
    else:
        word = "".join(dashes)
        return False


won = False
guesses_left = 10

while guesses_left > 0:
    print(word)
    print(f"{guesses_left} incorrect guesses left.")
    guesses = update_dashes(secret_word, dashes, get_guess())
    if guesses_left == 0:
        won = False
        break
    elif word == secret_word:
        won = True
        break
    elif not guesses:
        guesses_left -= 1
        print("That letter is not in the word.")
    else:
        print("That letter is in the word!")

if won:
    print("You win! You guessed the word! The word was: " + secret_word)
else:
    print("You lose! The word was: " + secret_word)
