# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if abs(l-r)>1:
                res[0]=False
                return 0
            return 1+max(l,r)
        dfs(root)
        return res[0]
        

        