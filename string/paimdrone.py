class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self,A,l,r):
        while l<r:
            if A[l]==A[r]:
                l+=1
                r-=1
            else:
                return 0
        return 1
            
    def solve(self, A):
        if len(A)==1 or self.isPalindrome(A,0,len(A)-1):
            return 0
        A=A[::-1]
        target=A[0]
        print(target)
        for i in range(1,len(A)):
            if A[i]==target:
                if self.isPalindrome(A,0,i):
                    return len(A)-1-i
                else:
                    return len(A)-1
        return len(A)-1
A = "abede"
temp = Solution()
print(temp.solve(A))