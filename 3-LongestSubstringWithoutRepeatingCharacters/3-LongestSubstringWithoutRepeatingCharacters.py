# Last updated: 10/13/2025, 5:28:41 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        res = 0

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left +=1
            seen.add(s[i])
            res = max(res,i-left+1)
        return res