nums = [1,2,3]
k = 5
ans=0
prefsum=0
d={0:1}
for num in nums:
    prefsum = prefsum + num

    
    if prefsum-k in d:
        ans = ans + d[prefsum-k]

    if prefsum not in d:
        d[prefsum] = 1
    else:
        d[prefsum] = d[prefsum]+1
    print(prefsum,d)
    # print(prefsum)
print(ans)