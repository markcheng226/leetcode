class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]
        cur = []
        wordDict = set(wordDict)

        def backtrack(i):
            if i == len(s):
                res.append(" ".join(cur))
                return
                
            for j in range(i,len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    cur.append(w)
                    backtrack(j+1)
                    cur.pop()
        backtrack(0)
        return res
                    