class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        counts = {}

        degree = 0

        minSize = 10000

        for i in range(len(arr)):
            if arr[i] not in counts:
                counts[arr[i]] = [1, i] 
            else: 

                counts[arr[i]][0] += 1

            if degree < counts[arr[i]][0]:
                degree = counts[arr[i]][0]
                minSize = i - counts[arr[i]][1] + 1

            elif degree == counts[arr[i]][0]:

                if i - counts[arr[i]][1] + 1 < minSize:
                    minSize = i - counts[arr[i]][1] + 1
        
        return minSize