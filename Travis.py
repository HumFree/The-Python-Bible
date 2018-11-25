#! /usr/bin/python3.6

# Make a list of Kwown users on the system.
Kwown_users = ["Alice", "Bob", "Clair", "Dan", "Emma", "Fred", "Georgie", \
"Harry", "Tom", "Tim", "Sarah", "Sam", "Billy", "William", "Elvis"]

# Have Travis introduce himself & ask for the users name.
while True:
    print("Hi!, My name is Travis. Please to meet you!")
    name = input("What is your name? ").strip().capitalize()

# Check to see if users name is in the system and print a response.
    if name in Kwown_users:
        print(("Hello {}. Nice to see you again.").format(name))
        remove = input("Would you like to be removed from the system? y/n? ").lower()

        if remove == "y":
            Kwown_users.remove(name)
            print("Sorry to see you go. :(")

        else:
            print("OK then, You will remain in the system.\n")

    else:
        print(("I'm sorry {}, you are NOT in the system.").format(name))
        add_user = input("Would you like to be added to the system? y/n ")

        if add_user == "y":
            print("OK then, you will be added to the system. Thank you!\n")
            Kwown_users.append(name)

        else:
            print("Oh well, maybe next time.\n")
