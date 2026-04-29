class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get number of rows and columns
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # We will first binary search on rows
        # WHY: Each row is sorted and first element of row > last element of previous row
        top = 0
        bot = ROWS - 1

        # Step 1: Find the correct row where target could exist
        while top <= bot:
            row = (top + bot) // 2  # Middle row
            
            # If target is greater than the last element of this row,
            # it must be in rows below
            if target > matrix[row][-1]:
                top = row + 1
            
            # If target is smaller than the first element of this row,
            # it must be in rows above
            elif target < matrix[row][0]:
                bot = row - 1
            
            # Otherwise, target lies within this row range
            else:
                break
        
        # If no valid row found, target does not exist
        if not (top <= bot):
            return False
        
        # Step 2: Binary search within the identified row
        l, r = 0, COLS - 1
        
        while l <= r:
            m = (l + r) // 2  # Middle column
            
            # If target is greater, search right half
            if target > matrix[row][m]:
                l = m + 1
            
            # If target is smaller, search left half
            elif target < matrix[row][m]:
                r = m - 1
            
            # Found target
            else:
                return True
        
        # Target not found in the row
        return False