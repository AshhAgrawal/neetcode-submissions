class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        resarea = 0

        while l<r:
            area = (r-l) * min(heights[l], heights[r])
            resarea = max(resarea,area)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return resarea
             
