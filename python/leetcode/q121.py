class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize the lowest price to a very high number
        # and the max profit to 0
        min_price = float('inf')
        max_profit = 0
        
