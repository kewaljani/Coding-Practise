A = "111"
lst = []
for i in range(len(A)):
    if A[i]=='0':
        lst.append(1)
    else:
        lst.append(-1)
print(lst)
if 1 in lst:
    maxf = maxe = 0
    temp = 0
    indl = []
    for i in range(len(lst)):
        maxe = maxe+lst[i]
        if maxf<maxe:
            maxf = maxe
            findex = temp
            lindex = i 
        if maxe<0:
            maxe = 0
            temp = i+1
    indl = [findex+1,lindex+1]
    print(indl)
else:
    print("nothing")