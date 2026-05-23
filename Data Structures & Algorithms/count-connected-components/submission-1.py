class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # adj = {i:[] for i in range(n)}
        # for i,j in edges:
        #     adj[i].append(j)
        #     adj[j].append(i)
        
        # vis = set()

        # def dfs(i,prev):
        #     if i in vis:
        #         return
        #     vis.add(i)
        #     for j in adj[i]:
        #         if j==prev or j in vis:
        #             continue
        #         dfs(j,i)

        # c=0
        # for i in range(n):
        #     vl = len(vis)
        #     dfs(i,-1)
        #     if len(vis) > vl:
        #         c+=1
        # return c

        parent = [i for i in range(n)]
        rank = [1]*n

        def find(n1):
            res = n1
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1] += 1
            
            else:
                parent[p1] = p2
                rank[p2] += 1
            return 1
        
        res = n
        for i,j in edges:
            res -= union(i,j)
        return res
        