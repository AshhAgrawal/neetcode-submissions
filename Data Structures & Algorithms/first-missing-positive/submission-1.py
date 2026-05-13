class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums_set = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                return i

        return len(nums) + 1
