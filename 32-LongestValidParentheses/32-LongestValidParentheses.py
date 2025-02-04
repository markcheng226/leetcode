class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right ,res =0,0,0

        for c in s:
            if c == "(":
                left +=1
            else:
                right +=1
            if left==right:
                res = max(res,left*2)
            if left<right:
                left = right = 0
        left = right = 0

        for c in reversed(s):
            if c == ")":
                right +=1
            else:
                left +=1
            if left == right:
                res = max(res,left*2)
            if right < left:
                left = right =0
        return res
