# Umar Jan 101270578

listlen = 0
list = []

Flag = True

while Flag:
    # Get user input
    print("enter 1 to Add a number to a list")
    print("enter 2 to Remove last value added to list (undo)")
    print("enter 3 to Quit")
    choice = int(input(">"))

    if choice == 1:
        # Add input
        print("what number would you like to add to the list")
        num = int(input(">"))
        list.append(num)
        listlen += 1

    elif choice == 2:
        #pop if list biger than 0
            if listlen>0:
                list.pop()
                listlen -= 1
            else:
                print("please enter a number before removing it")

    elif choice ==3:
        print("the length is:", listlen)
        Flag = False