
sumtrav = 0
count = 0
flag =0
for i in path:
    print(count,sumtrav)
    if i == 'U':
        sumtrav+=1
    elif i == 'D':
        sumtrav-=1
    if sumtrav < 0:
        flag =1 
    if flag == 1:
        if sumtrav>0:
            flag = 0
            count +=1
    print(count)