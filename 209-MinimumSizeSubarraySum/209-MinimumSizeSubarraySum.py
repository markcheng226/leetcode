# Last updated: 7/8/2025, 1:00:23 AM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        res = float('inf')
        

        for i in range(len(nums)):
            total += nums[i]

            while total >= target:
                res = min(res,i-left+1)
                total -=nums[left]
                left +=1
        return 0 if res == float("inf") else res            