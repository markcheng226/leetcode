// Last updated: 3/22/2025, 8:31:10 AM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        numsSet = set(nums)

        for i in range(1,len(nums)+1):
            if i not in numsSet:
                res.append(i)
        return res
