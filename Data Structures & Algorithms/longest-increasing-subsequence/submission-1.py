class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1 , len(nums)):
                print(nums[i], nums[j])
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
            print(nums)
            print(dp)
        
        return max(dp)


"""
len(nums) = 7
[9, 1, 4, 2, 3, 3, 7]

dp[6] = 
dp[5] = 
dp[4] = 
dp[3] = 
dp[2] = 
dp[1] = 
dp[0] = 

"""
