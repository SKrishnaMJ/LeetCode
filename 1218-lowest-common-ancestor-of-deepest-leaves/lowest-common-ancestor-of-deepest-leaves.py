# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.res_node = None
        self.max_depth = -1

        self.dfs(root,0)

        return self.res_node

    def dfs(self, node, depth):
        if not node:
            return 0
        if not node.left and not node.right:
            if depth>self.max_depth:
                self.res_node = node
                self.max_depth = depth
            return depth
        l = self.dfs(node.left, depth+1)
        r = self.dfs(node.right, depth+1)
        if l==r==self.max_depth:
            self.res_node = node
        return max(l,r)

        
        
        