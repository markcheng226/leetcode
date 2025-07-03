# Last updated: 7/3/2025, 5:32:30 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxn = curn = 0

        for i in range(len(s)):
            
            if s[i] in "aeiou":
                curn +=1

            if i < k-1:
                continue
        
            maxn = max(maxn,curn)

            if s[i-k+1] in "aeiou":
                curn -=1
        
        return maxn