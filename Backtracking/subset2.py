final= []
temp = []
A=[9]
def solve(A,i,temp,final):
    print(temp)
    if temp not in final:
        final.append(list(temp))
    for i in range(i,len(A)):
        temp.append(A[i])
        solve(A,i+1,temp,final)
        temp.pop()
solve(A,0,final,temp)
print(temp)
# print(final)