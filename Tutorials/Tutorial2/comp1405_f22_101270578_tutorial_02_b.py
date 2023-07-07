# Umar Jan 101270578
# Tutorial 2, Ex. A

number = int(input("Enter your seven-digit phone number? "))

# get first 3 digits 1234567
prefix = number//10000
lineNumber = number % 10000

# Number calculations
calculatedNumber = 80*prefix
print("\nYour prefix is ", prefix, " Multiply this by 80, and the result is: ", calculatedNumber)

calculatedNumber = (calculatedNumber + 1) * 250
print("Add 1 to that result and multiply it by 250, and the result is: ", calculatedNumber)

calculatedNumber = calculatedNumber + 2*lineNumber
print("Your line number is", lineNumber,". Add this to the previous result twice, and the result is: ", calculatedNumber)

calculatedNumber = (calculatedNumber - 250)/2
print("Subtract 250 from that result and divide it by 2, and the result is: ", int(calculatedNumber))
