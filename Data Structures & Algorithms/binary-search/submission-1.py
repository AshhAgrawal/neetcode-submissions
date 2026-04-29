class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # l → left boundary, r → right boundary of search space
        l = 0
        r = len(nums) - 1

        # Continue while search space is valid
        # WHY: When l > r, target is not present
        while l <= r:

            # Find middle index
            # WHY: Binary search splits array into two halves
            mid = (l + r) // 2

            # If target found → return index
            if nums[mid] == target:
                return mid

            # If target is greater → search right half
            # WHY: Array is sorted → right side contains larger values
            elif target > nums[mid]:
                l = mid + 1

            # If target is smaller → search left half
            # WHY: Left side contains smaller values
            elif target < nums[mid]:
                r = mid - 1

        # If loop ends → target not found
        return -1