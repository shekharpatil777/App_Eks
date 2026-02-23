class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        total_profit = 0
        
        # Start from the second day
        for i in range(1, len(prices)):
            # If the price today is higher than yesterday, take the profit
