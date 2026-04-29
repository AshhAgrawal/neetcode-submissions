class Solution:
    def trap(self, height: List[int]) -> int:
        l =0
        r = len(height) -1
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        while l<r:
            if height[l] < height[r]:
                l+=1
                leftMax = max(height[l],leftMax)
                res+= leftMax - height[l]
            else:
                r-=1
                rightMax = max(height[r],rightMax)
                res+= rightMax-height[r]
        return res