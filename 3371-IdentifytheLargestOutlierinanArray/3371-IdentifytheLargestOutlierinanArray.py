class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        res = float("-inf")
        totalsum = sum(nums)
        count = Counter(nums)

        for num in nums:
            count[num] -=1
            totalsum -= num
            if totalsum % 2==0 and count[totalsum//2]>0:
                res = max(res,num)
            count[num] +=1
            totalsum +=num
        return res