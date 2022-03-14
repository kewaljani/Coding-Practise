A = "abba"
dic = dict()
for i in A:
    if i in dic:
        dic.pop(i)
    else:
        dic[i]=1

if len(A)%2!= 0:
    if len(dic) == 1:
        print(1)
    else:
        print(0)
else:
    if len(dic) == 0:
        print(1)
    else:
        print(0)