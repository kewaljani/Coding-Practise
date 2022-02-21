def Solve(x):
    for i in range(1,int(x)+1):
        values, partition = input().split(" ")
        C = input().split(" ")
    
        # print((values),partition)
        sum = 0
        for j in C:
            sum +=int(j)
        
        print("Case #%d:"%i,sum%int(partition))


x = input()
Solve(x)