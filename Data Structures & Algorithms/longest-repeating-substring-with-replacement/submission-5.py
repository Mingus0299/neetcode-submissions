class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxfrequency = 0
        ans = 0
        l = 0
        mp = {}

        for r in range(len(s)):
            
            mp[s[r]] = mp.get(s[r],0) + 1
            maxfrequency = max(maxfrequency, mp[s[r]])
            lenght = r-l + 1

            if (lenght - maxfrequency > k):
                mp[s[l]]-=1
                l+=1

        
            ans = max(r-l + 1, ans)

        return ans





