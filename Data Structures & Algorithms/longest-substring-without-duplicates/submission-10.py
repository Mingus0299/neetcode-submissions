class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

# sliding windows: left , right
# "zxyzxyz"
#  mp to keep track of the index of all the characters seen just before

        left, right = 0,0
        answer = curr = 0
        mp = {}
        while(right < len(s)):
            if s[right] in mp:
                left = max(mp[s[right]]+ 1, left)
            mp[s[right]] = right
            curr = right - left +1  
            answer = max(answer, curr)
            right+=1
        
        return answer


            


    





