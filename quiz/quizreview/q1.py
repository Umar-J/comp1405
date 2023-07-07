outer = float(input("What is the outer radius of the circle"))
inner = float(input("What is the inner radius of the circle"))
height = float(input("What is the height of the circle"))

volume = ((outer**2 - inner**2) * height * 3.14159)
print(f"{volume:.4f}")