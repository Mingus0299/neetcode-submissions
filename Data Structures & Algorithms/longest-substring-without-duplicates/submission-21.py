class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        start = 0
        res = 0


        for i in range(len(s)):
            if s[i] in mp:
                start = max(start, mp[s[i]]+1)

            res = max(i-start+1, res)
            mp[s[i]] = i

        return res

            
