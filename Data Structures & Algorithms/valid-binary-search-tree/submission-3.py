# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        queue = deque()
        queue.append((root, float('-inf'), float('inf')))

        while queue:
            node, minn, maxx = queue.popleft()

            if not (minn < node.val < maxx): return False

            if node.left: queue.append((node.left, minn, node.val))

            if node.right: queue.append((node.right, node.val, maxx))

        return True

        

        