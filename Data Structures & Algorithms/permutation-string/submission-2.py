class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1)>len(s2)):
            return False


        ls_s1 = [0] * 26
        ls_s2 = [0] * 26
        l = 0
        r = len(s1)-1

        for i in range(r+1):
            ls_s1[(ord(s1[i])-ord('a'))]+=1
            ls_s2[(ord(s2[i])-ord('a'))]+=1

        while(r < len(s2)):
            if ls_s1 == ls_s2:
                return True

            ls_s2[(ord(s2[l])-ord('a'))]-=1
            l+=1
            r+=1
            if(r == len(s2)):
                break
            ls_s2[(ord(s2[r])-ord('a'))]+=1


        return False