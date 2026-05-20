# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.m = root.val
        def check(node):
            if not node:
                return 0
            
            l = max(0,check(node.left))
            r = max(0,check(node.right))

            self.m = max(self.m, l+r+node.val)

            return node.val + max(l,r)
        
        check(root)
        return self.m

        