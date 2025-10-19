# Last updated: 10/19/2025, 12:40:48 AM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid +1         
            else:
                if nums[r] >= target > nums[mid]:
                    l = mid +1
                else:
                    r = mid
        return -1
