# Umar Jan 101270578

import sys

# Variables for first schematic
b = (sys.argv[2] == '1')
c = (sys.argv[3] == '1')
f = (sys.argv[6] == '1')

#  Variables for second schematic
g = (sys.argv[7] == '1')
i = (sys.argv[9] == '1')
j = (sys.argv[10] == '1')

# 1st schematic
result1 = ((not f) and c)
result1 = result1 and b
result1 = result1 and b

# 2nd schematic
result2 = (not g) or (not i)
result2 = result2 or j
result2 = result2 and i
print("<", result1, "," , result2, ">", sep="")
