class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Queue to store all initially rotten oranges
        # WHY: BFS starts from all rotten oranges simultaneously (multi-source BFS)
        q = collections.deque()

        # fresh → count of fresh oranges remaining
        # time → minutes passed
        fresh = time = 0

        # Traverse grid to:
        # 1. Count fresh oranges
        # 2. Add all rotten oranges to queue (starting points)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1      # count fresh oranges
                if grid[r][c] == 2:
                    q.append([r, c])  # enqueue rotten ones
        
        # Directions for 4-directional movement (down, up, right, left)
        # WHY: Rot spreads only to adjacent cells (not diagonals)
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        # BFS: process level by level (each level = 1 minute)
        # Continue while:
        # 1. There are fresh oranges left
        # 2. There are rotten oranges to spread infection
        while fresh > 0 and q:

            # Number of oranges that will spread rot in this minute
            # WHY: Process current level fully before incrementing time
            qLen = len(q)

            for i in range(qLen):
                r, c = q.popleft()

                # Try all 4 directions
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    # Skip if:
                    # 1. Out of bounds
                    # 2. Not a fresh orange
                    # WHY: Only fresh oranges can become rotten
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                        continue

                    # Convert fresh → rotten
                    # WHY: This orange is now infected
                    grid[row][col] = 2

                    # Add it to queue so it can infect others next minute
                    q.append([row, col])

                    # Decrease fresh count
                    fresh -= 1

            # After processing one full layer → 1 minute passed
            time += 1

        # If all fresh oranges are rotted → return time
        # Otherwise → some oranges couldn't be reached → return -1
        return time if fresh == 0 else -1