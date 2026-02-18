class Solution:
    def maxProfit(self, prices):
        mi = prices[0]
        profit = 0

        for price in prices:
            if price < mi:
                mi = price
            else:
                diff = price - mi
                if diff > profit:
                    profit = diff

        return profit

