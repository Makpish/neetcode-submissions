class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dirx = [-1,0,1,0]
        diry = [0,-1,0,1]

        minh = [[grid[0][0], 0, 0]]
        n=len(grid)
        m=len(grid[0])

        vis=set()
        # res = float("-inf")

        while minh:
            # print(minh)
            w, x,y = heapq.heappop(minh)

            if (x,y) in vis:
                continue
            if x==n-1 and y==m-1:
                return w
            
            vis.add((x,y))
            # res = max(res, w)

            for i in range(4):
                x1 = x+dirx[i]
                y1 = y+diry[i]
                if x1>=0 and x1<n and y1>=0 and y1<m:
                    heapq.heappush(minh, [max(w,grid[x1][y1]), x1, y1])
        return -1



        