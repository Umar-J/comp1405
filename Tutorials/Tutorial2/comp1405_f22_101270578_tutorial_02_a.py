# Umar Jan 101270578
# Tutorial 2, Ex. A

# get user name
name = input ("Please enter your name:  ")

# get current year
currentYear = int(input("Enter the current year: "))

# get birth year
birthYear = int(input("enter what year you were born: "))

# calculate age
age = currentYear - birthYear

# print possible ages and case for being born on a leap day
print("You are ", age, ", or ", (age - 1)," years old. If you were born on a leap-day that would mean you are", (age // 4)," years old" )
