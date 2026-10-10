class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        long = 0
        l = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp.get(s[r])+1)

            mp[s[r]] = r
            long = max(long,r-l+1)


        return long

# baabba
