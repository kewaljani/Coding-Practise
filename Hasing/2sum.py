dic = dict()
A  = [ -10, -10, -10 ]
B  =  -5

for i in range(len(A)):
    if B-A[i] in dic:
        print(dic[B-A[i]],i)
    if A[i] not in dic:
        dic[A[i]] = i
print(-1)