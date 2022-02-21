A  = [ -50, -41, -40, -19, 5, 21, 28 ]
B =  [ -50, -21, -10 ]
front = 0
front2 = 0
# flag1 = 0
# flag2 = 0
lst = []

while front<=len(A)-1 or front2<=len(B)-1:
    print(front,front2)
    # print("fronts ",A[front],B[front2])
    if front == len(A) and front2!=len(B):
        front2+=1
        lst.append(B[front2])
        continue
    if front2 == len(B) and front!=len(A):
        
        lst.append(A[front])
        front+=1
        continue
    if A[front] > B[front2]:
        lst.append(B[front2])
        front2+=1
    else:
        lst.append(A[front])
        front+=1
    print(lst)
print(lst)
length = len(lst)

if length%2==0:
    index1 = length//2-1
    index2 = (length//2)
    median = (lst[index1]+lst[index2])/2.0
else:
    median = lst[length//2]
print(median)