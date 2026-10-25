class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        count = 0
        l = 0
        length = 0


        for r in range(len(s)):
            mp[s[r]] += 1
            count = max(count, mp[s[r]])

            while (r-l+1 - count) > k:
                mp[s[l]] -= 1
                l+=1
            
            length = max(length, r-l+1)

        return length