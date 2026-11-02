class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        count = 0
        mp = defaultdict(int)
        l=0
        for r in range(len(s)):
            mp[s[r]]+=1
            count = max(count, mp[s[r]])

            while (r-l+1) - count > k:
                
                mp[s[l]]-=1
                l+=1

            max_length = max(max_length, r-l+1)
        return max_length