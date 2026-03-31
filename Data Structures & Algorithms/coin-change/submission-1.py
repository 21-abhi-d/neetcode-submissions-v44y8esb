class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], 1 + dp[i - c])

        return dp[-1] if dp[-1] != (amount + 1) else -1 


"""
dp[12] = 
dp[11] = 
dp[10] = 
dp[9] = 
dp[8] = 
dp[7] = 
dp[6] = 
dp[5] = 1
dp[4] = 4
dp[3] = 3
dp[2] = 2
dp[1] = 1
dp[0] = 0

"""
