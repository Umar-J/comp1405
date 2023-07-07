# Umar Jan 101270578
# Tutorial 5, Ex. A
def isprime(x):
    for z in range(2, (x+2) // 2, 1):
        if (x% z)==0:
            return False
    return True
def inte():
    num = input("enter a number to check if its prime\n> ")
    if num.isdigit():
        return int(num)
    else:
        return inte()
while True:
    userint = inte()
    print(userint)# y is it none?
    print(isprime(userint))
    ask = input("Enter 'yes' if you would you like to continue?\n> ").upper()
    if ask != "YES":
        break
