# Last updated: 4/2/2025, 8:34:19 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()

        for i in range(len(nums)):
            if nums[i] in duplicate:
                return True
            else:
                duplicate.add(nums[i])
        return False