A= [1 ,2 ,3, 3, 4, 5, 6]
B= [3, 3, 5]

f,l = 0,0
temp = []
while f!=len(A) and l!= len(B):
    if A[f] == B[l]:
        temp.append(A[f])
        f+=1
        l+=1
    elif A[f]<B[l]:
        f+=1
    else:
        l+=1
print(temp)
