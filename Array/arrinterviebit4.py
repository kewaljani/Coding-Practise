A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
curr=0
maxseen=-9999999
for i in range(len(A)):
    curr=curr+A[i]
    print(curr, maxseen)
    if(maxseen<curr):
        maxseen=curr
    if(curr<0):
        curr=0
print(maxseen)