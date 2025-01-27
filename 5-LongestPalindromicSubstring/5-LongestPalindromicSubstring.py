class Solution:
    def longestPalindrome(self, s: str) -> str:
        resindex = 0
        reslen = 0


        for i in range(len(s)):
            l = r = i
            while l >= 0 and r <len(s) and s[l] == s[r]:
                if (r-l+1) > reslen:

                    resindex = l
                    reslen = r-l+1
                l-=1
                r+=1
        
            l = i
            r = i+1
            while l >= 0 and r <len(s) and s[l] == s[r]:
                if (r-l+1) > reslen:
                    resindex = l
                    reslen = r-l+1
                l-=1
                r+=1
        return s[resindex:resindex+reslen]
                