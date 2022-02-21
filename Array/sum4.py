nums = [1,0,-1,0,-2,2]
target = 0
nums.sort()
print(nums)
f = 2
l = len(nums)-1
for i in range(len(nums)-3):
    f = i+2 
    l = len(nums)-1
    for j in range(i+1,len(nums)-2):
        while f<l:
            if nums[i]+nums[j]+nums[f]+nums[l] == target:
                print("available")
                print(nums[i],nums[j],nums[f],nums[l])
                break
            elif nums[i]+nums[j]+nums[f]+nums[l]> target:
                l-=1
            else:
                f+=1
    