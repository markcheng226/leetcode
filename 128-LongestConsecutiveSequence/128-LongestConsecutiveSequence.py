# Last updated: 10/26/2025, 3:28:53 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for i in numSet:
            if i-1 not in numSet:
                length = 1
                while i + length in numSet:
                    length +=1
                res = max(res,length)
        return res