A = [1,2,3]

temp= []
final= []
def perm(A,i,temp,final,length):
    print(temp)
    if len(temp) == length:
        # temp = []
        final.append(list(temp))
        return 
    for i in range(len(A)):
        temp.append(A[i])
        temp2 = A[i]
        A.remove(A[i])
        perm(A,0,temp,final,length)
        A.append(temp2)
        A = A[::-1]
        temp.pop()

length = len(A)
x=  perm(A,0,temp,final,length)
print(final)