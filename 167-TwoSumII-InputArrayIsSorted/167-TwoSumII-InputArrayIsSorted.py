# Last updated: 10/7/2025, 3:03:42 AM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1

        while l < r:
            if numbers[l]+ numbers[r] > target:
                r -=1
            elif numbers[l]+ numbers[r] < target:
                l +=1
            else:
                return [l+1,r+1]