A =[ 9488, 25784, 5652, 9861, 31311, 8611, 1671, 7129, 28183, 2743, 11059, 4473, 7927, 21287, 2259, 7214, 32529 ]
temp = 0
max = A[0]
for i in range(len(A)):
    fix = A[i]
    count = 0
    flag = 0
    
    # print("fix =",fix)
    # print("max = ",max)
    if fix > max:
        max = fix
        for j in range(i+1,len(A)):
            # print(A[j])
            if fix<A[j]:
                # print("proper") 
                continue
            else:
                flag = 1
                # print("improper")
                break
        if flag == 0:
            print(A[i])
            temp = 1  
print(temp)
