# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        def dfs(n,h):
            if not n:
                return
            if len(self.ans)<h:
                self.ans.append(0)
            self.ans[h-1] = n.val
            dfs(n.left, h+1)
            dfs(n.right, h+1)
        dfs(root,1)
        return self.ans
            
        