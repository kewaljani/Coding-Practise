string = ""
A  = "abb"
def longestPalindrome(A):
    i = 0
    maxl = 0
    palen = None
    while i < len(A):
        ch = A[i]
        m = i
        
        while i+1 < len(A) and ch == A[i+1]: 
            i = i+1
        n = i
        print (i, ch, m, n)
        
        while m-1 >= 0 and n+1 < len(A) and A[m-1] == A[n+1]:
            m-=1
            n+=1
    
        l = n - m + 1
        if l > maxl:
            maxl = l
            palen = A[m:n+1]
        i+=1
    return palen
print(longestPalindrome(A))