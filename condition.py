#! /usr/bin/python3.6

# Conditionals or, and, & not and combos of them

# or Conditional if either of the comparisons are true than the statement
# is true.
c = 10
b = 20
if c > 15 or b < 30:
    print("It works")

# The and Conditional both comparisons are true if both are true.
# If one or both comparisons are false then the statement is false.
A = 30
D = 3
if A > 20 and D < 5:
    print("It works")

if A < 40 and D < 2:
    print("It shouldn't work")

if A > 50 and D > 4:
    print("This shouldn't work either")

# The not Conditional 
