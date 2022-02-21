class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, weights, days):
        def is_enough(capacity):  #helper function, to check if given capacity is enough
            count = 1
            print()
            max_weight = capacity
            
            for w in weights:
                print("max = ",max_weight)
                if w > max_weight:
                    print("inside this",w)
                    max_weight = capacity
                    count += 1
                max_weight -= w
            return  count <= days

        l, r = max(weights), sum(weights)

        print(l,r)
        while l < r:
            m = (l+r) // 2
            print("m =",m )
            if is_enough(m):
                r = m
            else:
                l = m+1
            
        return l
temp = Solution()
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = 5
x = temp.solve(A,B)
# print(x)