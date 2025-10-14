# Last updated: 10/13/2025, 11:01:21 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = {}
        for i in t:
            need [i] = need.get(i,0) +1
        
        miss = len(t)
        left = 0
        bestlen = float("inf")
        bestleft = 0

        for i in range(len(s)):
            c = s[i]
            if c in need:
                if need[c] > 0:
                    miss -=1
                need[c] -=1

            while miss == 0:
                if i -left+1<bestlen:
                    bestlen = i-left +1
                    bestleft = left
                
                cl = s[left]
                if cl in need:
                    need[cl] +=1
                    if need[cl] > 0:
                        miss +=1
                left +=1
        return "" if bestlen == float("inf") else s[bestleft:bestleft+bestlen]