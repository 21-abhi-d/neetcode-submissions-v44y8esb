class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def backtrack(openB, closeB, stack):
            if openB == closeB == n:
                ret.append("".join(stack))
                return
            
            if openB < n:
                stack.append("(")
                backtrack(openB + 1, closeB, stack)
                stack.pop()
            
            if openB > closeB:
                stack.append(")")
                backtrack(openB, closeB + 1, stack)
                stack.pop()

        backtrack(0, 0, [])

        return ret