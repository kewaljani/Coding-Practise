A  = "13.0"
B = "13.0.8"
A = A.split('.')
B = B.split('.')
i = 0
j = 0
while i<len(A) and j<len(B):
    if int(A[i])>int(B[j]):
        print(1)
    elif int(A[i])==int(B[j]):
        i+=1
        j+=1
    else:
        print(-1)

print(len(B),j)
if i==len(A) and j==len(B):
    print(0)
elif i==len(A):
    print(1)
else:
    print(-1)