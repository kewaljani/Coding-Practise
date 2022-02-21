A =  [[1,2,3],[4,5,6],[7,8,9]]
r=len(A) 
c=len(A[0])
ans=[]
for i in range(r):
    curr=[]
    row=0
    col=i
    while col>=0:
        curr.append(A[row][col])
        row=row+1
        col=col-1
    ans.append(curr)
   
print(ans)