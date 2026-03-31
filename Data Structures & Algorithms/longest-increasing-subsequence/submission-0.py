class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            print(dp)
        
        return max(dp)

"""
[1, 2, 4, 3]
len of nums for 3 here
dp[3] = max(1, 1 + )
dp[2]
dp[1]
dp[0]

"""
