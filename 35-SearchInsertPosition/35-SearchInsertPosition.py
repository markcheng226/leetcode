# Last updated: 9/21/2025, 12:35:26 AM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l <= r:
            #[0,3]
            mid = (l+r) //2
            if nums[mid] <target:
                l = mid +1
            else:
                r = mid -1
        return l