# Last updated: 7/3/2025, 6:04:27 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k,len(nums)):
            window_sum += nums[i] - nums[i-k]

            max_sum = max(max_sum,window_sum)
        
        return max_sum/k