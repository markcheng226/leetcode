# Last updated: 7/8/2025, 12:52:32 AM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero +=1
            
            while zero > k:
                if nums[left] == 0:
                    zero-=1
                left +=1
            
            res = max(res,i-left+1)
        return res