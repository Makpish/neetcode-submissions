class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mh = []
        for i in stones:
            heapq.heappush(mh,-i)
        
        while len(mh)>1:
            x = heapq.heappop(mh)
            y = heapq.heappop(mh)
            if x==y:
                continue
            heapq.heappush(mh, -abs(x-y))
        
        return 0 if not mh else -mh[0]
        