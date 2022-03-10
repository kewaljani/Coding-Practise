n = 8
final = []
temp = []
def nqueen(n,final,temp,row,current):
    # print(temp)
    if row<=n:
        if ispossible(temp,current):
            # print(temp)
            # print("yeahh")
            pass
        else:
            return
    if row ==n:
        final.append(list(temp))
        return
    for i in range(n):
        temp.append([row,i])
        current = [row,i]
        nqueen(n,final,temp,row+1,current)  
        temp.pop()



def ispossible(temp,current):
    # print("inside")
    # print(temp,current)
    
    for i in range(len(temp)-1):
        # print(i,current)
        dy = abs(current[1]-temp[i][1])
        dx = abs(current[0]-temp[i][0])
        if current[0] == temp[i][0] or current[1]==temp[i][1] or dx == dy:

            return False
    else:
        return True 



nqueen(n,final,temp,0,[])
# print(final[0])
final2 = []
ans = []
temp2 = []
final[0]
count = 0
string = ""
for x in final:
    print(x)
    for i in range(n):
        for j in range(n):
            # print(x[][lcount],x[rcount],i,)
            if i==x[count][0] and  j == x[count][1]:
                string+="Q"
            else:
                string+="."
        count+=1
        final2.append(string)
        string =""
    count = 0
    ans.append(final2)
    final2 = []
print(ans[0])
# for i in 