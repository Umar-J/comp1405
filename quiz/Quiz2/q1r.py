def foo():
    matrix = [
        [False, True, True, False, True, False, True],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, True],
        [False, False, False, False, True, True, False], #3
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, True],
        [False, False, False, True, True, True, False]
    ]
    return matrix

def egg(matrix):
    for x in range (len(matrix)):
        z=0
        for i in range (len(matrix[x])):
            if matrix [x][i] == True:
                z+=1
        print(z,",",sep="",end="")

    if matrix [1]:
        b=0
        for z in range (len(matrix)):
            if matrix[z][1] == True:
                b+=1
        print("The number of nodes into 1 is", b)
