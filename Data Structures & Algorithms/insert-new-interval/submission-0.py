class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals:
            lastEnd = res[-1][1]

            if start<= lastEnd:
                res[-1][1] = max(end, lastEnd)
            else:
                res.append([start,end])
        return res