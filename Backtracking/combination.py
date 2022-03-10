
temp = []
final= []

def solve(A,temp,final,i,B):
    # print(temp)
    if len(temp) == B:
        final.append(list(temp))
        return

    for i in range(i,len(A)):
        temp.append(A[i])
        solve(A,temp,final,i+1,B)
        temp.pop()
A = 1
B = 1
A = list(range(1,A+1))
solve(A,temp,final,0,B)
print(final)