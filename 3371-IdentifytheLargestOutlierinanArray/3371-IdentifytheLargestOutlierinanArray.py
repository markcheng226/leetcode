class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        outlier = float("-inf")
        totalsum = sum(nums)
        count = Counter(nums)

        for i in range(len(nums)):
            count[nums[i]] -=1
            totalsum -= nums[i]

            if totalsum % 2 == 0 and count[totalsum//2]>0:
                outlier = max(nums[i],outlier)
            count[nums[i]] +=1
            totalsum += nums[i]
        return outlier