
A = [ 22649, 27447, 23806, 15891, 6730, 24371, 15351, 15007, 31102, 24394, 3549, 19630, 12624, 24085 ]

ft = 0 
sum = 0
max = 0
maxs = 0
lt = len(A)-1
print(A)
for i in range(len(A)):
    if i != 0 and A[i] == A[i-1]:
        continue
    l,r = i+1,len(A)-1
    while l<r:
        sum = A[i]+A[l]+A[r]
        if sum > max:
            max = sum
        if A[l]>A[r]:
            r-=1
        else:
            l+=1
        print(A[i],A[l],A[r] , sum)
    if max > maxs :
        maxs = max
print(maxs)