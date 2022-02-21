A = [ 1, 7, 67, 133, 178 ]
B = 1

for i in range(1,len(A)):
    if A[i-1]>A[i]:
        pivot = i
        low1 = 0
        high1 = pivot-1
        low2 = pivot
        high2 = len(A)-1
        break
else:
    pivot = len(A)
    low1,low2 = 0,0
    high1,high2 = pivot-1,pivot-1
print(i)
if len(A)==1:
    if A[0]==B:
        print(0)
    else:
        print(-1)
# low1 = 0
# high1 = pivot-1
# low2 = pivot
# high2 = len(A)-1
print(low1,high1,low2,high2)
if A[high2]<B:
    print("inside")
    while low1<=high1:
        
        mid = low1+(high1-low1)//2
        # print(mid)
        if A[mid]==B:
            print(mid)
            print("found")
            break
        elif A[mid]>B:
            high1 = mid-1
        elif A[mid]<B:
            low1 = mid+1
# print(A[high1])
elif A[high1]>B:
    while low2<=high2:
        
        mid = low2+(high2-low2)//2
        print(mid)
        if A[mid]==B:
            print("found")
            break
        elif A[mid]>B:
            high2 = mid-1
        elif A[mid]<B:
            low2 = mid+1

print("not found")
