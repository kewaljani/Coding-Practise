A = ["rrrrr", "rrrrg", "rrrrr", "bbbbb"]
for i in range(len(A)):
    for j in range(len(A[0])):
        print(A[i][j],end=" ")
    print()
print( )

for i in range(len(A[0])):
    for j in range(len(A)):
        print(A[j][i],end=" ")
    print()


