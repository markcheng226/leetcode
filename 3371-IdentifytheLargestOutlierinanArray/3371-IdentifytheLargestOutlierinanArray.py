class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        count = Counter(nums)
        res = float("-inf")

        for num in nums:
            count[num] -=1
            totalsum -= num
            if totalsum % 2 == 0 and count[totalsum//2] >0:
                res = max(res,num)
            count[num] +=1
            totalsum +=num
        return res
