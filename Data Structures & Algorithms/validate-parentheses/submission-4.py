class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        if len(s) < 2:
            return False

        stack = []
        for i in range(len(s)):
            if s[i] in ["(", "{", "["]:
                stack.append(s[i])
            elif stack and s[i] in [")", "}", "]"] and stack[-1] == bracket_map[s[i]]:
                stack.pop()
            else: return False

        return False if stack else True


"""
stack = [(, [, {]

"""
