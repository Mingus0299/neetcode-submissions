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

        def dfs(digit_i,cur):
            if len(cur) == len(digits):
                res.append(cur)
            
            if digit_i >= len(digits):
                return

            for char in mp[digits[digit_i]]:
                
                dfs(digit_i+1, cur+char)
              

        dfs(0, cur)
        return res


        