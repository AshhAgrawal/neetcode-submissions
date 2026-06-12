class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = float("-inf")

        l = 0
        r = len(heights)-1

        while l<r:
            area = max(area,((r-l) * min(heights[l],heights[r])))
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return area 

