# Last updated: 10/10/2025, 10:22:29 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0

        for i in numsSet:
            if i -1 not in numsSet:
                length = 1
                while i + length in numsSet:
                    length +=1
                res = max(res,length)
        return res