# Last updated: 7/3/2025, 5:39:38 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxn = curn = 0
        vowel = "aeiou"

        for i in range(len(s)):
            if s[i] in vowel:
                curn +=1
            
            if i < k-1:
                continue
            
            maxn = max(maxn,curn)

            if s[i-k+1] in vowel:
                curn -=1
        
        return maxn
            