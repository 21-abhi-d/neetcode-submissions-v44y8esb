class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def dfs(openB, closeB, combination):
            if openB == closeB == n:
                ret.append("".join(combination))
                return
            
            if openB < n:
                combination.append("(")
                dfs(openB + 1, closeB, combination)
                combination.pop()

            if closeB < openB:
                combination.append(")")
                dfs(openB, closeB + 1, combination)
                combination.pop()
            

        dfs(0, 0, [])
        return ret