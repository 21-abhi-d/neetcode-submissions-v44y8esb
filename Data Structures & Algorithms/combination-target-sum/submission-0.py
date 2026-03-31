class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def backtrack(i, cur, total):
            if total == target:
                ret.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            cur.append(nums[i])
            # repeat i in sum calculation
            backtrack(i, cur, total + nums[i])
            cur.pop()
            # do not repeat i, go forward in nums array to avoid i
            backtrack(i + 1, cur, total)
        
        backtrack(0, [], 0)

        return ret

