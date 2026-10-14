class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []
        for s in stones:
            heapq.heappush(hp, -s)
        
        while len(hp)>1:
            x,y=-heapq.heappop(hp),-heapq.heappop(hp)
            r = abs(x-y)
            if r>0:
                heapq.heappush(hp, -r)
        
        if len(hp) == 0:
            return 0
        return -hp[0]


        