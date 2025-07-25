# Last updated: 7/8/2025, 11:47:17 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            if numbers[left] + numbers[right] > target:
                right -=1
            elif numbers[left] + numbers[right] < target:
                left +=1
            else:
                return [left+1,right+1]
            
            
            