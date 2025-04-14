# Last updated: 4/14/2025, 7:43:59 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicateSet = set()
        
        for num in nums:
            if num in duplicateSet:
                return True
            else:
                duplicateSet.add(num)
        return False