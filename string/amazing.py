
class Solution:
    def ispal(self, s):
        return s == s[::-1]
        
    def solve2(self, A):
        match = 0
        for idx in reversed(range(1, len(A) + 1)):
            if self.ispal(A[:idx]):
                match = idx
                break
        return len(A) - match

    def gen_lsp(self, p):
        lsp = [0 for i in range(len(p))]
        j = 0
        for i in range(1, len(lsp)):
            while j != 0 and p[i] != p[j]:
                j = lsp[j - 1]
            if p[i] == p[j]:
                lsp[i] = j + 1
                j = j + 1
            else:
                lsp[i] = 0
        return lsp

    def solve(self, A):
        s = A + '_' + A[::-1]
        lsp = self.gen_lsp(s)
        return len(A) - lsp[-1]
temp = Solution()
A = "ABC"
print(temp.solve(A))