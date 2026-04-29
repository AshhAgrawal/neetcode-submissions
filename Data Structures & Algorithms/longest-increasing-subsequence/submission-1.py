class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # LIS[i] → length of longest increasing subsequence starting at index i
        # Initialize all to 1
        # WHY? → every element alone is a subsequence of length 1
        LIS = [1] * len(nums)

        # Traverse from right → left
        # WHY? → LIS[i] depends on future values LIS[j]
        for i in range(len(nums) - 1, -1, -1):

            # Check all elements to the right of i
            for j in range(i + 1, len(nums)):

                # If we can extend increasing sequence
                # WHY nums[i] < nums[j]?
                # → ensures strictly increasing
                if nums[i] < nums[j]:

                    # Update LIS[i] by extending LIS[j]
                    # WHY 1 + LIS[j]?
                    # → include current element + best sequence from j
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # Answer = maximum LIS starting from any index
        return max(LIS)