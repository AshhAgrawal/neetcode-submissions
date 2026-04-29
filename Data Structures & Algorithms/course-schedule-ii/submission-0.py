class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()
        output = []
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return []
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in preMap[crs]:
                if  not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
