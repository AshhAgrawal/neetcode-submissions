class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start = sorted([i.start for i in intervals]) 
        end = sorted([i.end for i in intervals]) 
        s = e = res = count = 0

        while s < len(start):

            if start[s]<end[e]:
                count+=1
                s+=1
            else:
                count-=1
                e+=1
            res = max(res, count)
        return res
        