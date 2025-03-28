# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        s=[]
        def traversal(node):
            if node:
                traversal(node.left)
                s.append(node.val)
                traversal(node.right)
        traversal(root)
        res=float("inf")
        for i in range(1,len(s)):
            diff = abs(s[i]-s[i-1])
            res=min(res,diff)
        return res
        