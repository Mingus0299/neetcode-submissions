class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} # char: index
        l = 0
        ans = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]]+1)

            ans = max(ans, r - l + 1)
            mp[s[r]] = r

        return ans