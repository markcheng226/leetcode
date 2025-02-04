class Solution:
    def longestValidParentheses(self, s: str) -> int:

        left, right, max_length = 0, 0, 0

 
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, left * 2)
            elif right > left:
                left = right = 0  

        left = right = 0
  
        for c in reversed(s):
            if c == ')':
                right += 1
            else:
                left += 1
            if left == right:
                max_length = max(max_length, left * 2)
            elif left > right:
                left = right = 0 
                
        return max_length
