# Last updated: 7/5/2025, 11:26:50 PM
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_count = Counter(p)
        s_count = Counter()

        for i in range(len(s)):
            s_count[s[i]] +=1

            if i >= len(p):
                if s_count[s[i-len(p)]] == 1:
                    del s_count[s[i-len(p)]]
                else:
                    s_count[s[i-len(p)]] -=1
            
            if s_count == p_count:
                res.append(i-len(p) +1)
        return res
