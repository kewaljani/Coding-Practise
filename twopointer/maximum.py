A = [2, 5, 6]
B = 10
high = len(A)-1
low = 0
while high>low:
    print(high)
    if A[low]+A[high]>=B:
        high-=1
    else:
        subarr = high-low
        break
    
print(2**subarr)
