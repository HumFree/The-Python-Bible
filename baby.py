#! /usr/bin/python3.6
from random import choice

questions = ["Is the moon made from cheese? ", "Are hot dog made from dogs? ",
"Why is the sky blue? ", "Who made us? ", "Who's the oldest in the family? "]
question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("WHY! ").strip().lower()
print("Oh, Okay!")


"""
number = 1

while number <= 1000:
    number = number + number
    print(number)
"""
"""
which_way = input("What direction do you want to go? \ left or right ").strip().lower()

while which_way != "left" or "right":
    which_way = input("Please choose left or right.").strip().lower()

if which_way == "left, right":
    print(("You have chosen {}").format(which_way))
"""
