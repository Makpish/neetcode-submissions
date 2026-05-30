class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mh = []
        for i,j in points:
            heapq.heappush(mh, [-(i**2 + j**2)**0.5,[i,j]])
            if len(mh)>k:
                heapq.heappop(mh)
        
        return [i[1] for i in mh]
        