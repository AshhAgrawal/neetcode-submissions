class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        s=0
        e = 0
        res = 0
        count = 0

        while s < len(start):
            if start[s] < end[e]:
                count+=1
                s+=1
            else:
                e+=1
                count-=1
            res = max(count, res)
        return res