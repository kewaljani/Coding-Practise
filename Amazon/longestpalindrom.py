def helper(self, s, left, right):
    while left>=0 and right<len(s) and (s[left]==s[right]):
        left-=1
        right+=1
    print(s[left+1:right])

def longestPalindrome(self, s: str) -> str:
    ans = ""
    for i in range(len(s)):
        odd_pos = self.helper(s, i, i)
        even_pos = self.helper(s, i, i+1)
        print(odd_pos)
        print(even_pos)
        ans = max(even_pos, odd_pos, ans, key=len)
    print(ans)