class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if not prices or k == 0:
            return 0
        
        # Optimization: If k is large enough, it's just like unlimited transactions
        # (Standard "Buy and Sell Stock II" logic)
        if k >= len(prices) // 2:
            return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))
        
        # Initialize DP arrays
        # buy[j] = max profit with j transactions and currently holding a stock
        # sell[j] = max profit with j transactions and currently not holding
        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)
        
        for price in prices:
            for j in range(1, k + 1):
                # Max profit if we buy the stock for our j-th transaction
                buy[j] = max(buy[j], sell[j-1] - price)
                
                # Max profit if we sell the stock for our j-th transaction
                sell[j] = max(sell[j], buy[j] + price)
                
        return sell[k]