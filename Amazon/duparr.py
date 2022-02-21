A = [3,4,1]
dic = dict()
for i in range(len(A)):
    if A[i] in dic:
        print(dic[A[i]])
        break
    else:
        dic[A[i]] = 1
else:
    print(-1)
    print(dic)