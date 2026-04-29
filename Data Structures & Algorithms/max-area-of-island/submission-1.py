class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # area → stores maximum island area found
        area = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        # DFS function to calculate area of an island starting from (r, c)
        def dfs(r, c):

            # Base case: stop if
            # 1. Out of bounds
            # 2. Cell is water (0) or already visited
            # WHY: Only land cells (1) contribute to area
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return 0

            # Mark current cell as visited
            # WHY: Avoid revisiting same cell → prevents infinite loops
            grid[r][c] = 0

            # Count current cell (1) + explore all 4 directions
            # WHY: Island = connected land horizontally/vertically
            return (
                1 +
                dfs(r + 1, c) +   # down
                dfs(r - 1, c) +   # up
                dfs(r, c + 1) +   # right
                dfs(r, c - 1)     # left
            )

        # Traverse entire grid
        for r in range(ROWS):
            for c in range(COLS):

                # If land is found, compute island area using DFS
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))

        return area