class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        sell = 0
        hold = float('-inf')
        prev_sell = 0

        for price in prices:
            old_sell = sell
            sell = max(sell, hold + price)
            hold = max(hold, prev_sell - price)
            prev_sell = old_sell

        return sell