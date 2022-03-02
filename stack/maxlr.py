A  = [ 5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9 ]
stack  = []
arr = []

for i in range(len(A)):
    x = 0
    # if A[i]<stack[-1]:
    while stack and A[i]>=stack[-1][0]:
        stack.pop()
    if stack:
        x = stack[-1][1]
    arr.append(x)
    stack.append([A[i],i])
stack2 = []
arr2 = []
for i in range(len(A)-1,-1,-1):
    x = 0
    # if A[i]<stack[-1]:
    while stack2 and A[i]>=stack2[-1][0]:
        stack2.pop()
    if stack2:
        x = stack2[-1][1]
    arr2.append(x)
    stack2.append([A[i],i])
# return(arr)
# return(arr)
print(arr)
arr2 = arr2[::-1]
# print(arr2[])
print(arr2)
maximum = 0
for i in range(len(A)):
    maximum = max(maximum,arr[i]*arr2[i])
# print(arr,arr2)
print(maximum)
# print(arr2)