class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Convert list to set for O(1) lookups
        # WHY: We need fast existence checks for consecutive numbers
        unique = set(nums)
        
        streak = 0  # Stores the maximum length of consecutive sequence found

        # Iterate through original list (can also iterate through set)
        for i in nums:
            
            # Check if 'i' is the start of a sequence
            # WHY: Only start counting if (i-1) does NOT exist
            # This avoids recomputing sequences multiple times
            if (i - 1) not in unique:
                
                length = 1  # Current sequence length starts at 1 (just 'i')
                
                # Expand the sequence forward
                # WHY: Check if next consecutive numbers exist
                while (i + length) in unique:
                    length += 1
                
                # Update maximum streak
                streak = max(length, streak)
        
        return streak