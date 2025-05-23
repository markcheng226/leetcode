# Last updated: 3/23/2025, 6:03:42 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid +1
                else:
                    r = mid -1
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid -1
                else:
                    l = mid+1
        return -1