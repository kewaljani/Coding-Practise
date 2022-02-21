A = [0.6,0.7,0.8,1.2,0.4]

A.sort()
top = 0
last = len(A)-1

while top - last>2:
    mid  = top+last//2
    sum = A[top]+A[last]+A[mid]
    if A[top]+A[last]+mid>1:
        last-=1
    elif sum
