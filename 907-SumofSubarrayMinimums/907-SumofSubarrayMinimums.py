class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        Mod = 10**9+7
        n = len(arr)

        stack = []
        left = n*[-1]
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack = []
        right = n * [n]
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        res = 0
        for i in range(n):
            leftCount = i - left[i]
            rightCount = right[i] -i
            res += arr[i] * leftCount * rightCount
            res %= Mod
        return res