# Last updated: 7/10/2025, 11:26:21 PM
class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        max_len = 1
        
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count +=1
            else:
                count = 1
            
            max_len = max(max_len,count)
        return max_len
