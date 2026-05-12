class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        hq = []
        for i in nums:
            if i not in x:
                x[i] = 0
            x[i]+=1
        
        for i in x.keys():
            heapq.heappush(hq, (-x[i], i))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(hq)[1])
        return res
        