class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Build adjacency list (course -> its prerequisites)
        # WHY: We need to know which courses must be taken before a given course
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()  # Courses already fully processed (no cycle found)
        output = []      # Stores the valid topological order
        cycle = set()    # Tracks current recursion path (used to detect cycles)

        def dfs(crs):
            # If course is already in current recursion stack → cycle detected
            # WHY: Visiting same node again in same path = dependency loop
            if crs in cycle:
                return False
            
            # If already processed, no need to reprocess
            # WHY: Avoid recomputation (memoization)
            if crs in visited:
                return True
            
            # Add to current recursion stack
            cycle.add(crs)
            
            # Visit all prerequisites of current course
            for pre in preMap[crs]:
                # If any prerequisite leads to a cycle → invalid
                if not dfs(pre):
                    return False
            
            # Remove from recursion stack after processing
            # WHY: We're done exploring this path
            cycle.remove(crs)
            
            # Mark course as fully processed
            visited.add(crs)
            
            # Add course to output AFTER processing prerequisites
            # WHY: Post-order DFS ensures correct topological order
            output.append(crs)
            
            return True

        # Run DFS for all courses (important for disconnected graph)
        for c in range(numCourses):
            if not dfs(c):
                return []  # Cycle found → no valid ordering
        
        # Return topological order
        return output