# len =int(input())
# if len%3 != 0:
#     length = len//3+1
# else:
#     length = len//3
# print(length, len)
# count = 1
# [1,1,1,1,1,1,1,1,1]
len =int(input())
d = [1,1,2]
for i in range(4,len+1):
    temp = d[0]+d[2]
    d[0] = d[1]
    d[1] = d[2]
    d[2] = temp
print(d[2])

