# Last updated: 10/23/2025, 6:25:58 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False