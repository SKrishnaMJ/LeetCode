"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        my_dict={}
        def dfs(node):
            if node in my_dict:
                return my_dict[node]
            copy = Node(node.val)
            my_dict[node]=copy
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
            return copy
        if node:
            return dfs(node)


        