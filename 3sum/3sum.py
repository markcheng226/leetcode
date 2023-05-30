class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return result
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums)-1

            while right > left:
                sums= nums[i] + nums[left] + nums[right]

                if sums < 0:
                    left +=1
                elif sums > 0:
                    right -=1
                else:
                    result.append([nums[i],nums[left],nums[right]])

                    while right > left and nums[left] == nums[left+1]:
                        left +=1
                    while right > left and nums[right] == nums[right -1]:
                        right -=1        
                    left +=1
                    right -=1
        return result