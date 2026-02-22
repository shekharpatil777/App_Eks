class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize the lowest price to a very high number
        # and the max profit to 0
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # If we find a new floor, update our min_price
            if price < min_price:
                min_price = price
            # Otherwise, check if selling today gives us a better profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit