# A = [1, 1, 1, 2, 2]
A = [ 4, 6, 13, 16, 20, 3, 1, 12 ]
A.sort()
c = len(A)-1
count = 0
while c>1:
    ft = 0
    lt = c-1
    
    while ft<lt:
        print(ft,lt,c)
        if A[ft]+A[lt]>A[c]:
            count+=lt-ft
            lt-=1
        else:
            ft+=1
    c-=1
print(count)
