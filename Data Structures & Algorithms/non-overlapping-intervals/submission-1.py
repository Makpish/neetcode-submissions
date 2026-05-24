class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        pe = intervals[0][1]

        for i,j in intervals[1:]:
            if i>= pe:
                pe = j
            else:
                res+=1
                pe = min(pe,j)
        
        return res
        