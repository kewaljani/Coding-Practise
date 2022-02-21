A = [ 0 ]
if len(A)==1:
    print(0)
A.append('X')
temp = []
for i in range(len(A)-1):
    if A[i]!=A[i+1]:
        temp.append(A[i])
for i in range(len(temp)):
    A[i] = temp[i]
print(len(temp))