A = [0]
A = A[::-1]
sum = 0

for i in range(len(A)):
    sum  = sum+A[i]*10**i
sum = sum+1
print(list(str(sum)))