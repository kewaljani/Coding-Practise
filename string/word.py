A = "j"
ans = ""
A = A.strip()
A = A.split(" ")
print(A)
string = "" 
for i in A:
    if i=='':
        continue
    else:
        string+=i+' '
print(string)


# for i in range(len(A)-1,-1,-1):
#     # print(ans)
#     if i+1 == '' or i == 0:
#         ans = A[i]
#         continue
#     ans+=A[i]+' '
# print(ans)