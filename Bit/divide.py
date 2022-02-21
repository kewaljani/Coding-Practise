A = [1, 2, 1, 5]
tails = [0] * len(A)
size = 0
for x in A: 
    i = 0
    j = size
    while i != j:
        m = (i+j) //2
        if tails[m] < x:
            i = m + 1
        else:
            j = m
    tails[i] = x
    print(x,size,i,tails)
    size = max(i + 1, size)
    
print(size)

