class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        subset = []
        
        def backtracking(Opened, Closed):
            if Opened == Closed == n:
                res.append("".join(subset))
                return

            if Opened < n:
                subset.append("(")
                backtracking(Opened+1, Closed)
                subset.pop()

            if Closed < Opened:
                subset.append(")")
                backtracking(Opened, Closed+1)
                subset.pop()

        backtracking(0,0)
        return res
