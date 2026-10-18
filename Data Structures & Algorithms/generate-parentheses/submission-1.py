class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        res = []


        def dfs(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                opened+=1
                dfs(opened, closed)
                opened-=1
                stack.pop()

            if closed < opened:
                stack.append(")")
                closed+=1
                dfs(opened, closed)
                closed-=1
                stack.pop()

        dfs(0, 0)
        return res