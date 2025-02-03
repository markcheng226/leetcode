class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        outlier = float("-inf")
        totalSum = sum(nums)
        count = Counter(nums)

        for num in nums:
            count[num] -=1
            totalSum -= num
            
            if totalSum %2 == 0 and count[totalSum //2] > 0:
                outlier = max(outlier,num)
            
            count[num] +=1
            totalSum += num
        return outlier