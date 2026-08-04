class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        # hold: maximum profit while holding a stock
        # sold: maximum profit after selling today
        # rest: maximum profit while not holding and not selling today
        hold = -prices[0]
        sold = 0
        rest = 0

        for price in prices[1:]:
            previous_hold = hold
            previous_sold = sold
            previous_rest = rest

            # Buy today or continue holding
            hold = max(previous_hold, previous_rest - price)
