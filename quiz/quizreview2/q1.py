import random
def foo():
    for i in range(0,21,2):
        print(i)
def bar():
    numl4 = 0
    numg4 = 0
    num4 = 0
    for i in range (100):
        num = random.randint(1,6)
        if num < 4:
            numl4 += 1
        elif num>4:
            numg4 += 1
        elif num == 4:
            num4 +=1
    return numl4, numg4, num4
