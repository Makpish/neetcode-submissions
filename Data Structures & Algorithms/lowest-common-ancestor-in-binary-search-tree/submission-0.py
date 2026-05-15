# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        if q.val<p.val:
            p,q = q,p
        
        if (root.val > p.val and root.val < q.val) or (root.val == p.val or root.val == q.val):
            return root
        
        x = self.lowestCommonAncestor(root.left, p, q)
        if x:
            return x
        return self.lowestCommonAncestor(root.right, p, q)
        

        