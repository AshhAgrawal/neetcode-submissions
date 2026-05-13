class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        r = len(prices)

        for i in range(1, r):
            profit = prices[i] - prices[i-1]
            total = max(total+profit, total)  
        return total          