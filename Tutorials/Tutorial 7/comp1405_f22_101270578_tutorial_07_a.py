# Umar Jan 
# 101270578

# must use one or more loops to check that every element in the argument is, itself, a list
def verify(matrix):
    for x in matrix:
        if (isinstance(x, list)):
            pass
        else:
            return False
    
    lens = []
    for y in matrix:
        leng = len(y)
        lens.append(leng)
    for i in lens:
        if i == leng:
           pass
        else:
            return False
# must use one or more loops to check that every "row" of the matrix is the same length
    for z in range(len(matrix)):
        for i in matrix[z]:
            if (isinstance(i, int)) or (isinstance(i, float)):
                pass
            else:
                return False
# must use one of more loops to check that every element in the matrix is a numeric value
    return True
