class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = [0] * 26

        if (len(s) != len(t)):
            return False

        for i in range (len(s)):
            ls[ord(s[i]) - ord('a')]+=1
            ls[ord(t[i]) - ord('a')]-=1

        for freq in ls:
            if freq > 0:
                return False

        return True