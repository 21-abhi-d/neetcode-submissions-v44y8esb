class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_lsc = 0

        for num in nums:
            lcs = 1
            while (num - 1) in seen:
                lcs += 1
                num -= 1
            max_lsc = max(max_lsc, lcs)
        
        return max_lsc
            
            





"""
seen = (2, 20, 4, 10)

nums = [2, 20, 4, 10, 3, 4, 5]
                         i

lcs = 3





"""
