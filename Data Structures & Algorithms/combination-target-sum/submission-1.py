class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combination = []  # current combination being built
        res = []          # stores all valid combinations

        def dfs(i, remaining):
            # If we have used all numbers
            # WHY? → no more choices left
            if i == len(nums):
                return

            # If remaining becomes negative → invalid path
            # WHY? → we exceeded target
            if remaining < 0:
                return

            # If remaining is exactly 0 → valid combination found
            if remaining == 0:
                # Add a copy of current combination
                # WHY copy? → list will change during backtracking
                res.append(combination.copy())
                return

            # Decision 1: include nums[i]
            # WHY? → we can reuse same element multiple times
            combination.append(nums[i])

            # Stay at same index i
            # WHY? → unlimited usage allowed
            dfs(i, remaining - nums[i])

            # Backtrack → remove last element
            combination.pop()

            # Decision 2: skip nums[i]
            # WHY? → move to next number
            dfs(i + 1, remaining)

        # Start DFS from index 0
        dfs(0, target)
        return res