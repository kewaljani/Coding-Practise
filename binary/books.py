A = [12, 34, 67, 90]
B = 2

min,max = A[len(A)-1],sum(A)
temp_sum = 0
current_sum = 0
count = 1
min_sum = 0
fmin = 100000000
print(min,max)
# while min<max:
for i in range(10):
    current_sum = 0
    temp_sum = 0
    min_sum = 0
    count = 1
    mid = max-min//2
    print(mid)
    for i in range(len(A)):
        # print("temp sum =",temp_sum)
        if temp_sum+A[i]>mid:
            # current_sum += temp_sum
            temp_sum = A[i]
            count+=1
            # if current_sum>min_sum:
            #     min_sum = current_sum
        else:
            temp_sum+=A[i]
    
    # print(min_sum)
    if count>B:
        print("not possibl")
        break
    if count<= B:
        result = mid
        max = mid-1
    else:
        min = mid+1
    # else:
    #     max = mid-1
    print("max = ",max,"mid = ",mid,"min = ",min,"fmin = ",fmin,"count = ",count)
    # break
print(result)
