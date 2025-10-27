# Last updated: 10/26/2025, 8:29:46 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""
        
        need = Counter(t)
        missing = len(t)
        l = 0
        best_len = float("inf")
        best_l = 0

        for i in range(len(s)):
            ch = s[i]
            need[ch] -=1
            if need[ch] >= 0:
                missing -=1
            

            while missing == 0:
                if i-l+1<best_len:
                    best_len = i-l+1
                    best_l = l
                
                left_ch = s[l]
                need[left_ch]+=1
                l +=1
                if need[left_ch] > 0:
                    missing +=1
        return "" if best_len == float("inf") else s[best_l:best_l+best_len]


