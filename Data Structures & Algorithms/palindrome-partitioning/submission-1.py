class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        


        def dfs(i):

            if i == len(s):
                res.append(path.copy())
                return


            for j in range(i, len(s)):

                if ispali(s, i, j):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()

        def ispali(word, i, j):
            while(i < j):
                if word[i] == word[j]:
                    i+=1
                    j-=1
                    continue
                return False

            return True

        dfs(0)
        return res

            