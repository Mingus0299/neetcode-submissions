class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        
        res = []


        def backtrack(nOpened, nClosed, stack):
            if nOpened == nClosed == n:
                res.append("".join(stack))
                return

            if nOpened < n:
                stack.append("(")
                backtrack(nOpened+1, nClosed, stack)
                stack.pop()

            if nClosed < nOpened:
                stack.append(")")
                backtrack(nOpened, nClosed+1, stack)
                stack.pop()

        backtrack(0,0,[])
        return res


                