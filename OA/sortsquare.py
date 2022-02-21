A =  [ -855, -847, -747, -708, -701, -667, -666, -618, -609, -536, -533, -509, -500, -396, -336, -297, -284, -229, -173, -173, -132, -38, -5, 35, 141, 169, 281, 322, 358, 421, 436, 447, 478, 538, 547, 644, 667, 673, 705, 711, 718, 724, 726, 811, 869, 894, 895, 902, 912, 942, 961 ]

i = 0
lst = []
print(len(A))
while A[i]<0:
    i+=1
f = i
s = i-1
for i in range(len(A)):
    if f<len(A) and s>=0:
        if abs(A[f]) > abs(A[s]):
            lst.append(A[s]**2)
            s-=1
        else:
            lst.append(A[f]**2)
            f+=1
        
    else:
        # print(f,len(A),s)
        if f<len(A):
            while f<len(A):
                lst.append(A[f]**2)
                f+=1
        else:
            while s>=0:
                lst.append(A[s]**2)
                s-=1   
print(len(lst))