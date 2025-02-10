class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        outlier = float("-inf")
        totalnum = sum(nums)
        count = Counter(nums)

        for num in nums:
            count[num] -=1
            totalnum -= num
            if totalnum % 2==0 and count[totalnum //2 ]>0:
                outlier = max(outlier,num)
            count[num] +=1
            totalnum +=num
        return outlier