class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Search space for k (eating speed)
        # WHY:
        # Minimum speed = 1 (slowest possible)
        # Maximum speed = max(piles) (finish largest pile in 1 hour)
        l, r = 1, max(piles)

        # Store best (minimum valid) speed found
        res = r

        # Binary search on answer space (k)
        # WHY:
        # As k increases → hours needed decreases (monotonic relationship)
        while l <= r:

            # Try middle speed
            k = (l + r) // 2

            # Calculate total hours needed at speed k
            hours = 0
            for p in piles:
                
                # For each pile:
                # hours = ceil(p / k)
                # WHY:
                # Even if only a few bananas remain, it still takes 1 full hour
                hours += math.ceil(p / k)

            # If we can finish within h hours → valid speed
            if hours <= h:
                
                # Try to minimize k (we want smallest valid speed)
                res = min(res, k)

                # Search left half for smaller valid k
                r = k - 1

            else:
                # If too slow (takes more than h hours)
                # → increase speed
                l = k + 1

        # Return smallest valid speed found
        return res