class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            adj[i].append(j)
        
        vis = set()
        def dfs(c):
            if c in vis:
                return False
            if adj[c] == []:
                return True
            
            vis.add(c)
            for i in adj[c]:
                if not dfs(i): return False
            
            vis.remove(c)
            adj[c] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        