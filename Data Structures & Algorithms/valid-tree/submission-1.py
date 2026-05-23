class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:set() for i in range(n)}
        for i,j in edges:
            adj[i].add(j)
            adj[j].add(i)
        vis = set()
        def dfs(c,prev):
            for i in adj[c]:
                if prev!= None and i == prev:
                    continue
                if i in vis:
                    return False
                vis.add(i)
                if not dfs(i,c):
                    return False
            return True
        vis.add(0)
        if dfs(0,None) and len(vis) == n:
            return True
        return False
            

            
        