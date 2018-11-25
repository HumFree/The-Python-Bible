#! /usr/bin/python3.6
"""
# A list called jackson that takes out indexs 3,4,5
jackson = [1, 2, 3,"A", "B", "C", "Do", "Rei", "Mi", "You", "and", "Me"]
#print(jackson[3:6])

my_number = [[9, 3, 7], [9, 2, 5], [2, 0, 0, 2]]
#print(my_number)

area_code = my_number[0]
#print(area_code)

first_three = my_number[1]
#print(first_three)

last_four = my_number[2]
#print(last_four)


member_one = [["Christopher", "Ryan", "Humphrey"], ["1132", "Woodlawn", "Ave"], ["Springfield", "Ohio"]]
#print(member_one[0])
#print(member_one[1])
#print(member_one[2])
#print(member_one[3])

first_name = member_one[0][0]
print(first_name)

middle_name = member_one[0][1]
print(middle_name)

last_name =  member_one[0][2]
print(last_name)

house_number = member_one[1][0]
print(house_number)

street_name = member_one[1][1]
print(street_name)

street_ext = member_one[1][2]

city = member_one[2][0]
print(city)

state = member_one[2][1]
print(state)

full_name = first_name + " " + middle_name + " " + last_name
print(full_name)

address = house_number + " " + street_name + " " + street_ext + " " + city + " " + state
print(address)

"""
"""
matrix = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
#print(matrix[4])

zeros = [0] * 100
print(zeros)

#exes = ["M","I","A"] * 200
#print(exes)

#numbers = list(range(21))
#print(numbers)

#skip_by_two = list(range(0, 1001, 3))
#print(skip_by_two)

names = list("cat", "dog")
print(names)
"""

word_list = [["one"], ["two"], ["three"]]

user_pick = input("pick a number? ").strip().lower()

if user_pick in word_list:
    print("We got it")
