class Solution:
    def rotate(self, nums, k):
        
        n = len(nums)
        d = self.gcd(n,k)
        
        for i in range(d):
            temp = nums[i]
            for j in range(n//d):
                nums[(i-k*j)%n] = nums[(i-k*(j+1))%n]
            nums[(i-k*j)%n] = temp
        
        return
    
    def gcd(self, a, b):
        while b:
            a,b = b,a%b
        return a
