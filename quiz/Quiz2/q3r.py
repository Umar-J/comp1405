
#1: 
aap = aap[14:] + (aap[:(len(aap)-18)])

#2:
x=0
while x<11:
    aap.pop(0)
    print(x)
    x+=1

#3:
x=12
while x < 32:
    aap.insert(x,32)
    x+=1

#4
i=0
while True:
    if 50 in aap:
        aap.remove(50)
    else:
        break