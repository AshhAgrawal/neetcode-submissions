class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Initialize two pointers at start and end
        l = 0
        r = len(numbers) - 1
        
        # Continue until pointers meet
        while l < r:
            
            # Calculate current sum
            currSum = numbers[l] + numbers[r]
            
            # If sum is too large, move right pointer left
            # WHY: Array is sorted → decreasing r reduces sum
            if currSum > target:
                r -= 1
            
            # If sum is too small, move left pointer right
            # WHY: Increasing l increases sum
            elif currSum < target:
                l += 1
            
            # Found the target sum
            # WHY: Return 1-based indices as required by problem
            elif currSum == target:
                return [l + 1, r + 1]
        
        # If no pair found (though problem guarantees one exists)
        return []