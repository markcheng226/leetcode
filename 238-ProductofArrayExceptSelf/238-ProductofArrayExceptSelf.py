# Last updated: 10/10/2025, 9:24:09 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = len(nums) * [0]

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
        return res