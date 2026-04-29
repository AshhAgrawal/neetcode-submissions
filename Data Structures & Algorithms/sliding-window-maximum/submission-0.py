class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k
        res = []
        while r<len(nums)+1:
            # print(nums[l:r])
            res.append(max(nums[l:r]))
            # print(res)
            r+=1
            l+=1
        return res