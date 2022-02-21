def Solve(x):
    for i in range(1,int(x)+1):
        temp = input()
        A = input().split(" ")
        # C = input().split(" ")
        if temp == 1:
            print("Case #%d:"%i,end=" ")
            print(1)
            continue
        papers = 0
        print("Case #%d:"%i,end=" ")
        print(1, end=" ")
        minimum = 1
        for i in range(1,len(A)):
            papers =0
            count = 0
            for j in range(i,-1,-1):
                # print("inside",count,A[j])
                if int(A[j])>=i+1 or int(A[j])>minimum :
                    count+=1
                if count>i+1:
                    break
            
            minimum  = max(minimum,papers+count)

            print(minimum ,end=" ")
        print()
A = [1 ,3 ,3 ,2, 2 ,15]           
x = input()
Solve(x)