class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Initialize two pointers
        l = 0
        r = len(height) - 1
        
        # Track maximum height seen so far from left and right
        # WHY: Water at a position depends on the smaller of leftMax and rightMax
        leftMax = height[l]
        rightMax = height[r]
        
        res = 0  # Stores total trapped water
        
        # Process until pointers meet
        while l < r:
            
            # Decide which side to process
            # WHY:
            # If left height is smaller, leftMax is the limiting factor
            # So we can safely calculate water at left side
            if height[l] < height[r]:
                
                l += 1  # Move left pointer inward
                
                # Update leftMax
                # WHY: Keep track of tallest wall on left
                leftMax = max(height[l], leftMax)
                
                # Water trapped = leftMax - current height
                # WHY: Water level is bounded by leftMax on this side
                res += leftMax - height[l]
            
            else:
                # Process right side similarly
                r -= 1  # Move right pointer inward
                
                # Update rightMax
                rightMax = max(height[r], rightMax)
                
                # Water trapped = rightMax - current height
                res += rightMax - height[r]
        
        return res