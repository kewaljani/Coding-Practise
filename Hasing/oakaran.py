a= [1,2,3]
b = [1,4]
queries = [[1,5],[0,0,2],[1,5]]
lst = []
for i in range(len(queries)):
    print(queries[i][0],queries,b)
    if queries[i][0] == 1:
        dic = dict()
        count = 0
        # print(queries[i][0])
        for j in range(len(a)):
            
            if a[j] in dic:
                dic[a[j]]+=1
            else:
                dic[a[j]] = 1
        for j in range(len(b)):
            if queries[i][1]-b[j] in dic:
                count+=dic[queries[i][1]-b[j]]
        lst.append(count)
        # print(count) 
        # 0
    else:
        b[queries[i][1]] += queries[i][2]
        # l
        # print(b)
print(lst)
