import sys

a = (sys.argv[1] == '1')
b = (sys.argv[2] == '1')
c = (sys.argv[3] =='1')
d = (sys.argv[4] == '1')
e = (sys.argv[5] == '1')
f = (sys.argv[6] == '1')
g = (sys.argv[7] == '1')
h = (sys.argv[8] == '1')
i = (sys.argv[9] == '1')
j = (sys.argv[10] == '1')

# first schematic
result1 = ((((not e) or (c and f)) or d) or (not g)) and (((not h) or b) or a)

# second schematic
result2 = (((((not e) and g) or (not d)) or a) and ((not h) and (f or c))) and (not b)

print("<",result1, ",", result2,">",sep="")