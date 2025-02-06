class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSub = 0
        maxSub = nums[0]

        for num in nums:
            if curSub < 0 :
                curSub = 0
            
            curSub += num
            maxSub = max(curSub,maxSub)
        return maxSub