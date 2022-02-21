B = 6
A = 'IDIDI'
lst = []
for i in range(1,B+1):
    lst.append(i)
print(lst)
top  = 0
last = B-1
final = []

for i in range(len(A)):
    if A[i]=='I':
        final.append(lst[top])
        top+=1
    else:
        final.append(lst[last])
        last-=1
final.append(lst[top])
print(final)