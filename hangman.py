#! /usr/bin/python3.6

# Hangman the game. User tries to guess a word one letter at a time.
# If the user guesses right the letter is added to the word.
# If the word the user guesses is wrong then a body part is added and displayed.
# The user gets three tries.
from random import choice
# Word list
words = ["happy", "puppy", "paper", "kitten", "mouse", "tiger", "bird",
"pencil", "cloak", "candy", "water", "sand", "town"]

# Ask if user would like to play. If yes the program
play_game = input("Would you like to play? y/n ").strip().lower()
if play_game == "y":
    print("Welcome to Hangman!")
else:
    print("Goodbye!")
    exit()


# picks a random word from a list of words.
random_word = random.choice(words)
print(random_word)

# get the number of letter in the random word.
ran_count= len(random_word)
print(ran_count)

# make dashes for each letter in len of random word.
dashes = "_ "
dash_in_word = ran_count * dashes
print(dash_in_word)

blank_list = []


# Displays the gallow.


# Asks user to pick a letter
letter_guess = input("Please pick a letter? ").strip()
print(letter_guess)

random_count = random_word.count(letter_guess)
print("There is {} {} in the word.".format(random_count, letter_guess))


# Checks to see if letter is in the word
if letter_guess in random_word:
    print("it's in the word.")

else:
    print("Sorry!, That letter isn't in the word.")


# If the letter is in word the letter is placed on the dash.
# If not, a messege Displays that the user was wrong and a part of body is displayed.
# The user has three chances to guess.
# Last wrong answer Displays a messege to play again.
