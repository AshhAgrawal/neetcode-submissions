class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # dp[(i, buying)] → max profit starting from day i
        # buying = True  → we can buy
        # buying = False → we must sell (we are holding a stock)
        dp = {}

        def dfs(i, buying):
            # Base case: no days left
            if i >= len(prices):
                return 0

            # Return cached result if already computed
            if (i, buying) in dp:
                return dp[(i, buying)]

            # Option 1: cooldown (do nothing)
            # WHY? → skip current day
            cooldown = dfs(i + 1, buying)

            if buying:
                # Option 2: buy stock
                # WHY subtract price? → spending money
                buy = dfs(i + 1, False) - prices[i]

                # Choose best between buying or skipping
                dp[(i, buying)] = max(buy, cooldown)

            else:
                # Option 2: sell stock
                # WHY +prices[i]? → gain money
                # WHY i+2? → cooldown day after selling
                sell = dfs(i + 2, True) + prices[i]

                # Choose best between selling or skipping
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        # Start at day 0, with option to buy
        return dfs(0, True)