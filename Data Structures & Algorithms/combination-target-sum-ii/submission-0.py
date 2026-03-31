class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()

        def backtrack(i, cur, total):
            # Success base case
            if total == target:
                ret.append(cur.copy())
                return
            
            # Fail base case
            if total > target or i >= len(candidates):
                return
            
            # Take current candidate
            cur.append(candidates[i])
            backtrack(i + 1, cur, total + candidates[i])
            cur.pop()

            # Avoid duplicate candidate
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # Do not take current candidate
            backtrack(i + 1, cur, total)

        backtrack(0, [], 0)
        return ret