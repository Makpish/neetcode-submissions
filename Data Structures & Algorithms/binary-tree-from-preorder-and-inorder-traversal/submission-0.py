# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)<1:
            return None
        
        n = TreeNode(preorder[0])

        i=0
        while inorder[i] != n.val:
            i+=1
        
        n.left = self.buildTree(preorder[1:i+1], inorder[0:i])
        n.right = self.buildTree(preorder[i+1:len(preorder)], inorder[i+1:len(inorder)])
        return n
        