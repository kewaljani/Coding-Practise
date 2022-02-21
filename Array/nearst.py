A = [0, 1, 1]
B = [0, 1, 2]
path = 0
for i in range(len(A)-1):
    temp = 0
    if A[i+1]<A[i] and B[i+1]<=B[i]:
        B[i+1] = B[i+1]+2*(B[i]-B[i+1])   
    if A[i+1]<A[i] and B[i+1]>=B[i]:
        A[i+1]  = A[i+1]+2*(A[i]-A[i+1])
    if A[i+1]>=A[i] and B[i+1]<=B[i]:
        B[i+1] = B[i+1]+2*(B[i]-B[i+1])      
    if A[i+1]>=A[i] and  B[i+1]>=B[i]:
        if A[i+1]-A[i]<=B[i+1]-B[i]:
            temp = abs(A[i+1]-A[i])
            A[i] +=temp
            B[i] +=temp
            temp2 = abs(B[i+1]-B[i])
            temp = temp+temp2
        else:
            temp = B[i+1]-B[i]
            A[i]+=temp
            B[i]+=temp
            temp2 = A[i+1]-A[i]
            temp = temp+temp2
        path +=temp
print("path =",path)