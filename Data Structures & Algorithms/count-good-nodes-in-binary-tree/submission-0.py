# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.c = 0
        def dfs(n,m):
            if not n:
                return
            if n.val >= m:
                self.c+=1
            dfs(n.left, max(m,n.val))
            dfs(n.right, max(m,n.val))
        dfs(root,root.val)
        return self.c
        