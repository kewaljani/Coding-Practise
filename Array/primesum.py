A = int(input())
lst = []
prime = []

for num in range(A):
   if num > 1:
    #    print(num)
        print(num)
        for i in range(2, int(num/2)):
            print("new = ",num)
            print(i)
            if (num % i) == 0:
                #    print(num)
                break
        else:
            prime.append(num)
print(prime)
# for i in prime:
#     for j in range(len(prime),i,-1):
#         if prime[j]==A-i:
#             print([i,prime[j]])