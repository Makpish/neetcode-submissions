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
            if not lt:
                return 0,False
            rh,rt = dfs(node.right)

            if not rt or abs(lh-rh)>1:
                return 0,False
            
            return 1+max(lh,rh),True
        return dfs(root)[1]
        