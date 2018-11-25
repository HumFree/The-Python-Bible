#! /usr/bin/python3.6

"""for number in range(1,1001):
    print(number)


for number in range(0, 1001, 2):
    print(number)



vowels = 0
consonants = 0

for letter in "hello":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1

print("There's {} vowels".format(vowels))
print("There's {} consonants".format(consonants))
"""
# A dictionary named students
students = {
"male": ["Tom", "Charlie", "Harry", "Frank"],
"female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
} # loop over the dictionary students and print out the list of
# names with the letter "e" in them.
for key in students.keys():
    for name in students[key]:
        if "e" in name:
            print(name)

words = ["cat", "dog", "mouse", "bird"]
for word in words:
    if "o" in word:
        print(word)
