# Umar Jan 101270578
# Tutorial 4, Ex. A
while True:
    userNumber = int(input("Please enter a number: \n>"))
    
    #break if input biger than 9 or lower than 1
    if (userNumber >= 1) and (userNumber <= 9):
        break
    else:
        print("Please enter a number between 1 and 9")
x=1
# line
for q in range (1, userNumber+1):
    print()
    # repeat numbers in the line
    for z in range (1, q+1):
        print(q,end="")