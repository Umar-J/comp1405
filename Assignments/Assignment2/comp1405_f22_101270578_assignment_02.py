# Umar Jan 101270578 

import sys
# gets user input
number = int(input("Enter a number "))

# exponent of 4
number = number**4
print(number)

# Subtracts 5
number = number - 5
print(number)

# adds command line argument
number = number + int(sys.argv[1])
print(number)

# adds the integer that is one more than itself
number = (number + number + 1)
print(number)

# multiples by 0.065406
number = number * 0.065406
print(number)

# converts to int
number = int(number)
print(number)

# converts to character
number = chr(number)

# prints final value
print("<", number, ">",)
