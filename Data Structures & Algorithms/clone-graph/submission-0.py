"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hmap = {}

        vis = set()

        def dfs(n):
            if n in vis:
                return hmap[n]
            if n not in hmap:
                hmap[n] = Node(n.val)
            vis.add(n)
            
            for i in n.neighbors:
                x = dfs(i)
                # print(x)
                hmap[n].neighbors.append(x)
            return hmap[n]

        
        dfs(node)

        return hmap[node]

        