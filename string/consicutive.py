A = "aabbccd"
B = 2
mainstr = ""
sub = ""
if B == 1:
    print("")
count = 1
front = 1
while front<len(A):
    # print(count)
    print(A[front])
    if A[front]==A[front-1]:
        count+=1
    else:
        front+=1
        count = 1
    if count==B:
        print("inside = ",A[front])
        A = A.replace(A[front],'')
        print(A[front])
        count = 1
        front=1
print(A)