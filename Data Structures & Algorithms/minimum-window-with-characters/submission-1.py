class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""

        count_t = defaultdict(int)

        for c in t:
            count_t[c]+=1

        count_s = defaultdict(int)
        res_length = float("inf")
        res = [-1,-1]
        l=0
        have = 0
        need = len(count_t)
        for r in range(len(s)):
            count_s[s[r]]+=1
            if s[r] in count_t and count_s[s[r]] == count_t[s[r]]:
                have+=1

            while have == need:
                if (r-l+1) < res_length:
                    res = [l,r]
                    res_length = r - l +1

                count_s[s[l]]-=1
                
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have-=1
                l+=1

        l, r = res
        return s[l:r+1] if res_length != float("inf") else ""


        