class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cur = ""
        res = []
        if not digits:
            return []

        mp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(digitI, cur):
            if digitI == len(digits):
                res.append(cur)
                return

            for i in range(len(mp[digits[digitI]])):
                cur += mp[digits[digitI]][i]
                dfs(digitI+1, cur)
                cur = cur[:-1]


        dfs(0, "")
        return res