class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # l → left boundary, r → right boundary
        # WHY: We process the matrix layer by layer (outer → inner)
        l, r = 0, len(matrix) - 1

        # Process each square layer
        while l < r:

            # Iterate over elements in current layer (excluding last one)
            # WHY: Each iteration rotates one "group of 4" elements
            for i in range(r - l):

                # Define top and bottom row indices for current layer
                top, bottom = l, r

                # Save top-left value (will be overwritten)
                # WHY: Needed to complete the 4-way swap
                topLeft = matrix[top][l + i]

                # Move bottom-left → top-left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom-right → bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move top-right → bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move saved top-left → top-right
                matrix[top + i][r] = topLeft

            # Move inward to next layer
            # WHY: After completing outer layer, process inner square
            r -= 1
            l += 1