class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # LIS[i] → length of longest increasing subsequence starting at index i
        # Initialize all to 1
        # WHY? → every element alone is a subsequence of length 1
        LIS = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS)