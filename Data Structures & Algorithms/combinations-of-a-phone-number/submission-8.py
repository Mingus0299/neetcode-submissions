class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        mp  = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def dfs(digi, comb):
            if len(comb) == len(digits):
                res.append(comb)
                return

            for i in range(len(mp[digits[digi]])):
                c = mp[digits[digi]][i]
                dfs(digi+1, comb+c)

        if digits:
            dfs(0, "")

        return res
                
