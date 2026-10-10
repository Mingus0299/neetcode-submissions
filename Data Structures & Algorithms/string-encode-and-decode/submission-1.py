class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append(",")

        res.append("#")

        res.extend(strs)

        return ''.join(res)



    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        c = 0
        sizes = []
        res = []
        while(s[c] != "#"):
            start = c
            while(s[c] != ","):
                c+=1
            sizes.append(int(s[start:c]))
            c+=1
        c+=1
        
        for sz in sizes:
            res.append(s[c:c+sz])
            c+=sz

        return res



