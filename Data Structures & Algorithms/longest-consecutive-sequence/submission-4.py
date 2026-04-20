class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_lcs = 0
        for num in nums:
            lcs = 1
            while (num - 1) in seen:
                lcs += 1
                num -= 1
            max_lcs = max(max_lcs, lcs)
        
        return max_lcs
