# Last updated: 7/8/2025, 12:48:27 AM
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
        