# Last updated: 7/8/2025, 12:54:16 AM
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        res = 0
    

        for i in range(len(nums)):
            total += nums[i]

            while (i-left+1) * nums[i] - total > k:
                total -= nums[left]
                left +=1
            
            res = max(res,i-left+1)
        return res

