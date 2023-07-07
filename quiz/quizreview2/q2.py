def qux(var_1, var_2, var_3):
    if var_3 < 0:
        print(var_1 and var_2)
    elif var_3 >= 0:
        print(var_1 or var_2)

def aap(var_1, var_2, var_3, var_4):
    list =[]
    if var_1 == True:
        list.append(var_2)
    if (var_1== True) and (var_3==True):
        list.append(var_4)
    return list
print(aap(True, "var2",False,"var4"))