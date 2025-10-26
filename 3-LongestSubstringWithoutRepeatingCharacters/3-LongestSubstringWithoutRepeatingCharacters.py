# Last updated: 10/26/2025, 5:43:09 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen = set()
        
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l +=1
            else:
                seen.add(s[i])
            res = max(res,i-l+1)
        return res
