A = [ 4, 15, 4, 4, 15, 18, 20 ]
front = 0
last = len(A)-1
lst = []
flag1 = 0
flag2 =0
comm1 = 0 
comm2 = 0
print("front=",front,"last =",last,"flag1 =",flag1,"flag2 = ",flag2,"comm1",comm1,"comm2",comm2)
while front<last and front<len(A) and last>0:
    
    if flag1==0 and flag2 ==0:
        if A[front+1]<=A[front]:
            if  A[front+1]==A[front]:
                comm1+=1
            else:    
                flag1  = 1
                front-=comm1-1
        if A[last-1]>A[last]:
            if  A[last+1]==A[last]:
                comm2+=1
            else:
                flag2 = 1
                last +=comm2+1
        comm1 = 0
        comm2 = 0
        front+=1
        last-=1
    elif flag1==0 and flag2 ==1:
        if A[front+1]<=A[front]:
            if  A[front+1]==A[front]:
                comm1+=1
            else:    
                flag1  = 1
                front-=comm1-1
        front+=1
        comm1 = 0
        
    elif flag1==1 and flag2 ==0:
        if A[last-1]>A[last]:
            if  A[last+1]==A[last]:
                comm2+=1
            else:
                flag2 = 1
                last +=comm2+1
        comm2 = 0
        last-=1
    else:
        break
    print("front=",front,"last =",last,"flag1 =",flag1,"flag2 = ",flag2,"comm1",comm1,"comm2",comm2)
if flag1==0 and flag2 ==0:
    print([-1])
print([front,last])

    


