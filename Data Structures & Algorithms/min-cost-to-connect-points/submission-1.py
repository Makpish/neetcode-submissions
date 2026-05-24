class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        vis = set()
        minhp = [[0, points[0][0], points[0][1]]]
        # nonvis = set()
        # for i,j in points:
        #     nonvis.add((i,j))
        cost = 0

        while minhp and len(vis) < len(points):
            w,x,y = heapq.heappop(minhp)

            if (x,y) in vis:
                continue
            
            vis.add((x,y))
            # nonvis.remove((x,y))

            cost += w

            for i,j in points:
                if (i,j) not in vis:
                    heapq.heappush(minhp, [abs(x-i) + abs(y-j), i, j])
        
        return cost


        