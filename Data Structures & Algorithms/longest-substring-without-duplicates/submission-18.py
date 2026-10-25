class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(list)
        start = 0
        
        length = 0

        for i, c in enumerate(s):
            if c in mp:
                start = max(start, mp[c]+1)

            length = max(length, i - start+1)
            mp[c] = i

        return length
            
