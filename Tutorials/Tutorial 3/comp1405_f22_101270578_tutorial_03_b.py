# Umar Jan 101270578

job = input("What job do you want?\n1.Mechanic\n2.Hacker\n3.Taxi driver\nWhat is your choice: ")
# initial balance depending on job
if job == '1':
    money = 500
    print(f"\nyou have ${money} to spend")
elif job == '2':
    money = 600
    print(f"\nyou have ${money} to spend")
elif job == '3':
    money = 600
    print(f"\nyou have ${money} to spend")

# shop
enterStore = 1
while enterStore == 1:
    buy = input("\nWelcome to the store, What would you like to buy?\n1. Food\n2. Clothes\n3. Electronics\nEnter your selection: ")
    if buy == "1":
        food = int(input("\nFood costs $40/day, \nHow many days worth of food do you want? "))
        money -= food*40
        print(f"\nYou have ${money} left")
        enterStore = int(input("\nWould you like to buy more items\n Enter 1 if you would like to buy more items\n>"))

    elif buy == '2':
        clothes = int(input("\nClothes cost $100/set, \nHow many sets of clothes do you want? "))
        money -= clothes*100
        print(f"\nYou have ${money} left")
        enterStore = int(input("\nWould you like to buy more items\n Enter 1 if you would like to buy more items\n>"))

    elif buy == '3':
        elecs = int(input("\nPhones cost $200/phone, \nHow many phones do you want? "))
        money -= elecs*200
        print(f"\nYou have ${money} left")
        enterStore = int(input("\nWould you like to buy more items\n Enter 1 if you would like to buy more items\n>"))

else:
    print(f"\nThank you for shopping, you have ${money} leftover, have a nice day!\n")
