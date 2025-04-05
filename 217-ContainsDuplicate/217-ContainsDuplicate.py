# Last updated: 4/5/2025, 12:51:39 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for num in nums:
            if num in duplicate:
                return True
            else:
                duplicate.add(num)
        return False