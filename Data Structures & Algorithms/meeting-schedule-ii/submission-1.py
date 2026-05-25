"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        minh = []
        m = 0

        for i in intervals:
            if len(minh) > 0 and minh[0] <= i.start:
                heapq.heappop(minh)
            heapq.heappush(minh, i.end)
            m = max(m, len(minh))
        
        return m

        