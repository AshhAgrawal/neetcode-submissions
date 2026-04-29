class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # Two pointers: start from both ends
        # WHY: Maximum width initially → try to maximize area
        l = 0
        r = len(heights) - 1

        # resarea → store maximum water area found
        resarea = 0
 
        # Continue until pointers meet
        while l < r:

            # Calculate area between l and r
            # width = (r - l)
            # height = min of both lines (shorter one limits water)
            area = (r - l) * min(heights[l], heights[r])

            # Update maximum area
            resarea = max(resarea, area)

            # Move the pointer with smaller height
            # WHY:
            # - Area is limited by smaller height
            # - Moving taller one won't help increase area
            # - We try to find a taller boundary on the smaller side
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return resarea