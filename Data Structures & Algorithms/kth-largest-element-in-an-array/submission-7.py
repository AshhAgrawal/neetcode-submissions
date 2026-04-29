from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k   # convert kth largest to index in sorted order
        l, r = 0, len(nums) - 1

        while l <= r:
            pivot = nums[r]   # choose last element as pivot
            p = l             # p is the position where next smaller element goes

            # partition: move all elements <= pivot to the left side
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            # place pivot at its correct sorted position
            nums[p], nums[r] = nums[r], nums[p]

            # if pivot index is the target index, return answer
            if p == k:
                return nums[p]

            # target is on the right side
            elif p < k:
                l = p + 1

            # target is on the left side
            else:
                r = p - 1

        return -1