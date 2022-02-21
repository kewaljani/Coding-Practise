A = [ -4, 3 ]
B = [ -2, -2 ]
front =0
last = 0
temp = []
while front!=len(A) and last!=len(B):
    if A[front]<=B[last]:
        temp.append(A[front])
        front+=1
    else:
        temp.append(B[last])
        last+=1
while front!=len(A):
    temp.append(A[front])
    front+=1
while last!=len(B):
    temp.append(B[last])
    last+=1
# print(temp)
A = []
for i in range(len(temp)):
    A.append(temp[i])
print(A)