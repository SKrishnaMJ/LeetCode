# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.subTree = None
        self.max_depth = -1

        self.dfs(root, 0)

        return self.subTree

    def dfs(self, node, depth):
        if not node:
            return 0
        if not node.right and not node.left:
            if depth>self.max_depth:
                self.subTree = node
                self.max_depth = depth
            return depth

        l = self.dfs(node.left, depth+1)
        r = self.dfs(node.right, depth+1)

        if l==r==self.max_depth:
            self.subTree = node

        return max(l,r)
        