class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        visited = set()
        def dfs(r,c):
            if (r<0 or c<0 or r>=ROWS or c>=COLS or (r,c) in visited or grid[r][c] == -1):
                return
            visited.add((r,c))
            q.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if grid[r][c] != 0:
                    grid[r][c] = dist
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r, c-1)
            dist +=1