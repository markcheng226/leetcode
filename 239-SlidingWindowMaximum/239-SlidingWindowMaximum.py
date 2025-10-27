# Last updated: 10/26/2025, 9:59:49 PM
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        l,i = 0,0
        q = deque()

        while i < len(nums):
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            if l > q[0]:
                q.popleft()

            if i -l + 1 == k:
                res.append(nums[q[0]])
                l +=1
            i+=1
        return res
