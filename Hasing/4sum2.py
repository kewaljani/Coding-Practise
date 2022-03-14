A = [ 1, 1, 1, 1, 1 ]
final = []
dic = dict()
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[i]+A[j] in dic:
            # print(dic)
            for x,y in dic[A[i]+A[j]]:
                # print(A[i])
                if i in [x,y] or j in [x,y]:
                    pass
                else:
                    final.append([x,y,i,j])
            dic[A[i]+A[j]].append([i,j])
        else:
            dic[A[i]+A[j]] = [[i,j]]
            # break
final.sort()
print(final)