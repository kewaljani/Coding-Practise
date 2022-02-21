temp = '11'
N=2
second = ""
count = 1
while N<3:    
    for i in range(len(temp)-1):
        # print()
        if temp[i+1] == temp[i]:
            count+=1
        else:
            second+=str(count)+str(temp[i])
            count = 1
    if temp[-1]!=temp[-2]:
        second+=str(temp[-1])+str(1)
    if second == "":
        second+=str(count)+str(temp[i])

    temp = second
    print(temp)
    # second = ""
    # print(second)
    N+=1
