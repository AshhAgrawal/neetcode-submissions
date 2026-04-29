class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all values to negative
        # WHY? → Python has min-heap, so we simulate max-heap using negatives
        stones = [-s for s in stones]

        # Build heap
        heapq.heapify(stones)

        # Continue until at most one stone remains
        while len(stones) > 1:
            # Pop two largest stones (most negative = largest original)
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            # If stones are not equal
            # WHY second > first?
            # → since values are negative, "greater" means smaller absolute value
            if second > first:
                # Push remaining stone back
                # (difference of weights, still in negative form)
                heapq.heappush(stones, first - second)

        # If no stones left, return 0
        # WHY append 0? → ensures safe access to stones[0]
        stones.append(0)

        # Convert back to positive value
        return abs(heapq.heappop(stones))