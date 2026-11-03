class Solution:
    def partition(self, s: str) -> List[List[str]]:
        subset = []
        res = []

        def dfs(i):
            if i == len(s):
                res.append(subset.copy())
                return 
            
            for j in range(i, len(s)):
                if ispalin(i, j):
                    subset.append(s[i:j+1])
                    dfs(j+1)
                    subset.pop()

        def ispalin(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True

        dfs(0)
        return res