class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirx = [-1,0,1,0]
        diry = [0,-1,0,1]

        vis = set()

        def dfs(x,y):
            st = [(x,y)]

            while st:
                a,b = st.pop()
                if (a,b) in vis:
                    continue
                vis.add((a,b))
                
                for i in range(4):
                    a1,b1 = a+dirx[i], b+diry[i]

                    if a1<0 or a1==len(grid) or b1<0 or b1==len(grid[0]):
                        continue
                    
                    if (a1,b1) not in vis and grid[a1][b1] == "1":
                        st.append((a1,b1))
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in vis and grid[i][j] == "1":
                    c+=1
                    dfs(i,j)
        return c
        