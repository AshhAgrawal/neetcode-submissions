class CountSquares:

    def __init__(self):
        # Dictionary to count how many times each point appears
        # WHY: Same point can be added multiple times → affects number of squares
        self.ptsCount = defaultdict(int)

        # List of all points added
        # WHY: Needed to iterate through all possible diagonal points
        self.pts = []

    def add(self, point: List[int]) -> None:
        # Convert to tuple since lists are not hashable
        # WHY: Required to use as key in dictionary
        self.ptsCount[tuple(point)] += 1

        # Store point for future iteration
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0

        # Current point (potential corner of square)
        px, py = point

        # Iterate through all previously added points
        # WHY: Treat each as a possible diagonal point of square
        for x, y in self.pts:

            # Check if (px,py) and (x,y) can form a diagonal of a square
            # Conditions:
            # 1. Distance in x and y must be equal → forms square
            # 2. Not in same row or column → avoids degenerate case
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue

            # If valid diagonal:
            # We need the other two corners:
            # (x, py) and (px, y)

            # Multiply counts because:
            # - Each point can appear multiple times
            # - Combinations = count1 * count2
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]

        return res