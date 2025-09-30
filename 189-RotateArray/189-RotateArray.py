# Last updated: 9/30/2025, 1:06:45 AM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        
        def reversedarray(l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
        
        reversedarray(0,len(nums)-1)
        reversedarray(0,k-1)
        reversedarray(k,len(nums)-1)

        