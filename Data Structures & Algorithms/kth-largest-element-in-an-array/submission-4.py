from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert kth largest to index in sorted ascending order
        target = len(nums) - k

        left, right = 0, len(nums) - 1

        while left <= right:
            # Pick a random pivot index to reduce chance of worst-case partition
            pivot_index = random.randint(left, right)

            # Move chosen pivot to the end so partition logic stays simple
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            pivot = nums[right]
            p = left  # p marks where the next smaller/equal element should go

            # Partition the current subarray
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            # Put pivot into its final correct position
            nums[p], nums[right] = nums[right], nums[p]

            # If pivot lands exactly at target index, that is our answer
            if p == target:
                return nums[p]

            # If target index is on the right side, move left boundary
            elif p < target:
                left = p + 1

            # If target index is on the left side, move right boundary
            else:
                right = p - 1

        return -1  # This line should never be reached for valid input