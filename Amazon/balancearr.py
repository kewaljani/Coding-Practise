A = [5, 5, 2, 5, 8]
final = 0
leve =0
reve,rodd = 0,0
lodd = 0
for i in range(len(A)):
    if i%2==0:
        reve+=A[i]
    else:
        rodd+=A[i] 

print(reve,rodd)
for index,each_element in enumerate(A):
    if (index % 2) == 0:
        reve -= each_element
        if (leve + rodd) == (lodd + reve):
                final += 1
        leve += each_element
    else:
        rodd -= each_element
        if (leve + rodd) == (lodd + reve):
                final += 1
        lodd += each_element
print(final)

