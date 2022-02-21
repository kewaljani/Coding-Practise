matrix = [[1,2,3],[4,5,6],[7,8,9]]
i= len(matrix)
print(matrix)
rows, cols = (i, i)
arr=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    arr.append(col)
# print(arr)

for i in range(rows):
    for j in range(cols):
        # if i == j:
            # continue
        # else:
        arr[i][j] = matrix[j][len(matrix)-i-1]
arr = arr[::-1]
for i in range(len(arr)):
    arr[i] = arr[i][::-1]
print(arr)
