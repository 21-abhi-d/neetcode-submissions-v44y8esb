class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0

        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        
        return max_profit
        
"""
[7, 6, 4, 3, 1]
 l  r

mp = 5
profit = 5
     
"""
            

