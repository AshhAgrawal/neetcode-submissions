class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Result array initialized with 0
        # WHY 0? → default means no warmer day exists in future
        res = [0] * len(temperatures)

        # Stack will store [temperature, index]
        # WHY? → we need index to compute number of days difference
        # It will be a MONOTONIC DECREASING stack (temps decreasing)
        stack = []

        for i, t in enumerate(temperatures):

            # If current temperature is higher than stack top,
            # we found a "warmer day" for previous elements
            # WHY loop? → current temp might resolve multiple previous days
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()

                # Calculate how many days waited for a warmer temperature
                # WHY i - stackIndex? → distance between current day and previous day
                res[stackIndex] = (i - stackIndex)

            # Push current temperature and its index
            # WHY? → this day is waiting for a future warmer day
            stack.append([t, i])

        # Remaining elements in stack have no warmer future → already 0
        return res