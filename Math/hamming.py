ans = 0
A = [ 2, 4, 6 ]
for i in range(32):
    count = 0
    for j in range(len(A)):
        # print(count)
        # print(A[j]&1<<i)
        if A[j]&(1<<i) != 0:
            # print("yoo")
            count+=1
    ans += count*(len(A)-count)*2
print(ans)       
