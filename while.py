#! /usr/bin/python3.6
"""
number = 1

while number <= 1500:
    if number % 2 == 0:
        print(number)
    number = number + 1
"""
# empty list called list
list = []

# A while loop that checks if the length of list is less than 3
while len(list) < 3:
    new_name = input("Please add a new name. ").strip().capitalize()
    list.append(new_name)

print("Sorry, list is full.")
print(list)
