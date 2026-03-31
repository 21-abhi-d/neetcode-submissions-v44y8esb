class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ret = []

        def backtrack(open_num, closed_num):
            # Base case: Stack fully built, need to join for return value
            if open_num == closed_num and open_num == n:
                ret.append("".join(stack))
                return

            # Recursive case 2: Adding closed brackets 
            # as long as they are less than open_num.
            if closed_num < open_num:
                stack.append(")")
                backtrack(open_num, closed_num + 1)
                stack.pop()

            # Recursive case 1: Adding open brackets 
            # as long as they are less than n.
            if open_num < n:
                stack.append("(")
                backtrack(open_num + 1, closed_num)
                stack.pop()

        

        backtrack(0, 0)
        return ret


"""
stack = [(, (, (, ), ), )]


"""