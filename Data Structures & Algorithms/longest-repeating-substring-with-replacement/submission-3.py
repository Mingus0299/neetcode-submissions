class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0

        l = 0
        maxf = 0
        cnt = {}

        for r in range(len(s)):
            cnt[s[r]] = cnt.get(s[r], 0) + 1
            maxf = max(maxf, cnt[s[r]])

            while (r-l+1 - maxf > k):
                cnt[s[l]] = cnt.get(s[l]) - 1
                l+=1
                maxf = max(maxf, cnt[s[r]])

            length = max(length, r-l+1)

        return length





