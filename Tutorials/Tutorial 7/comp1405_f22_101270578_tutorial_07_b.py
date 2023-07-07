# umar jan
# 101270578
def verify (matrix1, matrix2):
    #if 1 and 2 are same size return true
    if len(matrix1) == len(matrix2):
        for i in range(len(matrix1)):
            if len(matrix1[i]) == len(matrix2[i]):
                flag = True
            else:
                flag = False
                break
    else:
        flag = False
    return flag

def add (matrix1,matrix2):
    #check if addable
    if verify(matrix1,matrix2):
        #add elements
        result = []
        for r in range (len(matrix1)):
            row = []
            for c in range(len(matrix1[r])):
                row.append(matrix1[r][c] + matrix2[r][c])
            result.append(row)
        return(result)
    else:
        return result
