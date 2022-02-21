
A = [7, 13, 8, 2, 3]
N = len(A)
bit = [0 for i in range(32)]
print(bit)
for i in range(N):
    print("new", A[i])
    x = 31
    while(A[i] > 0):
        
        if (A[i] & 1 == 1):
            bit[x] += 1
        A[i] = A[i] >> 1
        print("ans = ",A[i],bit[x])
        x -= 1
    print(bit)    
print(bit)