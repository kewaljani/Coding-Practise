A = [3, 6, 8, 10, 15, 50]
B = 5
dic = dict()
count = 0
for i in range(len(A)):
    if A[i]^B in dic:
        count+=1
        # return 1
    dic[A[i]] = 1
else:
    print(0)
print(count)