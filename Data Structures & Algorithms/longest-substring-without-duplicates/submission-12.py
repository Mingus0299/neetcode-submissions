class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        i, j = 0, 0
        ans = 0

        while(j < len(s)):
            if s[j] in mp:
                i = max(mp[s[j]]+1,i)

            ans = max(ans, j-i+1)
            mp[s[j]] = j
            j+=1

        return ans

                