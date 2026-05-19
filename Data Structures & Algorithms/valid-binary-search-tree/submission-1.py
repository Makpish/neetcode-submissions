# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def cbst(node, l, r):
            if not node:
                return True
            
            if node.val <= l or node.val >= r:
                return False
            
            return cbst(node.left, l, node.val) and cbst(node.right, node.val, r)
        
        return cbst(root, float("-inf"), float("inf"))
            
        