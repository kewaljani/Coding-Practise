s = [3,1 , 0 , 5 , 8 , 5]
f = [4,2 , 6 , 7 , 9 , 9]
count= 0
z = zip(s,f)
res =  sorted(z,key = lambda x: x[1])
# print(res[0][1])
remember = res[0][1]
for i in range(1,len(res)):
    if res[i][0]>remember:
        remember = res[i][1]
        count+=1
print(count)