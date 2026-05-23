class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        vis = set()

        def dfs(i,prev):
            if i in vis:
                return
            vis.add(i)
            for j in adj[i]:
                if j==prev or j in vis:
                    continue
                dfs(j,i)

        c=0
        for i in range(n):
            vl = len(vis)
            dfs(i,-1)
            if len(vis) > vl:
                c+=1
        return c
        