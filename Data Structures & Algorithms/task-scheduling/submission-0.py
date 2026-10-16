class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap = {}
        for i in tasks:
            hmap[i] = 1 + hmap.get(i,0)

        # hmap = {}
        maxh = [-i for i in hmap.values()]
        heapq.heapify(maxh)
        q = deque()
        t = 0

        while maxh or q:
            t+=1

            if maxh:
                c = 1+heapq.heappop(maxh)
                if c:
                    q.append([c, t+n])
            
            if q and q[0][1] <= t:
                heapq.heappush(maxh, q.popleft()[0])
        
        return t



        