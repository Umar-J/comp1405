pi = 3.14159
radius = float(input("Please enter the radius of a cone: "))
slant = float(input("please input the slant height of a cone: "))

result = (pi * slant * radius) + (pi * (radius**2))
print(f"{result:.4f}")