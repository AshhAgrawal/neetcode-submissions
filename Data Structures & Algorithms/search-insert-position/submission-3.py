class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        res = len(nums)
        # if nums[0]>target:
        #     return 0
        # if nums[-1] < target:
        #     return len(nums)
        # mid = 0
        while l<=r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                l = mid+1
            elif target < nums[mid]:
                res = mid
                r = mid - 1
            
        return res