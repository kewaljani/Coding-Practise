A = [3, 5, 4, 2]
class Solution:
    def maximumGap(self, A):
        array = list(range(len(A)))
        array.sort(key = lambda i:A [i])
        maxDistance = 0
        print(array)
        minSofar = array[0]
        for i in array:
            if i <= minSofar:
                minSofar = i
            else:
                maxDistance = max(maxDistance,i - minSofar)
        return maxDistance
temp = Solution()
print(temp.maximumGap(A))
# index = 0
# for i in range(len(A)):
#     for j in range(i+1,len(A)):
#         if A[j]>=A[i]:
#             index = max(index,j-i)
# print(index)