class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) > 1:
            rob1a, rob2a = 0, 0
            for i in range(0, len(nums) - 1):
                tmp = max(nums[i] + rob1a, rob2a)
                rob1a = rob2a
                rob2a = tmp

            rob1b, rob2b = 0, 0
            for i in range(1, len(nums)):
                tmp = max(nums[i] + rob1b, rob2b)
                rob1b = rob2b
                rob2b = tmp
            
            return max(rob2a, rob2b)
        else:
            return nums[0]

