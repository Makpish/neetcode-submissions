class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        dirx = [-1,0,1,0]
        diry = [0,-1,0,1]

        res = []

        def dfs(i,j):
            vis = set()
            done = set()
            st = [(i,j)]

            while st and len(done)<2:
                x,y = st.pop()
                if (x,y) in vis:
                    continue
                vis.add((x,y))

                if x==0 or y==0:
                    done.add("P")
                if x==n-1 or y==m-1:
                    done.add("A")
                for a in range(4):
                    x1,y1 = x+dirx[a], y+diry[a]
                    if x1<0 or y1<0 or x1==n or y1==m or heights[x1][y1]>heights[x][y]:
                        continue
                    st.append((x1,y1))
            
            return len(done)==2
        
        for i in range(n):
            for j in range(m):
                if dfs(i,j):
                    res.append([i,j])
        return res

        