class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, path):
            if i == len(s):
                res.append(path.copy())

            for j in range(i, len(s)):
                
                if ispali(s, i, j):
                    path.append(s[i:j+1])
                    backtrack(j+1, path)
                    path.pop()


        def ispali(s, j, i):
            while j < i:
                if s[j] == s[i]:
                    j+=1
                    i-=1

                else:
                    return False
            return True

        backtrack(0, [])
        return res

