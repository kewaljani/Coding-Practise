A =         [ [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]]
row= set()
col = set() 
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j]==0:
            row.add(i)
            col.add(j)
print(row,col)

for i in range(len(A)):
    for j in range(len(A[0])):
        if i in row:
            A[i][j] = 0
            continue
        if j in col:
            A[i][j] = 0
print(A)
