# Last updated: 10/26/2025, 3:27:27 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        numsSet = set(nums)

        for num in numsSet:
            if num -1 not in numsSet:
                length = 1
                while num + length in numsSet:
                    length +=1
                res = max(res,length)
        return res
