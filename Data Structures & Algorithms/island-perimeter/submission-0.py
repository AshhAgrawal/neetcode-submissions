class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(i,j):
            if i >= ROWS or j >= COLS or i<0 or j <0 or grid[i][j] == 0:
                return 1
            if (i,j) in visited:
                return 0
            visited.add((i,j))
            peri = dfs(i, j+1)
            peri += dfs(i+1, j)
            peri += dfs(i, j-1)
            peri += dfs(i-1, j)
            return peri

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    return dfs(r,c)

