class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def painter(self,A, C, maxTime):
        painter = 1
        s=0
        for i in C:
            s+=i
            if s>maxTime:
                painter+=1
                s=i
        return painter
            
    def paint(self, A, B, C):
        low = max(C)
        high = sum(C)
        minTime = float('inf')
        while(low<=high):
            mid = (low+high)//2
            painter = self.painter(A,C,mid)
            print(painter,mid)
            if painter > A:
                low = mid + 1
            else:
                minTime = mid
                high = mid - 1
        return (minTime*B)% 10000003
A = 10
B = 1
C = [1, 8, 11, 3]
temp = Solution()
print(temp.paint(A,B,C))
