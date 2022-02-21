S =  [ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ]
target = -1
S.sort()
flag =0
print(S)
minyet = 10000
for i in range(len(S)-2):
    if flag == 1:
        break
    top = i+1
    low = len(S)-1
    while top<low:
        sum = S[top]+S[low]+S[i]
        print(S[i],S[top],S[low] , "sum = ",sum)
        print(abs(sum-target),minyet)
        if abs(sum-target)<=abs(minyet):
            minyet = sum-target
            minsum = sum
        # print(sum,target)
        if sum== target:
            minsum = sum
            flag = 1
            break
        if sum>target:
            low-=1
        elif sum<target:
            top+=1
print(minsum)