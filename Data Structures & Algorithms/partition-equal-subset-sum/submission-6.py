class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # If total sum is odd, we cannot split into two equal subsets
        # WHY: equal partition requires total sum to be divisible by 2
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2  # We need to find a subset with this sum
        
        # dp will store all possible subset sums we can achieve
        # WHY: Instead of 2D DP, we track reachable sums using a set
        dp = set()
        dp.add(0)  # Base case: sum = 0 is always possible (empty subset)

        # Iterate through numbers (reverse order not required, but fine)
        for i in range(len(nums) - 1, -1, -1):
            
            nextDp = set()  # Stores updated sums after including nums[i]
            
            # Try adding current number to all existing sums
            for t in dp:
                
                # If adding nums[i] gives target, we found valid partition
                if (t + nums[i] == target):
                    return True
                
                # Include nums[i] → new sum formed
                nextDp.add(t + nums[i])
                
                # Exclude nums[i] → keep old sum
                nextDp.add(t)
            
            # Move to next state
            dp = nextDp
        
        # Check if target sum is achievable
        return True if target in dp else False