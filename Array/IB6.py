a=[]
b=[]
for i in range(len(A)):
    a.append(A[i]+i)
    b.append(A[i]-i)
print(max(max(a)-min(a),max(b)-min(b)))