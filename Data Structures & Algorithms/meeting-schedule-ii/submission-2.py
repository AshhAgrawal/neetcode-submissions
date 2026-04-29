class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # Extract all start times into a separate list
        # WHY: We only care about the order in which meetings start (timeline view),
        # not which specific meeting object they belong to.
        start = sorted([i.start for i in intervals])

        # Extract all end times into a separate list
        # WHY: We want to always know the earliest meeting that finishes,
        # so we can decide if a room becomes free.
        end = sorted([i.end for i in intervals])

        # s → pointer to next meeting start
        # e → pointer to next meeting end
        # WHY: We simulate time by comparing next start vs next end
        s = 0
        e = 0

        # count → current number of active meetings (rooms in use)
        # res → maximum rooms needed at any time (final answer)
        count = 0
        res = 0

        # We process all meeting starts one by one
        # WHY: Every new start forces us to decide → new room or reuse?
        while s < len(intervals):

            # If the next meeting starts BEFORE the earliest one ends
            # → overlap → we cannot reuse any room → need a new room
            if start[s] < end[e]:
                count += 1      # occupy one more room
                s += 1          # move to next start time

            else:
                # If start[s] >= end[e]
                # → at least one meeting has finished already
                # → we can reuse that room
                count -= 1      # free one room
                e += 1          # move to next ending time

            # Update the maximum number of rooms used simultaneously
            # WHY: This represents the peak overlap → minimum rooms needed
            res = max(res, count)

        # Final answer = maximum rooms ever needed at once
        return res