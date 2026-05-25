class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0

