class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s):
            # off
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1
            i+=1
        i = 0
        while i < len(s)-1:
            l,r = i, i+1
            #even
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l-=1
                r+=1
            i+=1

        return res