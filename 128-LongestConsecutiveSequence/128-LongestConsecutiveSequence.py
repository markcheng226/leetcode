# Last updated: 10/10/2025, 10:27:43 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        numsSet = set(nums)

        for i in numsSet:
            if i -1 not in numsSet:
                length = 1
                while i + length in numsSet:
                    length +=1
                res = max(res,length)
        return res