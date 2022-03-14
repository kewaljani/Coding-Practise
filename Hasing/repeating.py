dic = dict()
A = [ 6, 10, 5, 4, 9, 120 ]
s = set(A)
if len(s) == len(A):
    print(-1)
for i in A:
    if A.count(i) > 1:
        print(i)
else:
    print(-1)
print(min)