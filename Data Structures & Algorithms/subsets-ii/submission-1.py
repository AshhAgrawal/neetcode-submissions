class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []  # stores all unique subsets

        nums.sort()  
        # WHY sort? → brings duplicates together so we can skip them easily

        def backtrack(i, subset):
            # If we've processed all elements
            if i == len(nums):
                res.append(subset.copy())  # add snapshot of current subset
                return

            # --------------------
            # Decision 1: INCLUDE nums[i]
            # --------------------
            subset.append(nums[i])          # take current element
            backtrack(i + 1, subset)        # move to next index
            subset.pop()                    # backtrack (undo inclusion)

            # --------------------
            # Skip duplicates
            # --------------------
            # Move i forward while next element is same
            # WHY? → avoid generating duplicate subsets
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            # --------------------
            # Decision 2: EXCLUDE nums[i] (after skipping duplicates)
            # --------------------
            backtrack(i + 1, subset)

        backtrack(0, [])  # start recursion
        return res