class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up position and speed
        # WHY? → we need both to compute time to reach target
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = [] 

        # Sort cars by position and process from closest to target → farthest
        # WHY reverse? → cars ahead affect cars behind (not vice versa)
        for p, s in sorted(pair)[::-1]:

            # Compute time for current car to reach target
            # WHY time? → fleets are determined by whether cars meet before target
            time = (target - p) / s

            # Add current car's time to stack
            stack.append(time)

            # If current car reaches earlier or same time as car ahead,
            # it will catch up and form a fleet
            # WHY compare with previous? → stack[-2] is the fleet ahead
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # Merge fleet → remove current car's time
                # WHY pop? → it joins the fleet ahead, so no new fleet formed
                stack.pop()

        # Number of fleets = number of distinct times left in stack
        return len(stack)