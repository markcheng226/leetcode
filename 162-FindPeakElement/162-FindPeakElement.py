# Last updated: 9/20/2025, 12:11:56 AM
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0,len(nums)-1

        if len(nums) == 1:
            return 0

        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                #nums[mid] < nums[mid+1]
                l = mid + 1
        return l 