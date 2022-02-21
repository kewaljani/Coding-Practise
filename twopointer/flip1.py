A = [ 1, 0, 0, 0, 0, 0, 1, 0, 1, 1 ]
B = 2
front = 0
last = 0
answer = 0
flip = 0


lst =None
while front<len(A):
    # print(A[front])
    print("last = ",last,"front = ",front,"flip = ",flip)
    if A[front]  == 0 and flip<B:
        flip+=1
        front+=1
    elif A[front]==0 and flip==B:
        flip+=1
    else:
        front+=1
        continue
        # front-=1
    # else:
    # front+=1
    
    # print("flip",flip)
        # continue
    if flip > B:
        # answer = max(front-last,answer)
        if front-last>answer:
            print(front,last)
            lst = list(range(last,front))
            # print(lst)
            answer = front-last
        while A[last]!=0:
            # print(last,front)
            last+=1
        last+=1
        front+=1
        flip-=1
if lst:
    if front-last>len(lst):
        print(front,last)
        print(list(range(last,front)))
    else:
        print(lst)
else:
    print(list(range(last,front)))
# print(answer)
# print(list(range(0,5)))