class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) > 1:
            return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        else:
            return nums[0]


    def helper(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = tmp

        return rob2

