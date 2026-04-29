class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # maxArea → store maximum rectangle area found
        maxArea = 0

        # Stack will store (start_index, height)
        # WHY:
        # - Maintain increasing heights
        # - For each height, track how far left it can extend
        stack = []

        # Iterate through histogram bars
        for i, h in enumerate(heights):

            # Start index for current height
            # WHY: May expand left if we pop taller bars
            start = i

            # If current height is smaller → finalize rectangles for taller bars
            while stack and stack[-1][1] > h:

                # Pop taller bar
                stackIndex, height = stack.pop()

                # Calculate area with popped height
                # width = current index - start index of that height
                maxArea = max(maxArea, height * (i - stackIndex))

                # Update start to extend current bar leftward
                # WHY: Current smaller bar can extend back to where popped bar started
                start = stackIndex    

            # Push current bar with updated start index
            stack.append((start, h))

        # Process remaining bars in stack
        # WHY: These bars extend till end of histogram
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea