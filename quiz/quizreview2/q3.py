var_1 = 1 #global var
var_2 = 2 #modified but not returned so.......
var_3 = 3 #global var
var_4 = 4 #not modified
def foo(x):
    return 100 + x
def bar(var_2):
    var_2 += 100
def qux(var_3):
    var_3 = var_3 + 100
    return var_3
def main(var_1):
    var_1 = foo(var_1)
    bar(var_2)
    qux
main()
