A = [5, -2, 3 , 1, 2]
B = 3
ft = 0
lt = len(A)-1
sum = 0
for i in range(B):
    if A[ft]>=A[lt]:
        sum = sum+A[ft]
        ft+=1
    else:
        sum = sum+A[lt]
        lt-=1
print(sum)