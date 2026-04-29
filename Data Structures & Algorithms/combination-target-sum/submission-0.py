class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combination = []
        res = []

        def dfs(i, remaining):
            if i == len(nums):
                return
            if remaining<0:
                return
            if remaining ==0:
                res.append(combination.copy())
                return
            combination.append(nums[i])
            dfs(i, remaining - nums[i])
            combination.pop()
            dfs(i+1, remaining)

        dfs(0, target)
        return res #check