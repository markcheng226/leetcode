# Last updated: 3/24/2025, 3:53:52 PM
class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        total,count = 0,0

        for i in range(len(usageLimits)):
            total += usageLimits[i]
            if total >= ((count+1)*(count+2))/2:
                count +=1
        return count