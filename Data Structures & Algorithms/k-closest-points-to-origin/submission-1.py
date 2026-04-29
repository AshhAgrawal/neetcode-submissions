class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        # Build heap with (distance, x, y)
        for x, y in points:
            # Compute squared distance from origin
            # WHY squared? → avoids sqrt, preserves relative order
            dist = (x**2) + (y**2)

            # Store distance along with point
            # WHY include dist? → heap will sort based on this
            minHeap.append([dist, x, y])

        # Convert list into heap
        # WHY? → allows efficient extraction of smallest distance
        heapq.heapify(minHeap)

        res = []

        # Extract k closest points
        while k > 0:
            # Pop smallest distance point
            dist, x, y = heapq.heappop(minHeap)

            # Add point to result
            res.append([x, y])

            k -= 1

        return res