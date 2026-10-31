class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        path = []

        def dfs(i, path):
            if i == len(s):
                res.append(path.copy())
                return

            for j in range(i, len(s)):
                if ispali(i,j):
                    path.append(s[i:j+1])
                    dfs(j+1, path)
                    path.pop()


        def ispali(i, j):
            while i < j:
                if s[i] == s[j]:
                    i+=1
                    j-=1
                else:
                    return False

            return True

        dfs(0, path)
        return res
