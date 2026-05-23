class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(n+1)}

        for i,j,w in times:
            adj[i].append([j,w])
        
        minhp = [[0,k]]
        vis = set()
        m = 0
        while minhp:
            w, a = heapq.heappop(minhp)
            if a in vis:
                continue
            m = w
            vis.add(a)
            
            for j,w2 in adj[a]:
                if j not in vis:
                    heapq.heappush(minhp, [w+w2, j])
        # print(vis)
        if len(vis) != n:
            return -1
        
        return m
        