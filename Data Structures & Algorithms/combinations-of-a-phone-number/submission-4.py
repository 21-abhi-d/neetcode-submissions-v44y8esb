class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        digToChar = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        def dfs(i, combination):
            if i == len(digits): 
                ret.append("".join(combination))
                return

            for char in digToChar[digits[i]]:
                combination.append(char)
                dfs(i + 1, combination)
                combination.pop()



        dfs(0, [])
        return ret if ret != [""] else []

        
