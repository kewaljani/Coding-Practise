A = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
A.sort()
print(A)
lst = []
for i in range(len(A)-2):
    front = i+1
    last = len(A)-1
    while front<last:
        # print(sum)
        sum = A[i]+A[front]+A[last]
        if sum>0:
            last -=1
        elif sum<0:
            front+=1
        else:
            lst.append([A[i],A[front],A[last]])
            current = A[front]
            currl = A[last]
            print(current,currl)
            while front<last and (A[front]==current or A[last]==currl):
                
                if A[front] == current:
                    front+=1
                if A[last] == currl:
                    last-=1
                print(front,last)
        # break
        # print(front,last)
        # break
    # break 
print(lst)