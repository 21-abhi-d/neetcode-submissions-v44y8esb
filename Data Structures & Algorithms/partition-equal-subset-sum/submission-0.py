class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)

        target = sum(nums) // 2
        for i in range(len(nums) - 1, -1, -1):
            newDp = set()
            for curr in dp:
                newDp.add(curr)
                newDp.add(curr + nums[i])

            dp.update(newDp)

        return True if target in dp else False