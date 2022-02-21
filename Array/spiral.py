A = int(input())
rows, cols = (A, A)
number_of_rows = A
number_of_columns = A
arr=[]
for x in range(number_of_rows):
   column_elements=[]
   for y in range(number_of_columns):
       # Enter the all the values w.r.t to a particular column
       column_elements.append(0)
   #Append the column to the array.
   arr.append(column_elements)
# print(arr)
total = 1
row = 0
col = 0
round = 0
temp = A
round = 0
while total<=temp*temp: 
    while col<temp-round and total<=A*A:
        # print(row,col)
        arr[row][col] = total
        col+=1
        total+=1
        # print(arr)
    # print(col)
    col-=1
    row+=1
    # print(total)
    # break
#     col-=1
#     row+=1
    while row<temp-round and total<=A*A:
        # print(row,col)
        arr[row][col]= total
        total+=1
        row+=1
        # print(arr)
    # break
    row-=1
    col-=1
    
    while col>round and total<=A*A:
        # print(row,col)
        arr[row][col] = total
        col-=1
        total+=1
        # print(arr)
   
    while row>round and total<=A*A:
        # print(row,col)
        arr[row][col] = total
        row-=1
        total+=1
        # print(arr)
    row+=1
    col+=1
    round+=1
    # print(row,col,total,temp-round)
    # break
print(arr)