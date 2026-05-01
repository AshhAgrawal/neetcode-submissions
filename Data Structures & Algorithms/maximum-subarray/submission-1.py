class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxCurr = nums[0]
        curr = 0
        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            maxCurr = max(curr, maxCurr)
        return maxCurr