class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        length = len(prices)

        for i in range(length - 1):
            if prices[i + 1] > prices[i]:
                max_profit += prices[i + 1] - prices[i]

        return max_profit