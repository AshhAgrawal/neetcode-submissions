class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # cols[c] → set of values seen in column c
        # rows[r] → set of values seen in row r
        # squares[(r//3, c//3)] → set of values in 3x3 subgrid
        # WHY: We need to track duplicates efficiently
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        # Traverse every cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                
                # Skip empty cells
                # WHY: '.' does not contribute to constraints
                if board[r][c] == ".":
                    continue
                
                # Check if number already exists in:
                # 1. Same row
                # 2. Same column
                # 3. Same 3x3 square
                # WHY: Sudoku rules → no duplicates allowed in any of these
                if (board[r][c] in rows[r] 
                    or board[r][c] in cols[c] 
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                # Add value to row set
                rows[r].add(board[r][c])
                
                # Add value to column set
                cols[c].add(board[r][c])
                
                # Add value to corresponding 3x3 square
                # (r//3, c//3) uniquely identifies each subgrid
                squares[(r // 3, c // 3)].add(board[r][c])
        
        # If no violations found, board is valid
        return True