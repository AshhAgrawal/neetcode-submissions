class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS, COLS = len(matrix), len(matrix[0])

        # Flag to track if first row needs to be zeroed
        # WHY: matrix[0][0] is shared by first row & first column,
        # so we need a separate variable to handle first row
        rowZero = False

        # Step 1: Use first row and first column as markers
        for r in range(ROWS):
            for c in range(COLS):

                if matrix[r][c] == 0:
                    # Mark column
                    matrix[0][c] = 0

                    if r > 0:
                        # Mark row
                        matrix[r][0] = 0
                    else:
                        # If zero is in first row, mark separately
                        rowZero = True

        # Step 2: Use markers to update inner matrix (excluding first row/col)
        for r in range(1, ROWS):
            for c in range(1, COLS):

                # If row or column is marked, set cell to zero
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Step 3: Handle first column
        # WHY: matrix[0][0] acts as marker for first column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # Step 4: Handle first row separately
        # WHY: We used rowZero flag to avoid conflict with matrix[0][0]
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0