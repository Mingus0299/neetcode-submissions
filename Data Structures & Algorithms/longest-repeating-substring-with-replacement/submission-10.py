class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_count = 0
        l = 0
        mp = defaultdict(int)

        for r in range(len(s)):
            mp[s[r]]+=1
            max_count = max(max_count, mp[s[r]])

            while r-l+1 - max_count  > k:
                mp[s[l]]-=1
                l+=1

            max_length = max(max_length, r-l+1)

        return max_length