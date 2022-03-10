s = "aab"
temp =[]
final= []
def recursive(s,temp,final,i):
    print(temp)
    if i>=len(s):
        final.append(list(temp))
        return
    for j in range(i,len(s)):
        # print(s,i,j)
        if ispalimdron(s,i,j):
            temp.append(s[i:j+1])
            recursive(s,temp,final,j+1)
            temp.pop()
def ispalimdron(s,l,r):
    while l<r:
        if s[l]!=s[r]:
            return False
        l,r = l+1,r-1
    return True
recursive(s,temp,final,0)
print(final)