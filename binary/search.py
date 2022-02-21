A = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]
B = 10
top = 0
bottom = len(A)-1
flga = 0
while top<=bottom:
    mid = top+(bottom-top)//2
    if A[mid] == B:
        flag = 1
        break 
    elif A[mid]>B:
        bottom = mid-1
    elif A[mid]<B:
        top = mid+1
pt1,pt2 = mid,mid
while A[pt1]==A[mid] and pt1>0:
        # print(pt1)
        pt1-=1
while(A[pt2]==A[mid]) and pt2<len(A)-1:
        pt2+=1
# while A[]
print(pt1+1,pt2)
