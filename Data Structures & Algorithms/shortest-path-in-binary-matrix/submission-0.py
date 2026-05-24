class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        N = len(grid)
        q = deque([(0, 0, 1)])
        visited = set((0,0))
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        while q:
            r, c, l = q.popleft()
            if r < 0 or c < 0 or r >= N or c >= N or grid[r][c] == 1:
                continue
            if r == N - 1 and c == N - 1:
                return l
            for dr, dc in directions:
                if ((r+dr, c+dc) not in visited):
                    q.append((r+dr, c+dc, l + 1))
                    visited.add((r+dr, c+dc))
        return -1
