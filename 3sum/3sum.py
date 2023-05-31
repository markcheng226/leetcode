class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i]>0:
                return result
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            l=i+1
            r=len(nums)-1

            while r > l:
                sums = nums[i]+nums[l]+nums[r]

                if sums < 0:
                    l +=1
                elif sums >0 :
                    r -=1
                else:
                    result.append([nums[i],nums[l],nums[r]])

                    while r >l and nums[l]==nums[l+1]:
                        l +=1
                    while r > l and nums[r] == nums[r-1]:
                        r -=1
                    r-=1
                    l +=1
        
        return result

        