class MedianFinder:

    def __init__(self):
        # small → max heap (store negatives)
        # large → min heap
        # WHY two heaps? → split numbers into two halves
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # Always push into max heap first (as negative)
        # WHY? → assume new number belongs to lower half
        heapq.heappush(self.small, -1 * num)

        # Ensure ordering:
        # max of small ≤ min of large
        # WHY? → all elements in small must be ≤ elements in large
        if self.small and self.large and ((-self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance sizes: difference ≤ 1
        # WHY? → median depends on equal or near-equal halves
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


    def findMedian(self) -> float:
        # If one heap has more elements → median is its top
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]
        
        # If equal → average of both tops
        return ((-1 * self.small[0]) + self.large[0]) / 2