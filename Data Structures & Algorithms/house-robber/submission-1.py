class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            tmp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = tmp
        
        return rob2


"""
                    i
nums = [2, 9, 8, 3, 6]

dp = [2, 9, 10, 12, 16]

tmp = 16
rob1 = 12
rob2 = 16

"""


