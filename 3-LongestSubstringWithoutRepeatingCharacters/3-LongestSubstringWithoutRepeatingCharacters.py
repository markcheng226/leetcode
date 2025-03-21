// Last updated: 3/21/2025, 7:49:34 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l +=1
            charSet.add(s[i])
            res = max(res,i-l+1)
        return res