# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node, val):
            if not node:
                return
            if node.val == val:
                return node
            if val<node.val:
                return search(node.left, val)
            else:
                return search(node.right, val)
        
        return search(root, val)
        