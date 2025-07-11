# Last updated: 7/10/2025, 10:56:52 PM
class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zero = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.non_zero[i] = nums[i]
    
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in self.non_zero:
            if i in vec.non_zero:
                res += self.non_zero[i] * vec.non_zero[i]
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)