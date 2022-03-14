flag = 0
curr_len=0
A = [0, 1, 1, 0, 0, 1]
length = -100
sum = 0
for i in range(len(A)):
    if A[i]==1:
        flag = 1
    if flag == 1:
        
        if A[i] == 1:
            sum+=1
        if A[i] == 0:
            sum-=1
        if sum <=0:
            sum = 0
            curr_len = 0
            if curr_len>length:
                length = curr_len
            continue
        curr_len+=1
        print(length,sum,i)

        if curr_len>length:
            length = curr_len
print(length)