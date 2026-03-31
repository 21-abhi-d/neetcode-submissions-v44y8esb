class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()

        def dfs(i, combination, total):
            if total == target:
                if combination not in ret:
                    ret.append(combination.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            combination.append(candidates[i])
            dfs(i + 1, combination, total + candidates[i])

            combination.pop()
            dfs(i + 1, combination, total)
        
        dfs(0, [], 0)

        return ret