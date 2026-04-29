class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # prices[i] → minimum cost to reach node i
        # Initialize all to infinity (unreachable)
        prices = [float("inf")] * n

        # Cost to reach source is 0
        prices[src] = 0

        # We relax edges at most k+1 times
        # WHY k+1? → k stops = k+1 edges
        for i in range(k + 1):

            # Create a copy to avoid overwriting current iteration results
            # WHY? → ensures we only use results from previous iteration
            tempPrices = prices.copy()

            # Relax all edges (Bellman-Ford step)
            for s, d, p in flights:

                # If source node is unreachable, skip
                if prices[s] == float("inf"):
                    continue

                # Check if going through s gives a cheaper cost to d
                # WHY? → core relaxation step
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s] + p

            # Update prices after processing all edges
            prices = tempPrices

        # If destination is still unreachable, return -1
        return -1 if prices[dst] == float("inf") else prices[dst]