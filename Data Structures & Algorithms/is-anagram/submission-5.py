class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            mp[s[i]] = mp.get(s[i],0)+1
            mp[t[i]] = mp.get(t[i],0)-1


        for c in mp:
            if mp[c] != 0:
                return False

        return True