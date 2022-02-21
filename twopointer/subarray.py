A = [ 5, 3, 5, 1, 3 ]
B = 2
front = 0
last = 0
length = 0
dic = dict()
while last <= len(A)-1:
    
    if A[last] in dic:
        dic[A[last]]+=1
    else:
        dic[A[last]] =1 
    
    last+=1
    if len(dic) > B:
        while len(dic)>B:
            if dic[A[front]]>1:
                dic[A[front]]-=1
            else:
                del dic[A[front]]
            front+=1
    length += last-front+1
    print(length)
print(length)