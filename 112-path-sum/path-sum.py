# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def summ(node,cur_sum):
            if not node:
                return False
            cur_sum+=node.val
            if not node.left and not node.right:
                return targetSum==cur_sum
            return summ(node.left,cur_sum) or summ(node.right,cur_sum)
        return summ(root,0)
        