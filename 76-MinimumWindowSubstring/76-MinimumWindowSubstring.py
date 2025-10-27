# Last updated: 10/26/2025, 8:39:31 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""
        
        need = Counter(t)
        missing = len(t)
        l=0
        best_len = float("inf")
        best_l = 0

        for i in range(len(s)):
            need[s[i]] -=1
            if need[s[i]] >= 0:
                missing -=1
            
            while missing ==0:
                if i-l+1<best_len:
                    best_len = i-l+1
                    best_l=l
            
                need[s[l]]+=1
                if need[s[l]] > 0:
                    missing +=1
                l +=1
        return "" if best_len == float("inf") else s[best_l:best_l+best_len]


