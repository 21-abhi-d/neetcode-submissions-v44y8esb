class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        max_len = 0
        for num in nums:
            length = 1
            while (num - 1) in nums_set:
                length += 1
                num -= 1
            max_len = max(max_len, length)
        
        return max_len
