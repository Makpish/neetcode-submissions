# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def height(node, h):
            if not node:
                return
            
            if len(res)<h:
                res.append([])
            
            res[h-1].append(node.val)

            height(node.left, h+1)
            height(node.right, h+1)
        
        height(root,1)
        return res

        