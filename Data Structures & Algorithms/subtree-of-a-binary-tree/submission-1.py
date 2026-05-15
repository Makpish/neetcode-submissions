# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def find(node, snode):
            if not node:
                return None
            
            if node.val == snode.val:
                self.l.append(node)
            
            find(node.left, snode)
            find(node.right, snode)
        
        def struct(n1, n2):
            if not n1 and not n2:
                return True
            
            if not n1 or not n2 or n1.val != n2.val:
                return False
            
            return struct(n1.left, n2.left) and struct(n1.right, n2.right)
        
        if not subRoot and root:
            return False
        
        self.l = []
        find(root, subRoot)
        if len(self.l) < 1:
            return False
        
        for n in self.l:
            if struct(n, subRoot):
                return True
        return False
        