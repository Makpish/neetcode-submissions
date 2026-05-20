# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.m = float("-inf")
        def check(node):
            if not node:
                return float("-inf")
            
            l = check(node.left)
            r = check(node.right)

            self.m = max(self.m, l, r, l+r+node.val, node.val + l, node.val+r, node.val)

            return max(node.val + l, node.val + r, node.val)
        
        check(root)
        return self.m

        