A =  [4, 1, 1, 2, 1, 3]
B = 1

count = 0
i = 0
while i<len(A):
    print(i,len(A))
    if A[i] == B:
        A.remove(A[i])
    else:
        count+=1
        i+=1
print(A)
print(count)