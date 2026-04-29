class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # If no houses → no money to rob
        # WHY: Edge case
        if not nums:
            return 0

        # If only one house → rob it
        # WHY: No adjacent constraint issue
        if len(nums) == 1:
            return nums[0]

        # dp[i] → maximum money we can rob from houses [0...i]
        # WHY: Store best result up to each index to avoid recomputation
        dp = [0] * len(nums)

        # Base case: only first house available
        dp[0] = nums[0]

        # Base case: choose best between first and second house
        # WHY: Cannot rob both (adjacent constraint)
        dp[1] = max(nums[0], nums[1])

        # Fill DP array
        for i in range(2, len(nums)):
            
            # Two choices at each house:
            # 1. Skip current house → take dp[i-1]
            # 2. Rob current house → nums[i] + dp[i-2]
            # WHY: If we rob current, we must skip previous house
            
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        # Final answer = max money we can rob from all houses
        return dp[-1]