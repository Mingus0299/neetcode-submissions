class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opened = 0
        closed = 0

        res = []
        subset = []

        def backtrack(opened, closed):
            if n == opened == closed:
                res.append("".join(subset))
                return

            if opened < n:
                subset.append("(")
                opened+=1
                backtrack(opened, closed)
                subset.pop()
                opened-=1

            if closed < opened:
                subset.append(")")
                closed+=1
                backtrack(opened, closed)
                subset.pop()
                closed-=1

        backtrack(0, 0)
        return res
