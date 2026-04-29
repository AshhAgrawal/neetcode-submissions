class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1

        # Initialize result with first element
        # WHY? → ensures we always track the minimum seen so far
        res = nums[0]

        while l <= r:

            # If current window is already sorted
            # WHY? → leftmost element is the smallest in a sorted subarray
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # Compute middle index
            m = (l + r) // 2

            # Update result with middle element
            # WHY? → minimum could be at mid
            res = min(res, nums[m])

            # Check which half is sorted
            # If left half is sorted
            if nums[m] >= nums[l]:
                # Minimum must be in right half
                # WHY? → rotation point lies to the right
                l = m + 1
            else:
                # Right half is sorted, so min is in left half
                # WHY? → rotation point lies to the left
                r = m - 1

        return res