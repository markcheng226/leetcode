# Last updated: 10/26/2025, 9:53:21 PM
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l,i=0,0
        res = []
        q = deque()

        while i < len(nums):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
                
            q.append(i)

            if l > q[0]:
                q.popleft()

            if (i-l+1) == k:
                res.append(nums[q[0]])
                l +=1
            i+=1
        return res