class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r  = max(weights), sum(weights)
        res = r

        def canShip(m):
            ships = 1
            currCap = m
            for w in weights:
                if currCap - w < 0:
                    ships+=1
                    currCap = m
                currCap -= w
            return ships<= days
    
        while l<=r:
            m = (l+r) // 2

            if canShip(m):
                r = m - 1
                res = min(res, m)
            else:
                l = m + 1
        return res