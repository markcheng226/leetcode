class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i,j,k=0,len(nums)-1,len(nums)-1
        ans = [0] * len(nums)
        while i<=j:
            leftmax = nums[i] ** 2
            rightmax = nums[j] * nums[j]
            if leftmax > rightmax:
                ans[k] = leftmax
                i +=1
            else:
                ans[k] = rightmax
                j-=1
            k-=1
        return ans