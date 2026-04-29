class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = { i: [] for i in range(N) }
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1, N):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visit = set()
        minHeap = [[0,0]]

        while len(visit) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            visit.add(i)
            res+=cost

            for nCost, n in adj[i]:
                if n not in visit:
                    heapq.heappush(minHeap, [nCost, n])
        return res