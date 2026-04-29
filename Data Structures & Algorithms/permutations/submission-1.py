from typing import List  # Import List type for type hints

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []  # This will store all permutations

        def backtrack(nums, idx):
            # If idx reaches end, one full permutation is formed
            if idx == len(nums):
                res.append(nums[:])  # Append a copy of current permutation
                return  # Stop further recursion

            # Loop through all possible elements to place at position idx
            for i in range(idx, len(nums)):

                # Swap element at idx with element at i
                # WHY → fix nums[i] at current position idx
                nums[idx], nums[i] = nums[i], nums[idx]

                # Recurse for next index (next position)
                backtrack(nums, idx + 1)

                # Swap back to restore original state
                # WHY → backtracking (undo the choice)
                nums[idx], nums[i] = nums[i], nums[idx]

        backtrack(nums, 0)  # Start recursion from index 0
        return res  # Return all generated permutations