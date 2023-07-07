# Umar Jan 101270578

import random

exitFlag = True
# Ask user for an integer
usernum = int(input("Enter the size of the list:"))
# Create a list with the length of num
userList = [random.randint(1, 20) for i in range(usernum)]
def stringcount(userstring, list):
        count = 0
        for i in list:
            if userstring == i:
                count +=1 
        return print(userstring, "is in the list exactly", count, "times")

while exitFlag:
    # Print options and get choice
    print(userList)
    print("enter 1 to choose a number to replace with a string")
    print("enter 2 to count how many times a string is in the list")
    print("enter 3 to quit")
    choice = int(input(">"))

    # Call replace function
    if choice == 1:
        usernum = int(input("enter a number to replace with a string"))
        print("enter a string to replace", usernum, "with")
        string = input(">")
        for i in range(len(userList)):
            if usernum == userList[i]:
                userList[i] = string
    elif choice == 2:
        # Get the string and print the return value of the function
        userword = input("Enter string:\n> ")
        stringcount(userword,userList)
    elif choice == 3:
        exitFlag = False

