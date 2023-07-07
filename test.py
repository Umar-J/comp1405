list = [1,4,6,8,2,5]
#selection sort
# for i in range(0,len(list)-1):
#     minimum = i
#     for j in range (i+1, len(list)):
#         if list[j]<list[minimum]:
#             minimum = j
#     list[i], list[minimum] = list[minimum], list[i]
# print(list)

#bubble
n = len(list) -1
flag = True

while flag:
    flag = False
    for i in range (0, n):
        if (list[i+1] < list[i]):
            list[i+1], list[i] = list[i], list[i+1]
            flag = True
    n-=1
    print("hello")
print(list)
# why is this a postcondition loop?