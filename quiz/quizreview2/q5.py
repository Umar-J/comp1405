def foo():
    matrix = [
        [False, True, False, True, False, False, True, False],
        [True, False, False, False, False, True, True, True],
        [False, False, False, False, False, False, False, True],
        [True, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False],
        [False, True, False, False, False, False, False, True],
        [True, False, False, False, False, False, False, True], #6
        [False, True, False, False, False, True, True, False],
    ]
    return matrix

def bar():
    list = [[1,3,6], [0,5,7], [7], [0],[],[1,7],[0],[1,5,6]]
    return list

def qux(matrix, num1, num2):
    if matrix[num1][num2] == True:
        matrix[num1][num2] = False
        matrix[num2][num1] = False
    return matrix

def aap(matrix, num1, num2):
    if matrix[num1][num2] == False:
        matrix[num1][num2] = True
        matrix[num2][num1] = True ### have to do both cuz its an undirected graph OMGGGG
    return matrix

def ham(list, num1, num2):
    if num2 in list[num1]:
        list[num1].remove(num2)
        list[num2].remove(num1) ### same problem here (since undirected its gona be in both the 7 and the 1 but if directed dont need to do the other way)
    return list

def egg(list, num1, num2):
    if not(num2 in list[num1]):
        list[num1].append(num2)
    return list

