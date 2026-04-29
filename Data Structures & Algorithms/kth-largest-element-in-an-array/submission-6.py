from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        l, r = 0, len(nums) - 1

        while l <= r:
            pivot = r

            # Move chosen pivot to the end so partition logic stays simple
            nums[pivot], nums[r] = nums[r], nums[pivot]

            pivot = nums[r]
            p = l  # p marks where the next smaller/equal element should go

            # Partition the current subarray
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            # Put pivot into its final correct position
            nums[p], nums[r] = nums[r], nums[p]

            # If pivot lands exactly at k index, that is our answer
            if p == k:
                return nums[p]

            # If k index is on the r side, move l boundary
            elif p < k:
                l = p + 1

            # If k index is on the l side, move r boundary
            else:
                r = p - 1

        return -1  # This line should never be reached for valid input