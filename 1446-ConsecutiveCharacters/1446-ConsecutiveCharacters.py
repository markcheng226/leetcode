# Last updated: 7/10/2025, 9:31:21 PM
class Solution:
    def maxPower(self, s: str) -> int:
        max_len = 0
        count = 0

        for i in range(0,len(s)):
            if s[i] == s[i-1]:
                count +=1
            else:
                count = 1
            max_len = max(max_len,count)
        return max_len
