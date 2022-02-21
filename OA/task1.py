
def count(s):

    cnt = 0
 
    for c in s:
        if c == 'a':
            cnt += 1
 
    if (cnt % 3 != 0):
        return 0
 
    res = 0
    k = cnt // 3
    sum = 0
    mp = {}
    for i in range(len(s)):
        
        if s[i] == 'a':
            sum += 1
        if (sum == 2 * k and k in mp and
            i < len(s) - 1 and i > 0):
            res += mp[k]
        if sum in mp:
            mp[sum] += 1
        else:
            mp[sum] = 1
        print(sum,s[i],mp,res)
    return res
S= 'bbbb'
print(count(S))