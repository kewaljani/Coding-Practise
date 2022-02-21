A = 18
count = 0
while A>0:
    if A&1 == 0:
        count+=1
    else:
        break
    A = A>>1
print(count)