A = "sfzhppjyibudzcjbaiuvhfbp"
temp = A[::-1]+'_'+A
j =0
lsp = [0 for i in range(len(temp))]
for i in range(1,len(lsp)):
    while j!=0 and temp[i]!=temp[j]:
        j = lsp[j-1]
    if temp[i] == temp[j]:
        lsp[i] = j+1
        j+=1
    else:
        lsp[i] = 0
print(lsp)
print(len(A)-lsp[-1])