class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


# sliding windows: left, right pointers
# keep track of all the non duplicate characters and its previous index that came mp

        left, right = 0, 0
        mp = {}
        length = 0

        while (right < len(s)):
            if (s[right] in mp):
                left = max(mp[s[right]]+1, left)

            mp [s[right]] = right
            length = max(length, right - left +1)
            right+=1

        return length












            


    





