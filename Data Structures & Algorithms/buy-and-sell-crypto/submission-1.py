class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # l → buy day (minimum price so far)
        # r → sell day (current day)
        l = 0
        r = 0
        
        maxP = 0  # Stores maximum profit found
        
        # Traverse through prices
        while r < len(prices):
            
            # If current price is higher than buy price → profit possible
            if prices[l] < prices[r]:
                
                # Calculate profit if we sell at day r
                profit = prices[r] - prices[l]
                
                # Update maximum profit
                maxP = max(profit, maxP)
            
            else:
                # Found a lower price → better day to buy
                # WHY: Reset buy pointer to current day
                l = r
            
            # Move to next day
            r += 1
        
        return maxP