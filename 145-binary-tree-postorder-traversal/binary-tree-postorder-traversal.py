# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def pot(root):
            if root is not None:
                pot(root.left)
                pot(root.right)
                ans.append(root.val)
            return ans
        return pot(root)


        