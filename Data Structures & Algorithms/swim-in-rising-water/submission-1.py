class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        N = len(grid)  # Grid is N x N
        
        visit = set()  # Tracks visited cells
        # WHY: Avoid reprocessing the same cell (like Dijkstra visited set)
        
        # Min-heap: (time, row, col)
        # time = max elevation seen so far on the path
        # WHY: We always want to explore the path with minimum max elevation first
        minHeap = [[grid[0][0], 0, 0]]
        
        visit.add((0, 0))  # Mark starting cell as visited
        
        # Directions: right, left, down, up
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        # Process cells in increasing order of "time"
        while minHeap:
            
            # Get the cell with minimum current time
            t, r, c = heapq.heappop(minHeap)
            
            # If we reached bottom-right, return the time
            # WHY: First time reaching it guarantees minimum possible time (Dijkstra property)
            if r == N - 1 and c == N - 1:
                return t
            
            # Explore all 4 neighbors
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                
                # Skip invalid or already visited cells
                if (neiR < 0 or neiC < 0 or neiR == N or neiC == N 
                    or (neiR, neiC) in visit):
                    continue
                
                # Mark neighbor as visited
                visit.add((neiR, neiC))
                
                # Push neighbor into heap
                # New time = max(current path time, neighbor elevation)
                # WHY: We must wait until water level reaches the highest elevation in path
                heapq.heappush(
                    minHeap,
                    (max(t, grid[neiR][neiC]), neiR, neiC)
                )