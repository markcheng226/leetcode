# Last updated: 7/3/2025, 6:15:32 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_max = sum(nums[:k])
        max_max = window_max

        for i in range(k,len(nums)):
            window_max += nums[i] -nums[i-k]

            max_max = max(window_max,max_max)
        
        return max_max / k