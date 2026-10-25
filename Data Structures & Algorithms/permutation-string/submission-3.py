class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        l1 = [0] * 26
        l2 = [0] * 26

        for i in range(len(s1)):
            c2 = s2[i]
            c1 = s1[i]
            l2[ord(c2)-ord('a')]+=1
            l1[ord(c1)-ord('a')]+=1

        l = 0
        r = len(s1)-1

        while r < len(s2):
            if l1 == l2:
                return True
            
            
            r+=1
            if r < len(s2):
                l2[ord(s2[r]) - ord('a')] += 1
            l2[ord(s2[l])-ord('a')]-=1
            l+=1
        return False


