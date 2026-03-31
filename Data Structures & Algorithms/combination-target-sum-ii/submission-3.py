class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()

        def dfs(i, combination, total):
            if total == target:
                ret.append(combination.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            combination.append(candidates[i])
            dfs(i + 1, combination, total + candidates[i])
            combination.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, combination, total)
        
        dfs(0, [], 0)

        return ret