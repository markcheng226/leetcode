class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        Sum = 0
        res = float("inf")

        for j in range(len(nums)):
            Sum += nums[j]
            while Sum >= target:
                res = min(res, j-i+1)
                Sum -= nums[i]
                i +=1
        return 0 if res == float("inf") else res