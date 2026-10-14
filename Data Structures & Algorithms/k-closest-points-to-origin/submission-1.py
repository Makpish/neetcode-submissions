class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dis(x,y):
            return (x**2 + y**2)**0.5
        
        maxhp = []

        for x,y in points:
            heapq.heappush(maxhp, [-dis(x,y), [x,y]])
            if len(maxhp)>k:
                heapq.heappop(maxhp)
        
        return [i for _,i in maxhp]

        