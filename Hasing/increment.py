lst = []
A = [ 1, 2, 3, 2, 3, 1, 4, 2, 1, 3 ]
dic = dict()
for i in range(len(A)):
    print("i = ",i , dic)
    if A[i] in dic:
        A[dic[A[i]]]+=1
        val = A[dic[A[i]]]
        index = dic[A[i]]
        dic.pop(A[i])
        dic[val] = index
        lst.append(A[i])
    # else:
    dic[A[i]] = i
        # lst.append(A[i])
    print(A)
print(A)
