class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # Initialize boundaries of the matrix
        left = 0                      # left column index
        top = 0                       # top row index
        right = len(matrix[0]) - 1    # right column index
        bottom = len(matrix) - 1      # bottom row index
        
        out = []  # Stores spiral order result

        # Continue until boundaries cross
        # WHY: Once they cross, all elements are visited
        while top <= bottom and left <= right:

            # Traverse from LEFT → RIGHT on top row
            # WHY: First layer, top edge
            for i in range(left, right + 1):
                out.append(matrix[top][i])
            top += 1  # Move top boundary down (row consumed)

            # Traverse from TOP → BOTTOM on right column
            # WHY: Right edge of current layer
            for i in range(top, bottom + 1):
                out.append(matrix[i][right])
            right -= 1  # Move right boundary left (column consumed)

            # Traverse from RIGHT → LEFT on bottom row
            # Only if still within valid rows
            # WHY: Avoid double counting when single row remains
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    out.append(matrix[bottom][i])
                bottom -= 1  # Move bottom boundary up

            # Traverse from BOTTOM → TOP on left column
            # Only if still within valid columns
            # WHY: Avoid double counting when single column remains
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    out.append(matrix[i][left])
                left += 1  # Move left boundary right

        # Final spiral order list
        return out