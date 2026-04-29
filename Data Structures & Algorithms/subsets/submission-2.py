class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []      # stores all subsets
        subset = []   # current subset being built

        def dfs(i):
            # Base case: reached end of array
            # WHY? → one complete subset is formed
            if i >= len(nums):
                # Add a copy (important!)
                # WHY copy? → subset is modified later, so we need a snapshot
                res.append(subset.copy())
                return

            # Decision 1: include nums[i]
            subset.append(nums[i])   # choose element
            dfs(i + 1)               # explore further
            subset.pop()             # backtrack (undo choice)

            # Decision 2: exclude nums[i]
            # WHY? → explore subsets without current element
            dfs(i + 1)

        # Start recursion from index 0
        dfs(0)
        return res