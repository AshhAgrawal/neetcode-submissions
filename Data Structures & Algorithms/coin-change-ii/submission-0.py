class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, curr_amount):
            if curr_amount == amount:
                return 1

            if curr_amount > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, curr_amount) in cache:
                return cache[(i, curr_amount)]

            take = dfs(i, curr_amount + coins[i])
            skip = dfs(i+1, curr_amount)

            cache[(i, curr_amount)] = take + skip
            return cache[(i, curr_amount)]
        return dfs(0,0)