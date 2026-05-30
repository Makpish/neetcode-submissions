# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0,True
            lh,lt = dfs(node.left)
            rh,rt = dfs(node.right)

            if not lt or not rt or abs(lh-rh)>1:
                return 0,False
            
            return 1+max(lh,rh),True
        return dfs(root)[1]
        