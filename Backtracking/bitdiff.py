final = []
temp = []
A = [ 10,1,2,7,6,1,5]
A = sorted(list(A))
val= 8
lst = []
def solution (A,val,final,sum,flag,i):
    # print(final,sum,flag)
    # if i>=len(A):
    #     return
    if sum == val:
        if list(final) not in temp:
            temp.append(list(final))
        return 
    if sum>val:
        # final = []
        return
    
    
    for i in range(i,len(A)):
        if sum+A[i]<=val:
        # if 
            final.append(A[i])
            # sum+=A[i]
            solution(A,val,final,sum+A[i],flag,i+1)
            # sum-=A[i]
            final.pop()
        # for j in range(len(A)):
            
print(solution(A,val,final,0,0,0))
print(temp)
# check = set()
# for i in temp:
    

 
