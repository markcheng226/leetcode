class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        res = 0
        while len(s) > 1:
            i = s.index(s[-1])
            if i == len(s)-1:
                res += i//2
            else:
                res+=i
                s.pop(i)
            s.pop()
        return res