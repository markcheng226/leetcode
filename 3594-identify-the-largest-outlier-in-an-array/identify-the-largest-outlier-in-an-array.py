class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        totalsum=sum(nums)
        counts=Counter(nums)
        outlier=float("-inf")

        for num in nums:
            counts[num] -=1
            totalsum -= num

            if totalsum % 2 == 0 and counts[totalsum//2] > 0:
                outlier = max(outlier,num)

            counts[num] +=1
            totalsum += num
        return outlier