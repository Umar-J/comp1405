import random

def foo():
    odd = []
    for i in range (1,10000,2):
        odd.append(i)
def bar():
    upper=[]
    for i in range (100):
        letter = chr(random.randint(65,90))
        upper.append(letter)
def qux(list):
    #loop 20x
    for i in range (20):
        pos = random.randint(0,len(list))
        list.insert(pos,"?")
def aap(list):
    #loop random times
    num = random.randint(1,20)
    for i in range (num):
        # insert ! at end
        list.append("!")
def ham(list):
    #event loop
    i=0
    while True:
        if "A" in list:
            list.remove("A")
        else:
            break
def egg(list):
    while True:
        if "z" in list:
            list.pop(0)
        else:
            break
